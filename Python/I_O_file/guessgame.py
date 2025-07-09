import random

def game():
   score = random.randint(1,50)
   print(f"Playing game your score = {score}")
   
   with open("highscr.txt") as h:
    high_s = int(h.read())
    print(f"Recent high score = {high_s}")
    if(score>high_s):
       with open("highscr.txt","w") as h:
          h.write(str(score))
          print(f"Your score is high {score}")
    else:
       print("your not score high")   

    return score     


game()