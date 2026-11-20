def convert_temp(value, to="F"):
    to = to.upper()
    if to == "F":
        return value * 9 / 5 + 32
    elif to == "C":
        return (value - 32) * 5 / 9
    else:
        raise ValueError("unit must be 'F' or 'C'")


print(convert_temp(100))  # 212.0
print(convert_temp(212, to="C"))  # 100.0
print(convert_temp(0, "f"))  # 32.0
