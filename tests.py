import unittest
import tests


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(tests.check_facebook(), True)
        self.assertEqual(tests.check_gmail(), True)
        self.assertEqual(tests.check_hotmail(), True)
        self.assertEqual(tests.check_instagram(), True)
        self.assertEqual(tests.check_linkedin(), True)
        self.assertEqual(tests.check_twitter(), True)
        self.assertEqual(tests.check_vk(), True)
        self.assertEqual(tests.check_yahoo(), True)


if __name__ == '__main__':
    unittest.main()