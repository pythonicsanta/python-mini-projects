secret_number= 11
chances=3
while chances>0:
    guess=int(input("enter Your number: "))
    if guess==secret_number:
        print("Correct! You won.")
        break
    elif guess>secret_number:
        print("Too High! Try again.")
    else:
        print("Too Low! Try again.")
    chances=chances-1
    print("Chances Left", chances)
if chances==0:
    print("Game Over! Want to play Again")