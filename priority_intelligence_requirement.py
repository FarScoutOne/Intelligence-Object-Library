class PriorityIntelligenceRequirement:
    """Defines a PIR by author"""

    def __init__(self, author: str, enemy: str = None, target: str = None):
        self.author = author
        self.enemy = enemy
        self.target = target
        self.owners = {author}

    def add_owner(self, names: set) -> set:
        """This method assigns another owner to the PIR by name"""
        self.owners.update(names)
        return self.owners

    def remove_owner(self, name: str) -> set:
        """This method removes a current owner from the PIR by name"""
        if name in self.owners:
            self.owners.remove(name)
        return self.owners
