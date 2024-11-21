weight=float(input("Enter the weight in kg:"))
height=float(input("Enter the height in meters:"))

BMI=weight/height**2
if BMI<18.2:
    print("Under weight")
elif bmi < 25 :
    print("Healty weight")
else:
    print ("over weight")
