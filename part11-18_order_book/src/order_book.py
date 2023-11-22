# Write your solution here:
class Task:
    id = 1

    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False
        self.id = Task.id
        Task.id += 1

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}'


class OrderBook:
    def __init__(self):
        self.entire_list = []

    def add_order(self, description, programmer, workload):
        x = Task(description, programmer, workload)
        self.entire_list.append(x)

        pass

    def all_orders(self):
        return list(self.entire_list)

    def programmers(self):
        name_list = []
        for name in self.entire_list:
            name_list.append(name.programmer)
        return sorted(list(set(name_list)))
        pass

    def mark_finished(self, id: int):
        matching = False
        for name in self.entire_list:
            if name.id == id:
                matching = True
                name.mark_finished()
                break
        if not matching:
            raise ValueError

        pass

    def finished_orders(self):
        return [order for order in self.entire_list if order.finished]

    def unfinished_orders(self):
        return [order for order in self.entire_list if not order.finished]

    def status_of_programmer(self, programmer: str):
        all_tasks = []
        found = False
        for programmers_name in self.entire_list:
            if programmers_name.programmer == programmer:
                all_tasks.append(programmers_name)
                found = True

        if not found:
            raise ValueError

        finished = 0
        unfinished_Tasks = 0
        hours = 0
        Unfinished_hours = 0
        for i in all_tasks:
            if i.finished:
                finished += 1
                hours += i.workload
            elif not i.finished:
                unfinished_Tasks += 1
                Unfinished_hours += i.workload

        return finished, unfinished_Tasks, hours, Unfinished_hours


t = OrderBook()
t.add_order("program webstore", "Andy", 10)
t.status_of_programmer("JohnDoe")