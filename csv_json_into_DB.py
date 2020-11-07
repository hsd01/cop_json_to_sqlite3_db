import pandas as pd
import json
import sqlite3

conn = sqlite3.connect('c:/Users/Taka/Desktop/GDT_1.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS GreenDeck
	(name TEXT, brand_name TEXT, regular_price_value REAL, offer_price_value REAL, 
	 currency TEXT, classification_l1 TEXT, classification_l2 TEXT, classification_l3 TEXT,
	 classification_l4 TEXT)""")

df = pd.read_json("C:/Users/Taka/Desktop/js.json")
name = df['name']
name=name
brand = df['brand_name']
brand = brand
rp = df['regular_price_value']
rp = rp
of = df['offer_price_value']
of = of
curr = df['currency']
curr=curr
c1=df['classification_l1']
c2=df['classification_l2']
c3=df['classification_l3']
c4=df['classification_l4']
c1=c1
c2=c2
c3=c3
c4=c4
print("**************")
ml = [(name[i], brand[i], rp[i], of[i], curr[i], c1[i], c2[i], c3[i], c4[i]) for i in range(0,len(name))]

for i in ml:
    #print(i)
    c.execute("""INSERT INTO GreenDeck(name,brand_name,regular_price_value, offer_price_value, 
	 currency, classification_l1, classification_l2, classification_l3, classification_l4)
	  VALUES(?,?,?,?,?,?,?,?,?)""", (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
    
    

conn.commit()

conn.close()
