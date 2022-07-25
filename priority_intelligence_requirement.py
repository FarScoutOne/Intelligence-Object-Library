class PriorityIntelligenceRequirement:
    """Defines a PIR by author"""

    def __init__(self, author: str, enemy: str = None, target: str = None):
        self.author = author
        self.enemy = enemy
        self.target = target
        self.req_string = ""
        self.owners = {author}

    def add_owner(self, names: set) -> set:
        """This method assigns another owner to the PIR by name"""
        self.owners.update(names)
        return self.owners

    def remove_owner(self, name: str) -> set:
        """This method removes a current owner from the PIR by name"""
        if name in self.owners:
            if name == self.author:
                while True:
                    choice = input("Are you sure you want to remove the PIR's author from the list of owners? (Y/n)\n")
                    if choice.upper() == "Y":
                        break
                    elif choice.upper() == "N":
                        print("Action aborted by user.")
                        return self.owners
                    else:
                        print("I'm sorry. I did not understand.")
            self.owners.remove(name)
            print(f"{name} has been removed from the list of owners for this PIR.")
        else:
            print(f"{name} was not in the list of owners for this PIR.")
        return self.owners
