# Repository Name: CreateFunction_3NIMBelakang

def convert_temperature(value, unit):
    if unit == 'C':
        return (value * 9/5) + 32
    elif unit == 'F':
        return (value - 32) * 5/9
        
calculate_circle_area = lambda r: 3.14 * (r ** 2)



print("temperature in F", convert_temperature(25, 'C'))
print("calculate circle", calculate_circle_area(7))
