marks_1 = int(input("Enter marks1: "))
marks_2 = int(input("Enter marks2: "))
marks_3 = int(input("Enter marks3: "))
THRESHOLD= 35
total= marks_1+ marks_2 + marks_3
avg= total/3

print("==================")
print("---------Report--------")
print("Marks1    :"+ str(marks_1))
print("Marks2    :"+ str(marks_2))
print("Marks3    :"+ str(marks_3))
print("Total:    :" + str(total))
print("percentage: :" + str(avg))

if marks_1 > THRESHOLD and marks_2 > THRESHOLD and marks_3 > THRESHOLD
status ="passed"
