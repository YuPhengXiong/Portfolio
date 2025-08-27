import time

# This loop function will take the text in the Prng.py that are stored in a variable, and
# writes and prints into image-service.txt.
while True:
    time.sleep(1.0)
    f = open("image-service.txt", "r")
    read_text = f.readline()
    print(read_text)
    f.close()

    try:
        read_text = int(read_text)
    except:
        pass

    if type(read_text) == int:
        read_text = read_text % 30
        f = open("image-service.txt", "w")
        f.write("/Users/YuPheng Xiong/PycharmProjects/CS-361 Assignment 1/car images/" + str(read_text) + ".jpg")
        print("/Users/YuPheng Xiong/PycharmProjects/CS-361 Assignment 1/car images/" + str(read_text) + ".jpg")
    f.close()
