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


if __name__ == '__main__':
    unittest.main()
