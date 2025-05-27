import csv
import pandas as pd
from datetime import datetime

with open('./data.csv', mode='a', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Example: Writing a header and some data
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'Los Angeles'])
    reader = csv.reader(file)
    



class CsvManager:
    def __init__(self):
        self.file_path = "./data.csv"
        file = open(self.file_path, 'a', encoding='utf-8')
        self.data = pd.read_csv(self.file_path)
        

    def add_line(self,name, txt, bQty, bPrice, sPrice, shipping, shippingFee, imgUrl):
        margin = sPrice - bPrice - shippingFee
        stuffStack = String(bQty) +'/0'
        today_str = datetime.today().strftime('%Y-%m-%d')
        self.data.loc[len(self.data)] = [today_str, name, txt, imgUrl, bPrice, sPrice, shipping, shippingFee, margin, stuffStack, 0]
        self.data.to_csv(self.file_path, index=False, mode='a', header=False)

    def save(self):
        self.data.to_csv(self.file_path, index=False, mode='a', header=False)
        

    def __del__(self):
        file.close() 


csvManager = CsvManager()
csvManager.add_line(['이어폰', '설명설명설....', 10, 2000, 7000, '3호박스 우체국', '3000', './' ])
# csvManager.save()