#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == "__main__":
    students = []


    def stud_report(stud_details):
        for name,grade in stud_details:
           # print(name)
           # print(grade)
            students.append([name, grade])
            print(students)

            # Get the second lowest grade
        grades = sorted(set([grade for name, grade in students]))
        second_lowest_grade = grades[1]

        # Get the names of students with the second lowest grade
        second_lowest_students = [name for name, grade in students if grade == second_lowest_grade]
        second_lowest_students.sort()

        for student in second_lowest_students:
            return student

    stud_details = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    print(stud_report(stud_details))