'''

Conversational temperature conversion tool
by vagnes

'''

import re

# choose input unit

print("\n")
in_unit = input("What input unit do you want? (Celsius / Kelvin / Farenheit)\n> ")
print("\n")

if re.search('[c, C]', in_unit):
    print("You've choosen Celsius as your unit.")
    in_unit = 'degcel'
elif re.search('[k, K]', in_unit):
    print("You've chosen Kelvin as your unit.")
    in_unit = 'kelvin'
else:
    print("You've chosen Fahrenheit as your unit.")
    in_unit = 'degfah'

print("\n")

# choose output unit

out_unit = input("What output unit do you want? (Celsius / Kelvin / Farenheit)\n> ")

print("\n")

if re.search('[c, C]', out_unit):
    print("You've choosen Celsius as your unit.")
    out_unit = 'degcel'
elif re.search('[k, K]', out_unit):
    print("You've chosen Kelvin as your unit.")
    out_unit = 'kelvin'
else:
    print("You've chosen Fahrenheit as your unit.")
    out_unit = 'degfah'

print("\n")

# choose input value

try:
    if in_unit == 'degcel':
        in_val = float(input("How many degrees Celsius do you want to convert?\n> "))
        print(type(in_val))
    elif in_unit == 'kelvin':
        in_val = float(input("How many Kelvin do you want to convert?"))
    else:
        in_val = float(input("How many degrees Fahrenheit do you want to convert?"))
    if not in_val:
        raise ValueError('empty string')
    print("\n")
except ValueError:
    in_val = 50
    print("\n")
    print("Let's try with 05, m'kay?\n")

# do the conversion

if in_unit == 'degcel':
    if out_unit == 'degcel':
        print(f"That is the same value: {in_val} degrees Celsius.")
    elif out_unit == 'kelvin':
        out_val = in_val + 273.15
        round(in_val, 2), round(out_val, 2)
        print(f"{in_val} degrees Celsius equates to {out_val} Kelvin.")
    else:
        out_val = (5 / 9) * (in_val - 32)
        round(in_val, 2), round(out_val, 2)
        print(f"{in_val} degrees Celsius equates to {out_val} degrees Fahrenheit.")
elif in_unit == 'kelvin':
    if out_unit == 'degcel':
        out_val = in_val - 273.15
        round(in_val, 2), round(out_val, 2)
        print(f"{in_val} Kelvin equates to {out_val} degrees Celsius.")
    elif out_unit == 'kelvin':
        print(f"That is the same value: {in_val}")
    else:
        out_val = ((in_val - 32) * 5 / 9) - 273.15
        round(in_val, 2), round(out_val, 2)
        print(f"{in_val} Kelvin equates to {out_val} degrees Fahrenheit.")
else:
    if out_unit == 'degcel':
        out_val = (in_val * (9 / 5)) + 32
        round(in_val, 2), round(out_val, 2)
        print(f"{in_unit} degrees Fahrenheit equates to {out_unit} degrees Celsius.")
    elif out_unit == 'kelvin':
        out_val = ((in_val - 32) * 5 / 9) + 273.15
        round(in_val, 2), round(out_val, 2)
        print(f"{in_val} degrees Fahrenheit equates to {out_val} Kelvin.")
    else:
        print(f"That is the same value: {in_val} degrees Fahrenheit.")

print("\n")
