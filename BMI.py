def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2

def lb_to_kg(lb):
    return lb * 0.45359237

def ft_to_m(ft, inch = 0.0):
    return (ft * 0.3048) + (inch * 2.54 / 100)


units = int(input("BMI calculator, 1 for metric, 2 for imperial, 0 to exit program: "))

while units != 0:
    if units == 1:
        weight = float(input("State your weight in kg: "))
        height = float(input("State your height in m: "))
        print("Your BMI is:", bmi(weight, height))
        units = int(input("BMI calculator, 1 for metric, 2 for imperial, 0 to exit program: "))

    else:
        lb = float(input("State your weight in lb: "))
        ft = float(input("State your height in ft: "))
        inch = float(input("and your height in in: "))
        print("Your BMI is:", bmi(weight = lb_to_kg(lb), height = ft_to_m(ft, inch)))
        units = int(input("BMI calculator, 1 for metric, 2 for imperial, 0 to exit program: "))
