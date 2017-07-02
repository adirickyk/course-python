#create new exception
try:
    Value = int(input("Type a number between 1 and 10 : "))
except ValueError:
    print("You must type a number between 1 and 10")
else:
    if(Value > 0) and (Value <= 10):
        print("You typed value : ", Value)
    else:
        print("The value type is incorrect !")
