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


class Application:
    def __init__(self):
        self.orders = OrderBook()

    def instructions(self):
        # Defining multiline string is possible with triple apostrophes
        instructions_str = """
commands:
0 exit
1 add order
2 list finished tasks
3 list unfinished tasks
4 mark task as finished
5 programmers
6 status of programmer"""
        print(instructions_str)

    def add(self):
        description = input("description: ")
        programmer_and_estimate = input("programmer and workload estimate: ")
        try:
            programmer = programmer_and_estimate.split(' ')[0]
            workload = int(programmer_and_estimate.split(' ')[1])
            self.orders.add_order(description, programmer, workload)
            print("added!")
        except:
            print("erroneous input")

    def unfinished(self):
        for task in self.orders.unfinished_orders():
            print(task)

    def finished(self):
        finished_orders = self.orders.finished_orders()
        if len(finished_orders) == 0:
            print("no finished tasks")
            return

        for task in finished_orders:
            print(task)

    def programmers(self):
        for programmer in self.orders.programmers():
            print(programmer)

    def mark_finished(self):
        try:
            order_id = int(input("id: "))
            self.orders.mark_finished(order_id)
            print("marked as finished")
        except:
            print("erroneous input")

    def programmers_status(self):
        programmer = input("programmer: ")
        if not programmer in self.orders.programmers():
            print("erroneous input")
            return

        status = self.orders.status_of_programmer(programmer)
        print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")

    def run(self):
        self.instructions()
        while True:
            command = input("command: ")
            if command == "0":
                return
            elif command == "1":
                self.add()
            elif command == "2":
                self.finished()
            elif command == "3":
                self.unfinished()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.programmers_status()
            print()


Application().run()
