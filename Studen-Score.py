import pandas as pd

def get_student_data():
    students = pd.DataFrame(columns=["Name", "Grades"])
    num_students = int(input("How many students do you want to add? "))

    for i in range(0, num_students):
        name = input("Enter student name: ")
        while True:
          scores = input("Enter 4 grades separated by commas: ").split(",")
          if len(scores) == 4:
            break
          else:
            print("You need 4 scores, invalid")            
        scores = [float(score) for score in scores]
        avg = sum(scores) / len(scores)
        students.loc[len(students)] = [name, avg]
    return students

def print_report(students):
    for index, row in students.iterrows():
        name = row["Name"]
        avg = row["Grades"]
        if avg >= 75:
            status = "Pass"
        elif avg < 75:
            status = "Fail"
        else:
            status = "Unknown"
        print(f"{name}'s average: {round(avg, 2)}, Status: {status}")
        

students = get_student_data()
print_report(students)
students.to_excel("students.xlsx", index=False)

