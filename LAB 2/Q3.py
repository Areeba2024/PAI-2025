students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 90),
    ("Emy", 65)
]

n = len(students)
for i in range(n):
    for j in range(0, n-i-1):
        if students[j][1] < students[j+1][1]:
            students[j], students[j+1] = students[j+1], students[j]

print(students)
print("Top 3 Students:")
for i in range(3):
    print(students[i][0], ":", students[i][1])
