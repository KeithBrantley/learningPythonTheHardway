my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
inches_to_centimeters = round(my_height * 2.54)
pounds_to_kilograms = round(my_weight / 2.205)

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

# Inches to Centimiters
print(f"My height converted to centimeters is {inches_to_centimeters} centimeters.")

# pounds to pounds_to_kilograms
print(f"My weight converted to kilograms is {pounds_to_kilograms} kilograms.")
