# Program reads number sequens and counts how many of them
# are even, and how many are odd.
# Program ends after user inputs "0"

odd = 0
even = 0

# inpuut a number number
number = int(input("Input a number, or input \"0\" to end the program: "))

# 0 ends execution
while number != 0:
    # check if a number is odd
    if number % 2 == 1:
        # increase odd count
        odd += 1
    else:
        # increase even count
        even += 1
    # input another number
    number = int(input("Input a number, or input \"0\" to end the program: "))

# display results
print("Odd count equals to: ", odd, sep="")
print("Even count equals to: ", even, sep="")