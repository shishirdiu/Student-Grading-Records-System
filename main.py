name = input("Enter students name:")
marks = []
print("Enter marks for 5 students:")
for i in range(1,6):
    m = float(input(f"subjects {i}"))
    marks.append(m)
total_marks = sum(marks)
average = total_marks / 5
if average >= 80:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "F"
student_record = {
    "Name": name,
    "Marks": marks,
    "Average": average,
    "Grade": grade
}
print("\n *** Student Record ***")
print("Name:", student_record["Name"])
print("Average Marks:", student_record["Average"])
print("Final Grade:", student_record["Grade"])