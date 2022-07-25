import unittest
from priority_intelligence_requirement import PriorityIntelligenceRequirement

class TestIntelligence(unittest.TestCase):
    def setUp(self):
        self.pir = PriorityIntelligenceRequirement("Ryne Smith")
        self.pir.enemy = "Harkonnen"
        self.pir.target = "Base"
        #self.requirement_string = "Where will the Harkonnens establish a new military base?"

    def test_add_owner(self):
        self.pir.add_owner({"Samantha Smith", "Paul Atreides"})
        self.assertIn("Samantha Smith", self.pir.owners)

    def test_remove_owner(self):
        self.pir.remove_owner("Samantha Smith")
        self.pir.remove_owner("Ryne Smith")
        self.assertNotIn("Samantha Smith", self.pir.owners)
        self.assertIn(self.pir.author, self.pir.owners, "The PIR's author should not be removed from the set of owners!")

if __name__ == '__main__':
    unittest.main()
