print("welcome to the love calculator")
name1 = input("Write your Name: \n ")
name2 = input("Write Their Name: \n ")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t+r+u+e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l+o+v+e

love_score =int(str(true) + str(love))

if(love_score<20) or (love_score>90):
  print(f"Your love score is {love_score}, you are not made for each other ")
elif(love_score>=40) and (love_score<=70):
  print("you are perfect for each other,your love is outstanding")
else:
  print(f"Your love score is {love_score} you both are loving too much")  

