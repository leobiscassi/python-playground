"""
    @hackerrank - Nested Lists Challenge: https://www.hackerrank.com/challenges/nested-list/problem
"""
if __name__ == "__main__":
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 37.2], ['Harsh', 39]]
    unique_grades = set(dict(students).values())
    grades = list(unique_grades)
    grades.sort(reverse=True)
    second_lowest = grades[-2]

    names = []
    for name, grade in students:
        if grade == second_lowest:
            names.append(name)

    names.sort()
    for name in names:
        print(name)

