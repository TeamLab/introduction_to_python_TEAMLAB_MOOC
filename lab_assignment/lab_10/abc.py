import unittest
import stock_data_crawler as sdc
import urllib
import string
import random
import os

import csv

from unittest.mock import patch
from io import StringIO


class TestStockDataCrawler(unittest.TestCase):
    def setUp(self):
        self.test_url_1 = 'http://finance.google.com/finance/historical?q=KRX:005930&startdate=2013-01-01&enddate=2015-12-30&output=csv'
        self.test_url_2 = 'http://finance.google.com/finance/historical?q=KRX:051910&startdate=2013-01-01&enddate=2015-12-30&output=csv'
        self.test_url_3 = 'http://finance.google.com/finance/historical?q=KRX:051910&startdate=2013-01-01&enddate=2014-12-30&output=csv'

        self.stock_data_1 = self.get_stock_data(self.test_url_1)
        self.stock_data_2 = self.get_stock_data(self.test_url_2)
        self.stock_data_3 = self.get_stock_data(self.test_url_3)

        self.header = self.get_header_date(self.stock_data_1)

        import datetime
        basename = "testfile_"+ self.id_generator()
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        self.temp_file_name_1 = "_".join([basename+"_1", suffix, ".csv"])
        self.temp_file_name_2 = "_".join([basename+"_2", suffix, ".csv"])
        self.temp_file_name_3 = "_".join([basename+"_3", suffix, ".csv"])


    def tearDown(self):
        if os.path.isfile(self.temp_file_name_1):
            os.remove(self.temp_file_name_1)
        if os.path.isfile(self.temp_file_name_2):
            os.remove(self.temp_file_name_2)
        if os.path.isfile(self.temp_file_name_3):
            os.remove(self.temp_file_name_3)

    def test_get_stock_data(self):
        self.assertEqual(
            sdc.get_stock_data(self.test_url_1), self.stock_data_1
        )

        self.assertEqual(
            sdc.get_stock_data(self.test_url_2), self.stock_data_2
        )

        self.assertEqual(
            sdc.get_stock_data(self.test_url_3), self.stock_data_3
        )

    def test_get_header_data(self):
        self.assertEqual(
            sdc.get_header_data(self.stock_data_1), self.header
        )

    def test_get_attribute_data(self):
        self.assertEqual(
            sdc.get_attribute_data(self.stock_data_3, self.header[1]),
            self.get_attribute_data(self.stock_data_3, self.header[1])
        )
        self.assertEqual(
            sdc.get_attribute_data(self.stock_data_2, self.header[1], 2014),
            self.get_attribute_data(self.stock_data_2, self.header[1], 2014)
        )

        self.assertEqual(
            sdc.get_attribute_data(self.stock_data_1, self.header[1], 2014, 1),
            self.get_attribute_data(self.stock_data_1, self.header[1], 2014, 1)
        )

    def test_get_average_value_of_attribute(self):
        self.assertEqual(
            sdc.get_average_value_of_attribute(self.stock_data_1, self.header[1], 2014, 1),
            self.get_average_value_of_attribute(self.stock_data_1, self.header[1], 2014, 1)
        )

        self.assertEqual(
            sdc.get_average_value_of_attribute(self.stock_data_2, self.header[2], 2014),
            self.get_average_value_of_attribute(self.stock_data_2, self.header[2], 2014)
        )

    def test_write_csv_file_by_result(self):
        sdc.write_csv_file_by_result(self.stock_data_2, self.temp_file_name_1)
        self.write_csv_file_by_result(self.stock_data_2, self.temp_file_name_2)

        f_1 = open (self.temp_file_name_1, "r", encoding="utf8")
        f_2 = open (self.temp_file_name_2, "r", encoding="utf8")

        self.assertEqual(f_1.read(), f_2.read())
        f_1.close()
        f_2.close()


    def test_separate_user_query(self):
        user_input = "SAMSUNG, 2014-12, Open, ALL"
        self.assertEqual(
            sdc.separate_user_query(user_input), self.separate_user_query(user_input)
        )
        user_input = "SAMSUNG, 2013-12, Open, ALL"
        self.assertEqual(
            sdc.separate_user_query(user_input), self.separate_user_query(user_input)
        )
        user_input = "SAMSUNG, 2012-12, Open, Mean"
        self.assertEqual(
            sdc.separate_user_query(user_input), self.separate_user_query(user_input)
        )

    def test_main(self):
        for x in range(10):
            with patch('builtins.input', side_effect=["0"]):
                with patch('sys.stdout', new=StringIO()) as fakeOutput:
                    sdc.main()
                    console = fakeOutput.getvalue().strip().split("\n")
                    self.assertIn(console[1].upper(), "GOOD BYE")

        with patch('builtins.input', side_effect=["SAMSUNG, 2013-12, Open, ALL",
                                                  "SAMSUNG, 2014-12, "+self.header[3]+", Mean",
                                                  "SAMSUNG, 2015-01, "+self.header[3]+", FILE, "+ self.temp_file_name_3,
                                                  "0"]):
            with patch('sys.stdout', new=StringIO()) as fakeOutput:
                sdc.main()
                console = fakeOutput.getvalue().strip().split("\n")

        result = self.get_attribute_data(self.stock_data_1, self.header[1], 2013, 12)
        for row in result:
            answer_result = " ".join(row)
            answer_result = answer_result.replace("\ufeff", "")
            self.assertIn(answer_result, "\n".join(console))
        result = self.get_average_value_of_attribute(self.stock_data_1, self.header[3], 2014, 12)
        self.assertIn(str(result), "\n".join(console))

        result = self.get_attribute_data(self.stock_data_1, self.header[3], 2015, 1)
        try:
            f = open(self.temp_file_name_3, "r", encoding="utf8")

            contents = f.read()
            str_result = "\n".join([ ",".join(row) for row in result])
            self.assertEqual(contents.strip(), str_result.strip())

            f.close()
        except IOError:
            f.close()


    def get_stock_data(self, url_address):
        r = urllib.request.urlopen(url_address)
        data = r.read().decode("utf8").strip()
        result = []
        data_list = data.split("\n")
        for row in data_list :
            temp = []
            for value in row.split(","):
                temp.append(value)
            result.append(temp)
        return result

    def get_header_date(self, stock_data):
        return stock_data[0]

    def get_attribute_data(self, stock_data, attribue, year=None, month=None):
        attribute_id = stock_data[0].index(attribue)
        result = []
        result.append([stock_data[0][0], attribue])
        lettermonth_dict = {
            "Dec": 12, "Nov": 11, "Oct": 10, "Sep": 9, "Aug": 8,
            "Jul": 7, "Jun": 6, "May": 5, "Apr": 4, "Mar": 3, "Feb": 2, "Jan": 1
        }

        for data in stock_data[1:]:
            data_day, data_month, data_year = data[0].split("-")

            if (month != None):
                if (data_year == str(year)[2:]) and lettermonth_dict[data_month] == int(month):
                    result.append([data[0], data[attribute_id]])
                continue

            if (year != None):
                # print (data[0].startswith("2014"))
                if (data_year == str(year)[2:]):
                    result.append([data[0], data[attribute_id]])
                continue

            result.append([data[0], data[attribute_id]])
        return result

    def get_average_value_of_attribute(self, stock_data, attribue, year=None, month=None):
        attribute_stock_data = self.get_attribute_data(stock_data=stock_data, attribue=attribue, year=year, month=month)
        L = [float(value[1]) for value in attribute_stock_data[1:] ]
        return sum(L) / len(L)

    def write_csv_file_by_result(self, stock_data, filename):
        with open(filename, 'w', newline='', encoding="utf8") as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',',
                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csvwriter.writerows(stock_data)

    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def separate_user_query(self, user_input):
        user_query = [query.strip() for query in user_input.split(",")]
        return user_query

if __name__ == '__main__':
    unittest.main()
