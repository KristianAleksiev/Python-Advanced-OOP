from lion import Lion
from tiger import Tiger
from cheetah import Cheetah
from keeper import Keeper
from caretaker import Caretaker
from vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.workers = []
        self.animals = []

    def add_animal(self, animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        if price > self.__budget:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):

        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_workers_salary = sum(w.salary for w in self.workers)

        if self.__budget >= total_workers_salary:
            self.__budget -= total_workers_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animal_expenses = sum(a.money_for_care for a in self.animals)

        if self.__budget >= animal_expenses:
            self.__budget -= animal_expenses
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"

        lions = [repr(animal) for animal in self.animals if isinstance(animal, Lion)]
        result += f"----- {len(lions)} Lions:\n" + "\n".join(lions) + "\n"

        tigers = [repr(animal) for animal in self.animals if isinstance(animal, Tiger)]
        result += f"----- {len(tigers)} Tigers:\n" + "\n".join(tigers) + "\n"

        cheetahs = [repr(animal) for animal in self.animals if isinstance(animal, Cheetah)]
        result += f"----- {len(cheetahs)} Cheetahs:\n" + "\n".join(cheetahs)

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = [repr(worker) for worker in self.workers if isinstance(worker, Keeper)]
        result += f"----- {len(keepers)} Keepers:\n" + "\n".join(keepers) + "\n"

        caretakers = [repr(worker) for worker in self.workers if isinstance(worker, Caretaker)]
        result += f"----- {len(caretakers)} Caretakers:\n" + "\n".join(caretakers) + "\n"

        vets = [repr(worker) for worker in self.workers if isinstance(worker, Vet)]
        result += f"----- {len(vets)} Vets:\n" + "\n".join(vets)

        return result

