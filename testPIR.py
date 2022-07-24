import unittest
from priority_intelligence_requirement import PriorityIntelligenceRequirement

class TestIntelligence(unittest.TestCase):
    def test_PIR_creation(self):
        author = "Ryne Smith"
        enemy = "Harkonnen"
        target = "new base"
        new_PIR = PriorityIntelligenceRequirement(author)
        new_PIR.enemy = enemy
        new_PIR.target = target
        self.assertEqual(author, new_PIR.author)
        self.assertEqual(enemy, new_PIR.enemy)
        self.assertEqual(target, new_PIR.target)

    def test_add_owner(self):
        author = "Ryne Smith"
        enemy = "Harkonnen"
        target = "new base"
        new_PIR = PriorityIntelligenceRequirement(author)
        new_PIR.enemy = enemy
        new_PIR.target = target
        new_PIR.add_owner({"Samantha Smith", "Paul Atreides"})
        self.assertIn("Samantha Smith", new_PIR.owners)

    def test_remove_owner(self):
        author = "Ryne Smith"
        enemy = "Harkonnen"
        target = "new base"
        new_PIR = PriorityIntelligenceRequirement(author)
        new_PIR.enemy = enemy
        new_PIR.target = target
        new_PIR.add_owner({"Samantha Smith", "Paul Atreides"})
        new_PIR.remove_owner("Samantha Smith")
        new_PIR.remove_owner("Ryne Smith")
        self.assertNotIn("Samantha Smith", new_PIR.owners)
        self.assertIn(new_PIR.author, new_PIR.owners, "The PIR's author should not be removed from the set of owners!")

if __name__ == '__main__':
    unittest.main()
