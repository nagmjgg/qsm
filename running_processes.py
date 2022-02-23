import os
import subprocess

# Running the aforementioned command and saving its output
output = os.popen('wmic process get description, processid').read()
cmd = "get-wmiobject Win32_process -filter \"Name='python.exe'\" | foreach -process {$_.CommandLine}"
output2 = subprocess.run(["powershell","-Command",cmd], capture_output=True)

# Displaying the output
#print(output)
print(output2)