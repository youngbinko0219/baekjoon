students = [i for i in range(1,31)]
for _ in range(28):
    num = int(input())
    if num in students:
        students.pop(students.index(num))
        
min = students[0]
for num in students:
    if num<min:
        min=num
        
max = students[0]
for num in students:
    if num>max:
        max=num
        
print(min)
print(max)