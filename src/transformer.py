import pandas as pd

def transform(x):
    return x
	
	
import json 
import csv 
   
  
student_data = data['data'] 
  
# now we will open a file for writing 
data_file = open('sample_data_2.csv', 'w') 
  
# create the csv writer object 
csv_writer = csv.writer(data_file) 
  
# Counter variable used for writing  
# headers to the CSV file 
count = 0
  
for std in student_data : 
    if count == 0: 
  
        # Writing headers of CSV file 
        header = std.keys() 
        csv_writer.writerow(header) 
        count += 1
  
    # Writing data of CSV file 
    csv_writer.writerow(std.values()) 
  
data_file.close()