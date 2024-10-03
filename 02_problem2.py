# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update
# the Hi-score whenever the game() function breaks the Hi-score.

import random

def game():
    print("You are playing the Game:")
    score = random.randint(1,1001)
    # fetch the Hiscore
    with open("02_Hi-score.txt") as f:
        hiscore=f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f'Your score: {score}')

    if(score>hiscore):
        # write this hiscore to the file
        with open("02_Hi-score.txt","w")as f:
            f.write(str(score))
    return score

game()


# import random
# def game():
#     print("Yu are playing")
#     score = random.randint(1,1000)
#     with open("02_Hi-score.txt") as f:
#         hiscore=f.read()
#         if(hiscore != ""):
#             hiscore = int(hiscore)
#         else:
#             hiscore=0
#     print(f'score:{score}')
#
#     if(score>hiscore):
#         with open("02_Hi-score.txt","w")as f:
#             f.write(str(score))
#     return score
#
# game()




# import random
#
# def game2():
#     print("You are playing:")
#     score = random.randint(1,1000)
#     with open("02_Hi-score.txt")as f:
#         hiscore=f.read()
#         if (hiscore != ""):
#             hiscore=int(hiscore)
#         else:
#             hiscore=0
#     print(f"Score:{score}")
#
#     if(score>hiscore):
#         with open("02_Hi-score.txt","w") as f:
#             f.write(str(score))
#     return score
#
# game()