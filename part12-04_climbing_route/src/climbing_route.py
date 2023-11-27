class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"


# Write your solution here:

def sort_by_length(routes: list):
    def length(rawr: ClimbingRoute):
        return rawr.length

    return sorted(routes, key=length, reverse=True)


def sort_by_difficulty(routes: list):
    def difficulty(route: ClimbingRoute):
        hello = route.grade, route.length
        return hello

    return sorted(routes, key=difficulty, reverse=True)
