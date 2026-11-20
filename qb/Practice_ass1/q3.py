total = 0                      # running total
high = marks[0]                # assume first mark is highest
low = marks[0]                 # assume first mark is lowest
i = 0                          # index for while loop
while i < len(marks):          # run until all marks are seen
    total += marks[i]          # add this mark
    if marks[i] > high:        # found a bigger mark?
        high = marks[i]
    if marks[i] < low:         # found a smaller mark?
        low = marks[i]
    i += 1                     # IMPORTANT: move to next, else infinite loop
avg = total / len(marks)       # true division gives float
print(total, round(avg, 2), high, low)