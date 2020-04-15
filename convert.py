# Written in python3

def cypher(temp, scale):
    scale = scale.lower()
    
# Converts Celsius to Fahrenheit
    if scale == "f":
        temp = 9.0 / 5.0 * temp + 32
        return "%s degrees Fahrenheit"% temp
    
# Converts Fahrenheit to Celsius
    elif scale == "c":
        temp = (temp - 32)  / 9.0 * 5.0
        return "%s degrees Celsius"% temp

temp = float(input("What is the temperature to convert? "))

scale = str(input("Please enter f to convert to Fahrenheit or c to convert to Celsius (f or c): "))
 
print(cypher(temp, scale))

