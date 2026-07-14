'''A cricket tournament records players’ jersey numbers.

* Duplicate jersey numbers are not allowed.'''


players_jersey_no={2,3,4,2,5,6,3}
players_jersey_no_list=[2,9,8,3]
print(players_jersey_no)
#or
for i in players_jersey_no_list:
    if i not in players_jersey_no:
        players_jersey_no.add(i)
print(players_jersey_no)