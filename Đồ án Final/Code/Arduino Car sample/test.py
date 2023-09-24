import pyfirmata
import time
from pyfirmata import util

board = pyfirmata.Arduino('COM3')
iterator = util.Iterator(board)
iterator.start()

# pin = board.get_pin('d:13:o')
# time.sleep(1)
# print(pin.read())

while True:
    board.digital[13].write(1)
    time.sleep(5)
    board.digital[13].write(0)
    time.sleep(1)