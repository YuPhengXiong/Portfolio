import time

# This loop function will be taking the input from user, and based on the input,
# going through each sequence. It will open txt files and first write "run" in the file,
# then generates a number between 1-10 after, and display that in the prng-service.txt,
# and then closes and opens the same file reading it. Then next opens the image-service.txt
# and writes the stored data, then lastly will show the destination of the images.
while True:
    Input = input('Type 1 to generate a new image or 2 to exit.\n')
    if Input == "1":
        f = open("prng-service.txt", "w")
        f.write("run")
        f.close()
        time.sleep(5.0)
        f = open("prng-service.txt", "r")
        read_text = f.readline()
        f.close()
        g = open("image-service.txt", "w")
        g.write(read_text)
        g.close()
        time.sleep(5.0)
    # If input is equal to 2, ends UI.
    elif Input == "2":
        quit()
    else:
        print("unknown option")
