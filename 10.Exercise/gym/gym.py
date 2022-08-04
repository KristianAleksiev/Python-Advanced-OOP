class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, new_customer):
        if new_customer in self.customers:
            return
        self.customers.append(new_customer)

    def add_trainer(self, new_trainer):
        if new_trainer in self.trainers:
            return
        self.trainers.append(new_trainer)

    def add_equipment(self, new_equipment):
        if new_equipment in self.equipment:
            return
        self.equipment.append(new_equipment)

    def add_plan(self, new_plan):
        if new_plan in self.plans:
            return
        self.plans.append(new_plan)

    def add_subscription(self, new_sub):
        if new_sub in self.subscriptions:
            return
        self.subscriptions.append(new_sub)

    def subscription_info(self, sub_id):
        subscription = self.__find_by_id(self.subscriptions, sub_id)
        customer = self.__find_by_id(self.customers, subscription.customer_id)
        trainer = self.__find_by_id(self.trainers, subscription.trainer_id)
        plan = self.__find_by_id(self.plans, subscription.exercise_id)
        equipment = self.__find_by_id(self.equipment, plan.equipment_id)

        return repr(subscription) + "\n" + \
               repr(customer) + "\n" + \
               repr(trainer) + "\n" + \
               repr(equipment) + "\n" + \
               repr(plan)

    def __find_by_id(self, entities, id):
        for entity in entities:
            if entity.id == id:
                return entity
