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


orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Eric", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)


for order in orders.all_orders():
    print(order)

print()

for programmer in orders.programmers():
    print(programmer)
