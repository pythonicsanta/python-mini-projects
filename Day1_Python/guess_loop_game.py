secret_number= 9
while True:
    guess=int(input("Guess the number: "))
    if guess==secret_number:
        print("Correct answer! You Won.")
        break
    elif guess>secret_number:
        print("Too High! Try Again")
    else:
        print("Too Low! Try Again")