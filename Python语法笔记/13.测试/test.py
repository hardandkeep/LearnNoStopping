import unittest
from example import get_formatted_name
from example import gain_full_name


class NameTestCase(unittest.TestCase):
    def test_gain_format_name(self):
        """测试能否正确处理li xue这样的名字"""
        formatted_name = get_formatted_name("li", "xue")
        self.assertEqual(formatted_name, "Li Xue")

    def test_gain_full_name(self):
        """测试能否正确处理li xue xue这样的名字"""
        full_name = gain_full_name("li", "xue", "xue")
        self.assertEqual(full_name, "Li Xue Xue")


unittest.main()
