num = [12, 23, 33, 4, 5, 66, 4, 33, 22]

index = 0
large = num [0]
while index<len(num):
    if num[index] > large:
        large = num[index]

    index += 1

print('Large number I found', large)
print('Large by built-in', max(num))