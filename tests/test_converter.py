import unittest

from converter import Converter

class TestConverter(unittest.TestCase):
    def test_converter_x_equal_to_100_7(self):
        self.assertEqual(Converter.do(100.7), 1000)
    def test_converter_x_greater_than_100_7(self):
        self.assertEqual(Converter.do(150.0), 1000)
    def test_converter_x_equal_to_100_6(self):
        self.assertEqual(Converter.do(100.6), 100)
    def test_converter_x_between_0_and_100_7(self):
        self.assertEqual(Converter.do(65.7), 65)
    def test_converter_x_equal_to_0(self):
        with self.assertRaises(ValueError):
            Converter.do(0.0)
    def test_converter_x_between_negative_30_4_and_0(self):
        self.assertEqual(Converter.do(-10.5), -15)
    def test_converter_x_less_than_negative_30_4(self):
        self.assertEqual(Converter.do(-50.0), -2000)
    def test_converter_just_above_zero(self):
        self.assertEqual(Converter.do(0.1), 0) 
    def test_converter_just_below_zero(self):
        self.assertEqual(Converter.do(-0.1), -5)
    def test_converter_x_equal_to_negative_30_4(self):
        self.assertEqual(Converter.do(-30.4), -35)
    def test_converter_x_equal_to_negative_30_5(self):
        self.assertEqual(Converter.do(-30.5), -2000)


