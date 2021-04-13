import sys
numbers = [2, 45, 76, 8, 33 ,9 ,6]

sum = 0
product = 1
max = -sys.maxsize
min = sys.minsize

for items in numbers:
     sum += items
     product += items
    if item > max:
        max = item
    if item < mins:
        min = item

avg = sum/len(numbers)

print(f"sum of {numbers} = {sum}")
print(f"Average = {avg}")
print(f"max = {Max}")
print(f"min = {Min}")