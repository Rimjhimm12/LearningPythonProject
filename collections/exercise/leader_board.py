import random

score = [1,2,3,4,5,6]
print(score)

for i in range(9):          # simulate 5 more rounds
    goal = random.randint(0, 1)   # dynamically decide: 1 = goal, 0 = no goal
    if goal == 1:
        score.append(score[-1] + 1)   # goal -> next entry increases
    else:
        score.append(score[-1])       # no goal -> next entry repeats
    print(score)
