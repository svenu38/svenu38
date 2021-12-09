a=12
b=3
print(a+b)   # addition operation
print(a-b)   # subtraction operation
print(a*b)   #multiplication operation
print(a/b)   # floting point division operation
print(a//b)  # interger division operation
print(a%b)   # remender operation

for i in range(1,a//b):  # range operation its should be contains integer values
    print(i)

print("operation concept finished ")
print("operation precedence ")
print("a + b / 3 - 4 * 12")
print(a + b / 3 - 4 * 12) # / and * having first precedence then + and - but operation always starts from right of the expression
print(a + (b/3) - (4*12)) # bracess having higher precedence then the sign

print("(((a+b)/3)-4)*12") # inner bracess first and outer bracess

print((((a+b)/3)-4)*12) # bracket, order,division , multiplication, addition, subraction


c=a+b
d=c/3
e=d-4
print(e*12)

print( "a / (b * a ) / b" )
print( a / (b * a ) / b)
c= (b*a)
d=a / c
print(d / b)

