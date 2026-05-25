# secret_number=7
# guess=int(input("Enter your Guessed Number: "))
# if guess== secret_number:
#     print("Correct! You guessed it.")
# else:
#     print("Wrong")

secret_number= 8
guess=int(input("Enter your Guess Number: "))
if guess== secret_number:
    print("Correct! you guess it right.")
elif guess> secret_number:
    print("Too high.")
else:
    print("Too low.")