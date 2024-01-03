import csv
import pandas
field=['roll no','name','age']
sdict=[{'roll no':43,'name':'jo','age':21},
{'roll no':4,'name':'jake','age':20}]
with open('dept.csv',"w") as dfile:
	writer=csv.DictWriter(dfile,fieldnames=field)
	writer.writeheader()
	writer.writerows(sdict)
data=pandas.read_csv("dept.csv")
print (data)
	
