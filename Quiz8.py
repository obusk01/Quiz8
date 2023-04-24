# Olivia Busk, Rosemary Hoffman, and Katherine O'Roark

#7

fruits={"apple":"red","banana":"yellow","grape":"purple","pear":"green"}

x=fruits.values()
print(x)
#5
books={"harry potter":"JK Rowling","to the lighthouse":"Virginia Woolf","The sun also rises":"Hemmingway"}
x=books.values()
print(x)

#8
import random
x=random.randint(1,10)
guess=int(input("what is your guess?"))
while guess !=x:
    print("sorry, try again")
    guess=int(input("what is your guess?"))
if guess==x:
    print("congratulations your guess is correct")

#1
students={"bobby":30,"jane":40,"catherine":60}
def scores(x):
    list=[]
    for key in x:
        if x[key] <= 50:
            list.append(key)
    print(list)

scores(students)
