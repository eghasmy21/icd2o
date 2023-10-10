name = input("enter your name")

print ()

print("Game 1")
opponent1 = input("Enter opponent's name: ")
opponent1_score = int(input("Enter opponent's score: "))
your_score1 = int(input("Enter your score: "))



print("game 2")
opponent2 = input("Enter opponent's name: ")
opponent2_score = int(input("Enter opponent's score: "))
your_score2 = int(input("Enter your score: "))

print ()

print("Game 3")
opponent3 = input("Enter opponent's name: ")
opponent3_score = int(input("Enter opponent's score: "))
your_score3 = int(input("Enter your score: "))

print ()

print("Game 4")
opponent4 = input("Enter opponent's name: ")
opponent4_score = int(input("Enter opponent's score: "))
your_score4 = int(input("Enter your score: "))

print()

print("Game 5")
opponent5 = input("Enter opponent's name: ")
opponent5_score = int(input("Enter opponent's score: "))
your_score5 = int(input("Enter your score: "))

print()

#Calculate statistics
total_your_score = your_score1 + your_score2 + your_score3 + your_score4 + your_score5
total_opponents_score = opponent1_score + opponent2_score + opponent3_score + opponent4_score + opponent5_score
percentage_boxes_created = (total_your_score / 36) * 100

print(f"The total points you got was {total_your_score}")
print(f"the total pinots your opponent got was {total_opponents_score}")

#Display data in a table format
print("Opponent's Name   Your Points   Opponent's Points    Percentage of Boxes Created")
print(f"{opponent1}                  {your_score1}            {opponent1_score}                   {your_score1*100/36}%")
print(f"{opponent2}                  {your_score2}            {opponent2_score}                   {your_score2*100/36}%")
print(f"{opponent3}                  {your_score3}            {opponent3_score}                   {your_score3*100/36}%")
print(f"{opponent4}                  {your_score4}            {opponent4_score}                   {your_score4*100/36}%")
print(f"{opponent5}                  {your_score5}            {opponent5_score}                   {your_score5*100/36}%") 