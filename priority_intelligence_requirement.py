class PriorityIntelligenceRequirement:
    """Defines a PIR by author"""

    def __init__(self, author: str, enemy: str = None, target: str = None):
        self.author = author
        self.enemy = enemy
        self.target = target
        self.owners = [author]

    def assign_owner(self, name: str) -> list:
        """This method assigns another owner to the PIR by name"""
        self.owners.append(name)
        return self.owners

    def remove_owner(self, name: str) -> list:
        """This method removes a current owner from the PIR by name"""
        if name in self.owners:
            self.owners.remove(name)
        return self.owners
