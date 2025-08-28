


gender = input("enter gender:")

age = int(input("enter age:"))

height_in_cm = int(input("enter height:"))

weight_in_kg = int(input("enter weight:"))

activity_level = 1.2

if gender == "male":

    BMR = 10 * weight_in_kg + 6.25 * height_in_cm - 5 * age + 5

else:

    BMR = 10 * weight_in_kg + 6.25 * height_in_cm - 5 * age - 161

calories = BMR * activity_level

print(calories)




