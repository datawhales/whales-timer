import sys
import time

start = time.time()

while True:
    sys.stdout.write(f"{time.time() - start:.4f}\r")
    sys.stdout.flush()
