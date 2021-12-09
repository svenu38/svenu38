name=input("enter you name :")
age=int(input('how old are you , {0} '.format(name)))
print(age)
if age >18 :
    print("you are enough to vote{0}  ".format(name))
elif age < 18:
    print("please come back in {0} years ".format(18-age))
else:
    print("you are elegeble to vote")


