import pandas as pd
import glob
import os
import sqlite3
import csv
from os import path
from typing import final
from getRate import rate
from db_queries import create_data

def process(data):
    data[2] = float(data[2])
    transfer_rate = rate(data[0], data[1])
    converted_amount = data[2] * transfer_rate
    return transfer_rate, converted_amount
# file_path  = '/Users/sanleypeter/Desktop/TransferMate/data/csv/'
# print(type(file_path))
def read_file(file_path):
    file_path = str(file_path)
    csvfiles = []
    path = os.path.join(file_path)
    csvfiles = glob.glob(path+"/*.csv")
    print(*csvfiles, sep='\n')
    list_df = []
    con = sqlite3.connect(os.getcwd() + "/database/currency.db")
    cur = con.cursor()
    for csvfile in csvfiles:
        with open(csvfile, "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            if header != None:
                for row in reader:
                    transfer_rate, converted_amount = process(row)
                    row.extend([transfer_rate, converted_amount])
                    last_id = create_data(con, row)
                
    con.close()

