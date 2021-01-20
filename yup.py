from os import system

print("Hello mommy!!")
print("For refernce use 129 is 6% of what")
number = int(input("What is the number you have for the first number: "))
numbers = int(input("What percent is {} of something: ".format(number)))
print("INVALID CODE\nMELWARE DOWNLOADING")
huh = input("PRESS ENTER TO CONTINUE")
print("Just kidding lol")
result = (number/numbers)*100
print(number, "is", str(numbers) +"% of", result)
done = input("Are you done ma'am? ").lower()
if done == "yes":
    exit("Have a good day")

hello = True
while hello == True:   
    system('clear')
    print("For refernce use 129 is 6% of what")
    number = int(input("What is the number you have for the first number: "))
    numbers = int(input("What percent is {} of something: ".format(number)))
    result = (number/numbers)*100
    print(number, "is", str(numbers) +"% of", result)
    done = input("Are you done ma'am? ").lower()
    if done == "yes":
        print("Okay have a wonderful day")
        break
    if done == "no":
        continue
