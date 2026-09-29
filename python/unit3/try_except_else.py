try:
    attempts = int(input("enter the number of attempts: "))
except ValueError:
    print ("Please enter a valid positive integer")
else:
    print ("Login attempts recorded:",attempts)