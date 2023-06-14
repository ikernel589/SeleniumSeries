import os
import csv
class Const():
    def __init__(self):
        self.driver_path=r"C:\chrome\chromedriver.exe"
        self.output_path=r"C:\chrome\output"
        self.BASE_URL1 = "https://www.hermes.com/code/en/category/women/bags-and-small-leather-goods/small-leather-goods/#|"
        self.BASE_URL0 = "https://www.hermes.com/us/en/category/women/bags-and-small-leather-goods/bags-and-clutches/#|"
        self.items=self.load_items()
        self.country=self.load_country()
        
    def load_items(self):
        csv_file_path = f"{os.path.dirname(os.path.abspath(__file__))}\items.csv"

        data_list = []
        string_array = []
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                string_array.append(','.join(row))
                data_list.append(row)
                
        return string_array
    
    def load_country(self):
        csv_file_path = f"{os.path.dirname(os.path.abspath(__file__))}\country.csv"

        data_dict = {}

        with open(csv_file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if len(row) >= 3:
                    key=row[2]
                    value ={'port':row[0], 'name':row[1]}
                    data_dict[key]=value
        
        return data_dict