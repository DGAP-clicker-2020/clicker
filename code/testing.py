import unittest
from auxiliary_functions import to_fixed, calculate_hp

start_hp = 20


class TestToFixed(unittest.TestCase):

    def test_simple_positive(self):
        for param, result in [
            (2, '2'),
            (3.4, '3'),
            (7.5, '8'),
            (7845513.789513, '7845514'),
            (123456.97752, '123457'),
            (123.0000000000001, '123'),
            (239.99999990, '240'),
            (897.5789, '898'),
        ]:
            self.assertEqual(result, to_fixed(param))

    def test_simple_negative(self):
        for param, result in [
            (-2, '-2'),
            (-78.8, '-79'),
            (-53.2, '-53'),
            (-78.5, '-78'),
            (-101.7, '-102'),
            (-487.44887, '-487'),
            (-1237.889, '-1238'),
            (-789.99, '-790'),
            (-356.2, '-356'),
        ]:
            self.assertEqual(result, to_fixed(param))

    def test_complicated_positive(self):
        for param, num, result in [
            (2358.7931, 1, '2358.8'),
            (0.123, 2, '0.12'),
            (78.789112, 4, '78.7891'),
            (178, 3, '178.000'),
            (789.6, 4, '789.6000'),
            (153.9874626, 6, '153.987463'),
            (789.1212121212, 11, '789.12121212120'),
        ]:
            self.assertEqual(result, to_fixed(param, num))

    def test_complicated_negative(self):
        for param, num, result in [
            (-102.12367, 3, '-102.124'),
            (-567, 3, '-567.000'),
            (-236.000009, 2, '-236.00'),
            (-789.9999, 3, '-790.000'),
            (-236.98741, 1, '-237.0'),
            (-0.01, 1, '-0.0'),
            (-8.2379, 3, '-8.238'),
        ]:
            self.assertEqual(result, to_fixed(param, num))

    def test_wrong_input_type(self):
        with self.assertRaises(ValueError):
            to_fixed('Ignat', 7)
            to_fixed(0, '7')
            to_fixed('Hello', 'world')
            to_fixed(None, 3)
            to_fixed(7, [78, 25, 69])
            to_fixed({8: 1, 7: 9, 'day': 'monday'}, 'foo'.upper())
            to_fixed((1, 2, 3), 9)

    def test_wrong_input_parameters(self):
        with self.assertRaises(TypeError):
            to_fixed(1, 2, 3)
            to_fixed(None, 78, 23, 56)
            to_fixed('', '', '', '', num_obj=7, digits=9)
            to_fixed(num_obj=7, digits=2, status=True)


class TestCalculateHP(unittest.TestCase):

    def test_simple(self):
        for param, result in [
            (0, 20),
            (1, 21),
            (2, 22.82842),
            (3, 25.19615),
            (10, 51.6228),
            (20, 109.4427),
        ]:
            calculated_result = calculate_hp(param, start_hp)
            difference = abs(calculated_result - result)
            self.assertTrue(difference < 0.0001,
                            'Test failed on parameter: ' + str(param) + '. Difference was: ' + str(difference))

    def test_complicated(self):
        for param, result in [
            (100, 1020),
            (10000, 1000020),
            (100000, 31622796.6),
            (5697.6, 430088.79),
            (784.111148, 21976.668),
            (567.00001, 13521.269),
        ]:
            calculated_result = calculate_hp(param, start_hp)
            difference = abs(calculated_result - result)
            self.assertTrue(difference < 0.01,
                            'Test failed on parameter: ' + str(param) + '. Difference was: ' + str(difference))

    def test_wrong_input(self):
        with self.assertRaises((ValueError, TypeError)):
            calculate_hp('Vasya', 'Petya')
            calculate_hp(['Vasya', 'Gena'], (1, 2, 3))
            calculate_hp('', '', '', 7)
            calculate_hp(1_2_3, '789/')
            calculate_hp('Can I work?', 'No')
            calculate_hp(-2, 20)


if __name__ == '__main__':
    unittest.main()
