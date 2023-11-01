import unittest

from ex10_dict import roman2int as dictCase
from ex10_index import roman2int as indexCase
from ex10_zip import roman2int as zipCase

class TestRomanToArabic(unittest.TestCase):
    def test_method1(self):
        test_cases = [
            ("I", 1),
            ("IV", 4),
            ("IX", 9),
            ("XII", 12),
            ("XXIV", 24),
            ("XC", 90),
            ("CXLII", 142),
            ("CD", 400),
            ("DCCCXC", 890),
            ("MCMXCIV", 1994),
            ("MMMCMXCIV", 3994)
        ]
        for roman, expected_arabic in test_cases:
            result = dictCase(roman)
            self.assertEqual(result, expected_arabic)

    def test_method2(self):
        test_cases = [
            ("I", 1),
            ("IV", 4),
            ("IX", 9),
            ("XII", 12),
            ("XXIV", 24),
            ("XC", 90),
            ("CXLII", 142),
            ("CD", 400),
            ("DCCCXC", 890),
            ("MCMXCIV", 1994),
            ("MMMCMXCIV", 3994)
        ]
        for roman, expected_arabic in test_cases:
            result = indexCase(roman)
            self.assertEqual(result, expected_arabic)

    def test_method3(self):
        test_cases = [
            ("I", 1),
            ("IV", 4),
            ("IX", 9),
            ("XII", 12),
            ("XXIV", 24),
            ("XC", 90),
            ("CXLII", 142),
            ("CD", 400),
            ("DCCCXC", 890),
            ("MCMXCIV", 1994),
            ("MMMCMXCIV", 3994)
        ]
        for roman, expected_arabic in test_cases:
            result = zipCase(roman)
            self.assertEqual(result, expected_arabic)

if __name__ == "__main__":
    unittest.main()
