
temp = round(eval(input("Enter a temperature in celsius: ")),2)
if temp == -273.15:
    print("Wow, you are at absolute zero!")
elif -273.15< temp < 0:
    print("the temperature is below freezing")
elif temp == 0:
    print("the temperature is at freezing point")
elif 0< temp < 100:
    print("the temperature is in normal range")
elif temp == 100:
    print("the temperature is at boiling point")
elif temp > 100:
    print("The temperature is above boiling point")
else:
    print("Invalid: Temperature cannot be below absolute zero")