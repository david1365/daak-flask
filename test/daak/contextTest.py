import unittest

from src.daak.JsonDaak import JsonDaak


class TestJsonDaak(unittest.TestCase):

    def test_toJson(self):
        ali = JsonDaak()
        ali.name = "ali"

        me = JsonDaak()
        me.name = "Onur"
        me.age = 35
        me.dog = JsonDaak()
        me.dog.name = "Apollo"
        me.tople = [1,2,3.4]
        me.dic = {"ali": 1, "mamad":2, "hasn": ali}

        oneObject = JsonDaak.fromJson(me.toJSON())
        self.assertEqual(oneObject.dic.hasn.name, "ali")


    def test_fromJson(self):
        data = '{"name": "david", "hometown": {"name": "New York", "id": 123}}'
        oneObject = JsonDaak.fromJson(data)

        if  hasattr(oneObject, 'name'):
            self.assertEqual(getattr(oneObject, 'name'), "david")

        self.assertEqual(oneObject.name, "david")
        self.assertEqual(oneObject.hometown.id, 123)


if __name__ == '__main__':
    unittest.main()