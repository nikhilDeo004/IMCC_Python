total=int(input("Enter Seconds : "))

minutes , seconds=divmod(total,60)
hours,minutes=divmod(minutes,60)

print(f"{hours:02}:{minutes:02}:{seconds:02}")