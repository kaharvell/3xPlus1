# 3x+1

max = 0
result = []
frequency = {}
summation = []

for i in range(10000):
    occurrence = []
    num = i

    while num not in occurrence:
        occurrence.append(num)

        if num % 2 == 0:
            num = num>>1
        else:
            num = (num<<1) + num + 1

    count = len(occurrence)

    if count > max:
        max = count
        result = occurrence

        frequency[result[0]] = count
        summation.append(sum(result))

    print(i)

print("{0} has a count of {1}".format(result[0], max))
print(result)
print(frequency)
print(summation)