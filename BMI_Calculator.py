
Name=input("Enter your name: ")


height=float(input("Enter the Height in meters:-"))

weight=float(input("Enter the Weight in kgs:- "))


height_square=height**2
BMI_Calculated=weight/height_square

print("Calculated BMI is:-",BMI_Calculated)



print(Name,"'s BMI REPORT : \n")
if(BMI_Calculated<18.5):
    print("UNDER-WEIGHT")

if(BMI_Calculated>=18.5 and BMI_Calculated<24.9):
    print("NORMAL")

if(BMI_Calculated>=25.0 and BMI_Calculated<29.9):
    print("OVER-WEIGHT")
    

if(BMI_Calculated>=30.0 and BMI_Calculated<34.9):
    print("OBESE")
if(BMI_Calculated>=35.0 ):
    print("EXTREMELY-OBESE")