import random
user_score = 0
system_score = 0
print("------------------------------welcome to the game-----------------------------")
while True:
    user_choice = input("type your choice: rock/paper/scissors or q to quit:").lower()
    if user_choice == 'q':
        break
    if user_choice not in ["rock", "paper", "scissors"]:
        print("give valid option")
        continue
    system_choice = random.choice(["rock", "paper", "scissors"])
    print("your choice:", user_choice)
    print("computer choice:", system_choice)
    if user_choice == "rock" and system_choice == "scissors":
        print("------you win-----")
        user_score += 1
        continue
    if user_choice == "paper" and system_choice == "rock":
        print("------you win-----")
        user_score += 1
        continue
    if user_choice == "scissors" and system_choice == "paper":
        print("------you win-----")
        user_score += 1
        continue
    if system_choice == user_choice:
        print("----draw---")
        continue
    print("-----you lose-----")
    system_score += 1

print("your score:", user_score)
print("system score:", system_score)
if user_score > system_score:
    print("----------------------you win-------------------")
elif system_score > user_score:
    print("----------------------you lose-------------------")
elif system_score == user_score and (system_score>0 and user_score>0):
    print("-------------------match draw---------------------")
print("-------------------thanks for playing game------------------")