n = int(input("Enter a three-digit number: "))

d1 = n // 100          # hundreds digit
d2 = n // 10 % 10      # tens digit
d3 = n % 10            # ones digit

print("Sum of digits:", d1 + d2 + d3)
print("Reversed     :", d3 * 100 + d2 * 10 + d1)