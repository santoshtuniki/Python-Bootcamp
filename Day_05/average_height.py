# 123 156 178 183 192
student_heights = input().split()

len = 0
sum = 0
for height in student_heights:
    len += 1
    sum += int(height)

print(f"total height = {sum}")
print(f"number of students = {len}")
print(f"average height = {round(sum / len)}")

# We have sum() & len() shorcuts in python