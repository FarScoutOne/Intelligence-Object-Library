import unittest
from pir import PIR
from build_users import user_dict


class TestIntelligence(unittest.TestCase):
    def setUp(self):
        self.pir = PIR(user_dict["paul_atreides"])
        self.pir.enemy = "Harkonnen"
        self.pir.target = "Base"
        self.req_string = "Where will the Harkonnens establish a military base?"

    def test_add_owner(self):
        self.pir.add_owner({user_dict["leto_atreides"], })
        self.assertIn(user_dict["leto_atreides"], self.pir.owners)

    def test_remove_owner(self):
        self.pir.remove_owner(user_dict["leto_atreides"])
        self.assertNotIn(user_dict["leto_atreides"], self.pir.owners)

if __name__ == '__main__':
    unittest.main()
