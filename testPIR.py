import unittest
from pir import PIR

class TestIntelligence(unittest.TestCase):
    def setUp(self):
        self.pir = PIR(ryne_smith)
        self.pir.enemy = "Harkonnen"
        self.pir.target = "Base"
        self.req_string = "Where will the Harkonnens establish a military base?"

    def test_add_owner(self):
        self.pir.add_owner({samantha_smith, })
        self.assertIn(samantha_smith, self.pir.owners)

    def test_remove_owner(self):
        self.pir.remove_owner(samantha_smith)
        self.assertNotIn(samantha_smith, self.pir.owners)

if __name__ == '__main__':
    unittest.main()
