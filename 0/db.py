import sqlite3 as lite
import csv
import os
from datetime import datetime
class Color:
    def __init__(self,conn):
        self.conn=conn
        self.c=conn.cursor()
        
    def __exit__(self, exc_type, exc_val, exc_tb):     
        self.c.close()
    
    def NewColor(self,cn_name):
        self.c.execute(f"INSERT INTO TN_COLOR (CN_NAME) VALUES('{cn_name}')")
        self.conn.commit()
        self.c.execute("SELECT CN_ID FROM TN_COLOR ORDER BY CN_ID DESC LIMIT 1")
        ret=self.c.fetchone()
        return ret[0]
        
    def ColorID(self,cn_name):
        self.c.execute("SELECT CN_ID FROM TN_COLOR WHERE CN_NAME=?", (cn_name,))
        ret=self.c.fetchone()
        if ret:
            return ret[0]
        else:
            return self.NewColor(cn_name)
class Country:
    def __init__(self,conn,code):
        self.conn=conn
        self.c=conn.cursor()
        self.code=code.upper()
        self.name=self.Name()
        self.id=self.ID()
        
    def __exit__(self, exc_type, exc_val, exc_tb):     
        self.c.close()
    
    def NewCountry(self,cn_code):
        self.c.execute(f"INSERT INTO TN_COUNTRY (CN_CODE) VALUES('{cn_code}')")
        self.conn.commit()
        self.c.execute("SELECT CN_ID FROM TN_COUNTRY ORDER BY CN_ID DESC LIMIT 1")
        ret=self.c.fetchone()
        return ret[0]
        
    def ID(self):
        self.c.execute("SELECT CN_ID FROM TN_COUNTRY WHERE CN_CODE=?", (self.code,))
        ret=self.c.fetchone()
        if ret:
            return ret[0]
        else:
            return self.NewCountry(self.code)                           
        
    def Name(self):
        self.c.execute("SELECT CN_NAME FROM TN_COUNTRY WHERE CN_CODE=?", (self.code,))
        ret=self.c.fetchone()
        if ret:
            return ret[0]
        
        
conn=lite.connect("c:\chrome\hermes.db")
c=conn.cursor()

csv_file_path = f"{os.path.dirname(os.path.abspath(__file__))}\country.csv"

data_dict = {}

""" with open(csv_file_path, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if len(row) >= 3:
            key=row[2]
            value ={'port':row[0], 'name':row[1]}
            data_dict[key]=value
            c.execute(f"insert into TN_COUNTRY (CN_ID,CN_CODE,CN_NAME) VALUES('{row[0]}','{key}','{row[1]}')") """
            
            
update_query = "UPDATE TN_COUNTRY SET CN_CODE = LOWER(CN_CODE)"
c.execute(update_query)

color=Color(conn)  
colorid=color.ColorID("Black")
cn=Country(conn,"us")




conn.commit()
c.close()
conn.close()

