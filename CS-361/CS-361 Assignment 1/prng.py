import time
import random

# This loop function will open a txt file and write "run", then compare the string to the string we
# want, and generates a random number between 1-10. and writes that in the same file.
while True:
    time.sleep(1.0)
    f = open("prng-service.txt", "r")
    read_text = f.readline()
    print(read_text)
    f.close()

    if read_text == "run":
        value = random.randint(1, 10)
        print(value)
        f = open("prng-service.txt", "w")
        f.write(str(value))
    f.close()
