# reading file
# f= open("main.txt")
# data = f.read()
# print(data)
# f.close()


# write file
# add = "hey he is student of SOIT RGPV Bhopal"
# f = open("main2.txt", "a")
# f.write(add)
# f.close()


# close case 
# with open("main.txt") as f:
#     print(f.read())
    # dont need to explicitly close the file


# counter mtd
# def count_word(file_path):
#     word_length = len(f.read().split())
#     return word_length

# f= open("main.txt")
# data = f.read()
# counter = count_word(data)
# if("Twinkle" in data):
#     print("the word twinkle is present in content")
#     print(counter)
# else:
#     print("the word is not present") 
# f.close()

# game 
import random

# def game():
#     print("you are playing game!!")
#     score = random.randint(1,50)
#     with open("main2.txt") as f:
#         hiscore = f.read()
#         if(hiscore != ""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0
    
#     print(f"your score : {score}")
#     if(score>hiscore):
#         with open("main2.txt", "w") as f:
#             f.write(str(score))

#     return score

# game()


