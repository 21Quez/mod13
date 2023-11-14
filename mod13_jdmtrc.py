import unittest
from datetime import datetime

class TestStockInputs(unittest.TestCase):

    def test_symbol(self):
        symbol = "ABCDEFG"
        self.assertRegex(symbol, r"^[A-Z]{1,7}$")
        
        symbol = "abc"
        self.assertNotRegex(symbol, r"^[A-Z]{1,7}$")

    def test_chart_type(self):
        chart_type = "1"
        self.assertIn(chart_type, ["1", "2"])
        
        chart_type = "3"
        self.assertNotIn(chart_type, ["1", "2"])

    def test_time_series(self):
        time_series = "2"
        self.assertIn(time_series, ["1", "2", "3", "4"])

        time_series = "5"
        self.assertNotIn(time_series, ["1", "2", "3", "4"])

    def test_start_date(self):
        start_date = "2020-01-01"
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
        except ValueError:
            self.fail("Start date is not valid YYYY-MM-DD format")
            
        start_date = "2020-01-41"
        self.assertRaises(ValueError, datetime.strptime, start_date, "%Y-%m-%d")

    def test_end_date(self):
        end_date = "2022-12-31"
        try:
            datetime.strptime(end_date, "%Y-%m-%d") 
        except ValueError:
            self.fail("End date is not valid YYYY-MM-DD format")
        
        end_date = "2022-13-31"
        self.assertRaises(ValueError, datetime.strptime, end_date, "%Y-%m-%d")

if __name__ == '__main__':
    unittest.main()