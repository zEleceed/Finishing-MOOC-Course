from functools import reduce


class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"


# Write your solution


def sum_of_all_credits(courses: list):
    return reduce(lambda reduced_total, score: reduced_total + score.credits, courses, 0)


def sum_of_passed_credits(courses: list):
    filtered_list = list(filter(lambda score: score.grade > 1, courses))

    return reduce(lambda reduced_total, total_grades: reduced_total + total_grades.credits, filtered_list, 0)


def average(course:list):
    filtered_list = list(filter(lambda score: score.grade > 1, course))
    return (reduce(lambda reduced_total, total_Grades: reduced_total + total_Grades.grade, filtered_list, 0))/len(filtered_list)


s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
ag = average([s1, s2, s3])
print(ag)