# Example input = 78 65 89 86 55 91 64 89
student_scores=input("Enter the list of markls obtained by students").split()
for n in range(0,len(student_scores)):
    student_scores[n]=int(student_scores[n])
print(student_scores)

highest_score=0
for score in student_scores:
    if(score>highest_score):
        highest_score=score

print(f"The highest score in the class is: {highest_score}")