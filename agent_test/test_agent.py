import unittest
from langchain.agents.agent import BaseSingleActionAgent


class TestBaseSingleActionAgent(unittest.TestCase):
    def setUp(self):
        self.agent = BaseSingleActionAgent()

    def test_return_values(self):
        self.assertEqual(self.agent.return_values, ['output'])

    def test_get_allowed_tools(self):
        self.assertIsNone(self.agent.get_allowed_tools())


if __name__ == '__main__':
    unittest.main()

    