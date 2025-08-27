import time

while True:
    Input = input("Type Start to Start: \n")
    if Input == "Start":
        f = open("Request.txt", "w")
        f.write("Send a number")
        f.close()
        time.sleep(5)
        f = open("Request.txt", "r")
        print(f.readline())
        f.close()

    q = input("You would like to use the system again? (yes/no): ").lower()
    if q == 'yes':
        """This describes that if the user input is equal to yes, then we rerun the system.
        Since the statement is still true."""
        pass
    elif q == 'no':
        print("Thank you for using my Software, Hope it was helpful.")
        break
    else:
        break
