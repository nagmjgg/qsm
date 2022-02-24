# Copyright (c) 2013 phrack. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import math
from PIL import Image, ImageTk
import platform
import re
from tag_parser import TagParser
from target_pickler import TargetPickler
from threading import Thread
import time

DURATION_INDEX = 0
FIRST_IMAGE_INDEX = 1
FIRST_PHOTOIMAGE_INDEX = 2
LAST_IMAGE_INDEX = 3
FRAMES_INDEX = 4


# This class manages operations common to the webcam feed canvas
# and the target editor canvas
class CanvasManager():
    def selection_update_listener(self, old_selection, new_selection):
        self._selection = new_selection

        # Some of the ttk widgets steal focus, so we need to get it back
        # to the canvas on click
        self._canvas.focus_set()

        # brighten the old selection and make its outline black
        if (old_selection and
                not self.is_background(old_selection)):

            tags = self._canvas.gettags(old_selection)
            if not "_shape:image" in tags and not "visible:false" in tags:
                self._canvas.itemconfig(old_selection, stipple="gray25",
                                        outline="black")

                # On windows we need to do a little trick by converting any selected
            # ovals into a regular polygon with many sides, otherwise they won't
            # be transparent. We only do this when an oval is selected because
            # transparency is only really important when sizing and moving
            # a target or region.

            # We are checking to see if the selection was a tuple meaning it's
            # from the target editor. This transparency hack only works on the
            # webcam feed because the state is harder to track on the target editor
            if (platform.system() == "Windows" and
                    not isinstance(old_selection, tuple)):
                self.convert_ovals(old_selection, self.convert_from_windows_ovals)

                # darken the new one and make its outline gold
        if (new_selection and
                not self.is_background(new_selection)):

            tags = self._canvas.gettags(new_selection)
            if not "_shape:image" in tags and not "visible:false" in tags:
                self._canvas.itemconfig(new_selection, stipple="gray50",
                                        outline="gold")

            if (platform.system() == "Windows" and
                    not isinstance(new_selection, tuple)):
                self.convert_ovals(new_selection, self.convert_to_windows_ovals)

    def draw_windows_oval(self, x, y, radius, fill, tags):
        # What we are doing here is drawing a regular polygon with
        # 20 sides, which reasonably approximates a circle of most sizes
        sides = 20
        points = []
        offsetx = x - (radius / 2)
        offsety = y - (radius / 2)
        ang = 2 * math.pi / sides

        for i in range(sides):
            deg = (i + .5) * ang
            newx = math.sin(deg) / 2.0 + .5
            newy = math.cos(deg) / 2.0 + .5
            points.append(newx * radius + offsetx)
            points.append(newy * radius + offsety)

        return self._canvas.create_polygon(*points, fill=fill,
                                           outline="gold", stipple="gray50", tags=tags)

    def convert_ovals(self, selection, converter):
        regions = self._canvas.find_withtag(selection)

        for region in regions:
            tags = self._canvas.gettags(region)
            if "_shape:oval" in tags:
                # get whatever is above it so that we can keep
                # the z order the same
                higher = self._canvas.find_above(region)

                # preserve the fill color
                fill = self._canvas.itemcget(region, "fill")

                oval = converter(region, fill, tags)
                self._canvas.tag_raise(higher, oval)
                self._canvas.delete(region)

        # Restore z-order otherwise targets with ovals disappear
        # on projector arena
        self._canvas.tag_lower("background")
        self._canvas.tag_lower("visible:false", "background")

    def convert_to_windows_ovals(self, region, fill, tags):
        # get its coords so we can figure out how to draw it
        coords = self._canvas.coords(region)
        width = (coords[2] - coords[0])
        height = (coords[3] - coords[1])
        x = coords[2] - (width / 2)
        y = coords[3] - (height / 2)

        return self.draw_windows_oval(x, y, width, fill, tags)

    def convert_from_windows_ovals(self, region, fill, tags):
        # get its coords so we can figure out how to draw it
        coords = self._canvas.coords(region)
        max_x = max(coords[::2])
        min_x = min(coords[::2])
        max_y = max(coords[1::2])
        min_y = min(coords[1::2])

        return self._canvas.create_oval(min_x, min_y, max_x, max_y, fill=fill,
                                        stipple="gray25", tags=tags)

    def move_region(self, event):
        if (self._selection and
                not self.is_background(self._selection)):

            if event.keysym == "Up":
                event.widget.move(self._selection, 0, -1)
            elif event.keysym == "Down":
                event.widget.move(self._selection, 0, 1)
            elif event.keysym == "Right":
                event.widget.move(self._selection, 1, 0)
            elif event.keysym == "Left":
                event.widget.move(self._selection, -1, 0)

    def scale_region(self, event):
        if (not self._selection or
                self.is_background(self._selection)):
            return

        c = event.widget.coords(self._selection)
        is_polygon = len(c) > 6

        for region in self._canvas.find_withtag(self._selection):
            is_image = "_shape:image" in self._canvas.gettags(region)
            if is_image:
                break

        # If there is an image we have to scale every region one at a time
        # otherwise the images won't get scaled correctly
        if is_image:
            if isinstance(self._selection, tuple):
                self._scale_region(event, c, is_polygon, is_image, self._selection[0], 20)
            else:
                for region in self._canvas.find_withtag(self._selection):
                    c = event.widget.coords(region)
                    is_polygon = len(c) > 6
                    is_image = "_shape:image" in self._canvas.gettags(region)
                    if is_image:
                        self._scale_region(event, c, is_polygon, is_image, region, 20)
                    else:
                        self._scale_region(event, c, is_polygon, is_image, region)
        else:
            self._scale_region(event, c, is_polygon, is_image, self._selection)

    def _scale_region(self, event, c, is_polygon, is_image, region, size_incr=1):
        # The region is scaled by a ratio, so we need to know the current
        # dimension so that we can calculate the ratio needed to scale
        # the selection by only one pixel

        # We have to know if it is a polygon (with more sides than the triangle
        # we draw) because polygons are used to approximate circles on windows.
        # Calculating the width and height is different in that case
        if is_polygon:
            width = max(c[::2]) - min(c[::2])
            height = max(c[1::2]) - min(c[1::2])
        elif is_image:
            b = self._image_regions_images[region][FIRST_IMAGE_INDEX].getbbox()
            width = b[2] - b[0]
            height = b[3] - b[1]
        else:
            width = c[2] - c[0]
            height = c[3] - c[1]

        if event.keysym == "Up":
            # The vertical growth direction is reverse with a polygon hack for
            # windows
            if is_polygon:
                scale_factor = (height + size_incr) / height
                if (scale_factor > 0):
                    event.widget.scale(region, c[0], c[1], 1, scale_factor)
            elif is_image:
                height += size_incr
            else:
                if height - size_incr <= 0: return
                scale_factor = (height - size_incr) / height
                if (scale_factor > 0):
                    event.widget.scale(region, c[0], c[1], 1, scale_factor)
        elif event.keysym == "Down":
            if is_polygon:
                if height - size_incr <= 0: return
                scale_factor = (height - size_incr) / height
                if (scale_factor > 0):
                    event.widget.scale(region, c[0], c[1], 1, scale_factor)
            elif is_image:
                height -= size_incr
            else:
                scale_factor = (height + size_incr) / height
                if (scale_factor > 0):
                    event.widget.scale(region, c[0], c[1], 1, scale_factor)
        elif event.keysym == "Right":
            if is_image:
                width += size_incr
            else:
                scale_factor = (width + size_incr) / width
                if (scale_factor > 0):
                    event.widget.scale(region, c[0], c[1], scale_factor, 1)
        elif event.keysym == "Left" and width > 1:
            if is_image:
                width -= size_incr
            else:
                if width - size_incr <= 0: return
                scale_factor = (width - size_incr) / width
                if (scale_factor > 0):
                    event.widget.scale(region, c[0], c[1], scale_factor, 1)

        if is_image:
            tags = TagParser.parse_tags(self._canvas.gettags(region))
            self.cache_image_frames(region, tags["_path"], width, height)
            self._canvas.itemconfig(region, image=self._image_regions_images[region][FIRST_PHOTOIMAGE_INDEX])

    def cache_image_frames(self, shape, image_path, width=None, height=None):
        image = Image.open(image_path)
        frames = []

        try:
            while True:
                if width != None and height != None:
                    frames.append(image.copy().resize((width, height), Image.NEAREST))
                else:
                    frames.append(image.copy())
                image.seek(len(frames))
        except EOFError:
            pass

        if len(frames) == 1:
            self._image_regions_images[shape] = (0, frames[0], ImageTk.PhotoImage(frames[0]), frames[0], None)
            return self._image_regions_images[shape][FIRST_PHOTOIMAGE_INDEX]

        if "duration" in image.info:
            if image.info["duration"] != 0:
                animation_delay = float(image.info["duration"]) / 1000.0
            else:
                animation_delay = .1
        else:
            animation_delay = .1

        first = frames[0].convert('RGBA')
        frame_images = [ImageTk.PhotoImage(first)]

        temp = frames[0]
        for img in frames[1:]:
            temp.paste(img)
            frame = temp.convert('RGBA')
            frame_images.append(ImageTk.PhotoImage(frame))

        self._image_regions_images[shape] = (
        animation_delay, first, ImageTk.PhotoImage(first), frames[len(frames) - 1].convert('RGBA'), frame_images)

        return self._image_regions_images[shape][FIRST_PHOTOIMAGE_INDEX]

    # finish_frame is ImageTk.PhotoImage or None (if none, assume last frame)
    def animate(self, region, finish_frame=None, reverse=False):
        Thread(target=self._animate, args=(region, finish_frame, reverse)).start()

    def _animate(self, region, finish_frame, reverse):
        # Don't try to animate images that have only one frame
        if self._image_regions_images[region][DURATION_INDEX] == 0:
            return

        frames = list(self._image_regions_images[region][FRAMES_INDEX])

        ran_reversed = False
        if str(self._canvas.itemcget(region, "image")) != str(
                self._image_regions_images[region][FIRST_PHOTOIMAGE_INDEX]):
            # Don't repeat a non-reversable animation if the target is on the last frame
            if not reverse:
                return
            else:  # If it's a reversable frame and we are on the last frame, then reverse the animation
                ran_reversed = True
                frames.reverse()

        self._play_animation(region, frames,
                             self._image_regions_images[region][DURATION_INDEX], 0, finish_frame)

        if reverse and ran_reversed:
            self._image_regions_images[region] = (
                self._image_regions_images[region][DURATION_INDEX],
                self._image_regions_images[region][FIRST_IMAGE_INDEX],
                self._canvas.itemcget(region, "image"),
                self._image_regions_images[region][LAST_IMAGE_INDEX],
                self._image_regions_images[region][FRAMES_INDEX]
            )

        self._canvas.tag_lower("background")
        self._canvas.tag_lower("visible:false", "background")

    def _play_animation(self, region, frames, delay, index, finish_frame):
        if index == len(frames):
            if finish_frame != None:
                time.sleep(delay)
                self._canvas.itemconfig(region, image=finish_frame)

            return

        self._canvas.itemconfig(region, image=frames[index])

        time.sleep(delay)
        self._play_animation(region, frames, delay, index + 1, finish_frame)

    def execute_region_commands(self, region, command_list, operations):
        # Don't run commands if the region is a non-reversable image that is on the last frame
        if ("command:reverse" not in self._canvas.gettags(region) and "_shape:image" in self._canvas.gettags(region) and
                str(self._canvas.itemcget(region, "image")) != str(
                    self._image_regions_images[region][FIRST_PHOTOIMAGE_INDEX])):
            return

        args = []

        for command in command_list:
            # Parse the command name and arguments arguments are expected to
            # be comma separated and in between paren:
            # command_name(arg0,arg1,...,argN)
            pattern = r'(\w[\w\d_]*)\((.*)\)$'
            match = re.match(pattern, command)
            if match:
                command = match.groups()[0]
                if len(match.groups()) > 0:
                    args = match.groups()[1].split(",")

            # Run the commands
            if command == "reset":
                operations.reset()

            if command == "play_sound":
                operations.play_sound(args[0])

            if command == "animate":
                reverse = False
                if "reverse" in command_list:
                    reverse = True

                if len(args) != 0:
                    tags = TagParser.parse_tags(self._canvas.gettags(region))

                    for region in self._canvas.find_withtag("name:" + args[0]):
                        # Animate the named region
                        internal_name = "_internal_name:" + tags["_internal_name"]
                        current_tags = self._canvas.gettags(region)

                        if internal_name in current_tags:
                            self.animate(region, None, reverse)
                else:
                    self.animate(region, None, reverse)

    def aggregate_targets(self, current_targets):
        # Create a list of targets, their regions, and the tags attached
        # to those regions so that the plugin can have a stock of what
        # can be shot
        targets = []

        for target in current_targets:
            target_regions = self._canvas.find_withtag(target)
            target_data = {"name": target, "regions": []}
            targets.append(target_data)

            for region in target_regions:
                tags = TagParser.parse_tags(
                    self._canvas.gettags(region))
                target_data["regions"].append(tags)

        return targets

    def is_transparent_pixel(self, region, x, y):
        bbox = self._canvas.bbox(region)
        x = x - bbox[0]
        y = y - bbox[1]

        if str(self._canvas.itemcget(region, "image")) == str(
                self._image_regions_images[region][FIRST_PHOTOIMAGE_INDEX]):
            hit_location_color = self._image_regions_images[region][FIRST_IMAGE_INDEX].getpixel((x, y))
        else:
            hit_location_color = self._image_regions_images[region][LAST_IMAGE_INDEX].getpixel((x, y))

        if (type(hit_location_color) is tuple and hit_location_color[3] == 0):
            return True

        return False

    def is_animated(self, regions):
        for region in regions:
            for tag in self._canvas.gettags(region):
                if "animate" in tag:
                    return True

        return False

    def reset_animations(self):
        image_regions = self._canvas.find_withtag("_shape:image")

        for region in image_regions:
            self._canvas.itemconfig(region, image=self._image_regions_images[region][FIRST_PHOTOIMAGE_INDEX])

    def is_background(self, selection):
        if "background" in self._canvas.gettags(selection):
            return True

        return False

    def add_target(self, name, image_regions_images):
        # The target count is just supposed to prevent target naming collisions,
        # not keep track of how many active targets there are
        target_name = "_internal_name:target" + str(self._target_count)
        self._target_count += 1

        target_pickler = TargetPickler()
        (region_object, regions) = target_pickler.load(
            name, self._canvas, self, target_name)

        return target_name

    def __init__(self, canvas, images):
        canvas.bind('<Up>', self.move_region)
        canvas.bind('<Down>', self.move_region)
        canvas.bind('<Left>', self.move_region)
        canvas.bind('<Right>', self.move_region)
        canvas.bind('<Shift-Up>', self.scale_region)
        canvas.bind('<Shift-Down>', self.scale_region)
        canvas.bind('<Shift-Left>', self.scale_region)
        canvas.bind('<Shift-Right>', self.scale_region)

        canvas.focus_set()

        self._canvas = canvas
        self._selection = None
        self._target_count = 0
        self._image_regions_images = images