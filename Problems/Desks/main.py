# put your python code here
first_number = int(input())
second_number = int(input())
third_number = int(input())

count = 0

count += int(first_number / 2)
if first_number % 2 == 1:
    count += 1

count += int(second_number / 2)
if second_number % 2 == 1:
    count += 1

count += int(third_number / 2)
if third_number % 2 == 1:
    count += 1

print(count)
