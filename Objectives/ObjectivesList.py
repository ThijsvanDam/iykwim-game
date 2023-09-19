
from Objectives import Objective


class ObjectivesList:
    def __init__(self, title, descriptions):
        self.objectives = []

        for description in descriptions:
            objective = Objective(description)
            self.objectives.append(objective)
        
        self.title = title

    def show_objectives(self):
        for objective in self.objectives:
            objective.show_objective()

    def get_objectives(self):
        return self.objectives

    def add_objective(self, description):
        self.objectives.append(Objective(description))

    def remove_objective(self, description):
        for objective in self.objectives:
            if objective.get_objective() == description:
                self.objectives.remove(objective)
                return
