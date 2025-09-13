numbers = (0, 34, 5, 6, 75, 86, 89)
smallestSum = numbers[0] + numbers[1]
index1 = 0
index2 = 0

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):  
        if abs(numbers[i] + numbers[j]) < abs(smallestSum):
            smallestSum = numbers[i] + numbers[j]
            index1 = i
            index2 = j

print(numbers[index1], numbers[index2])
print("Sum closest to zero:", smallestSum)
