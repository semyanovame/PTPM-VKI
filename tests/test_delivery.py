import unittest
from src.Delivery import calculate_delivery_cost

class TestDelivery(unittest.TestCase):
    def test_express_delivery_is_more_expensive(self):
        cost_normal, date_normal = calculate_delivery_cost(weight=10.0, distance=1000, package_type="обычный", is_express=False)
        cost_express, date_express = calculate_delivery_cost(weight=10.0, distance=1000, package_type="обычный", is_express=True)

        self.assertGreater(cost_express, cost_normal)
        self.assertLess(date_express, date_normal)
    def test_invalid_weight_returns_error(self):
        cost, date = calculate_delivery_cost(weight=60.0, distance=1000, package_type="обычный", is_express=False)
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")
    def test_invalid_distance_returns_error(self):
        cost, date = calculate_delivery_cost(weight=10.0, distance=6000, package_type="обычный", is_express=False)
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")
    def test_invalid_package_type_returns_error(self):
        cost, date = calculate_delivery_cost(weight=10.0, distance=1000, package_type="неизвестный", is_express=False)
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")
    def test_heavy_package_increases_cost(self):
        cost_light, _ = calculate_delivery_cost(weight=4.0, distance=1000, package_type="обычный", is_express=False)
        cost_heavy, _ = calculate_delivery_cost(weight=25.0, distance=1000, package_type="обычный", is_express=False)
        self.assertGreater(cost_heavy, cost_light)
    def test_fragile_package_increases_cost(self):
        cost_normal, _ = calculate_delivery_cost(weight=10.0, distance=1000, package_type="обычный", is_express=False)
        cost_fragile, _ = calculate_delivery_cost(weight=10.0, distance=1000, package_type="хрупкий", is_express=False)
        self.assertGreater(cost_fragile, cost_normal)
    def test_dangerous_package_increases_cost(self):
        cost_normal, _ = calculate_delivery_cost(weight=10.0, distance=1000, package_type="обычный", is_express=False)
        cost_dangerous, _ = calculate_delivery_cost(weight=10.0, distance=1000, package_type="опасный", is_express=False)
        self.assertGreater(cost_dangerous, cost_normal)
    def test_express_delivery_reduces_time(self):
        _, date_normal = calculate_delivery_cost(weight=10.0, distance=1000, package_type="обычный", is_express=False)
        _, date_express = calculate_delivery_cost(weight=10.0, distance=1000, package_type="обычный", is_express=True)
        self.assertLess(date_express, date_normal)
    def test_minimum_delivery_time_is_one_day(self):
        _, date = calculate_delivery_cost(weight=10.0, distance=100, package_type="обычный", is_express=False)
        self.assertEqual(date, "2026-09-04")  
    def test_express_delivery_minimum_time_is_one_day(self):
        _, date = calculate_delivery_cost(weight=10.0, distance=100, package_type="обычный", is_express=True)
        self.assertEqual(date, "2026-09-04") 
    def test_maximum_delivery_time_for_long_distance(self):
        _, date = calculate_delivery_cost(weight=10.0, distance=5000, package_type="обычный", is_express=False)
        self.assertEqual(date, "2026-09-13")
    def test_express_delivery_maximum_time_for_long_distance(self):
        _, date = calculate_delivery_cost(weight=10.0, distance=5000, package_type="обычный", is_express=True)
        self.assertEqual(date, "2026-09-08")
if __name__ == "__main__":
    unittest.main()
