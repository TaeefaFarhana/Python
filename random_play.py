import random as rd
x=int(input("Enter a number : "))
y=rd.randint(1,11)
if x==y:
    print("Your number is matched!")
else:
    print("Try again.")
    
print(f"\n Acctual random number was : {y}")
print("\nWhere your answer is : ",x)

str_name=["Jubayer","Piyas","Noman","Jahid","Foysal"]
print("Computer will choose randomly who is a good trainer : ",rd.choice(str_name))
