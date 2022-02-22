import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')
logging.info("Just like that!")
x = logging.info("Just like that!")
print("x: ",x)
#> 2019-02-17 11:40:38,254 :: INFO :: Just like that!