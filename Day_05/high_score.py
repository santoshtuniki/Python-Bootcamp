# 78 65 89 86 55 91 64 89
student_scores = input().split()

max = 0
for score in student_scores:
    if max < score:
        max = score
else:
    print(f"The highest score in the class is: {max}")

# We have max() & min() shortcuts in python