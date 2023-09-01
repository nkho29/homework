import logging

logging.basicConfig(filename="logs_hw.log", level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")

count = [1,2,3,4]
count1 = {1:2, 2:3, 3:"Three"}

try:
    print(count[4])
except Exception as er:
    logging.error(msg="{result}", exc_info=True)
    print("ErRoR!!!", er)

try:
    print(count1[6])
except KeyError as er:
    logging.debug(msg="{result}", exc_info=True)
    print(f"This key {er} not found in dict!")
else:
    print("In block try all correct!")
finally:
    print("End!")