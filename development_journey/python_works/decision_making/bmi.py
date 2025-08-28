


height_in_cm = int(input("enter the height :"))

weight_in_kg = int(input("enter the weight :"))

height_in_meter = height_in_cm/100

BMI = weight_in_kg / (height_in_meter**2)

BMI = round(BMI)

print("BMI :",BMI)

if BMI >= 30:

    print("obese")

elif BMI >= 25:

    print("overweight")
    
elif BMI >= 20:

    print("normal")

else:

    print("under")

