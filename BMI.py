#taking weight input from user
Weight = int(input('Enter your weight in Kilograms; '))
# Assigning the variable to the weight 
a = Weight
print(f'Weight: ', a)

# Taking height as input from the user 
Height = float(input(f"Enter your height in meters; "))
# Assigning the variable to the Height
b = Height

# printing the height to avoid error 
print(f"Height: ", b)
# using the formula 
BMI = a/b

print(f"Body Mass Index (BMI): ", BMI)
# USING THE IF CONDITION TO DETERMINE WHEATHER THE BME LIES UNDERWEIGHT OR OVERWEIGHT 
if BMI < 18.5:
    print(f"Underweight you need to eat muc stuff ")
elif 18.5 <= BMI <25:
    print(f"Normal weight, i really dont know what to do there")
elif 25 <= BMI <30:
    print(f"Overweight, start doing exersize every day untili you decrease your weight")
else:
    print(f'Obessse')
    
