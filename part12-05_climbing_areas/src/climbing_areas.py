class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"


class ClimbingArea:
    def __init__(self, name: str):
        self.name = name
        self.__routes = []

    def add_route(self, route: ClimbingRoute):
        self.__routes.append(route)

    def routes(self):
        return len(self.__routes)

    def hardest_route(self):
        def by_difficulty(route):
            return route.grade

        routes_in_order = sorted(self.__routes, key=by_difficulty)
        # last route
        return routes_in_order[-1]

    def __str__(self):
        hardest_route = self.hardest_route()
        return f"{self.name} {self.routes()} routes, hardest {hardest_route.grade}"


def sort_by_number_of_routes(grawr):
    def amount_of_routes(x: ClimbingArea):
        return x.routes()

    return sorted(grawr, key=amount_of_routes)


def sort_by_most_difficult(areas):
    def most_difficult_grade(area: ClimbingArea):
        grades_order = ['4', '4+', '5', '5+', '6A', '6A+', '6B', '6B+', '6C', '6C+', '7A', '7A+', '7B', '7B+', '7C',
                        '7C+', '8A', '8A+', '8B', '8B+', '8C', '8C+']
        hardest_route = area.hardest_route()
        return grades_order.index(hardest_route.grade)

    return sorted(areas, key=most_difficult_grade, reverse=True)
