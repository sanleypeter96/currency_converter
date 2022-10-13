from multiprocessing import Process
import os
from process import read_file
import sqlite3
import pandas as pd
from concurrent.futures import ProcessPoolExecutor

file_paths = [
    '/Users/sanleypeter/Desktop/TransferMate/data/csv', 
    '/Users/sanleypeter/Desktop/TransferMate/data/csv2']

def post_work():
    con = sqlite3.connect(os.getcwd() + "/database/currency.db")
    db_df = pd.read_sql_query("SELECT * from Currency", con)
    print(db_df)
    con.close()

if __name__ == '__main__':
    # create a process pool with the default number of worker processes
    executor = ProcessPoolExecutor(max_workers=4)
    for result in executor.map(read_file, file_paths):
	    print("Success!")
    post_work()

    # p1 = Process(target=read_file, args=('/Users/sanleypeter/Desktop/TransferMate/data/csv',))
    # p2 = Process(target=read_file, args=('/Users/sanleypeter/Desktop/TransferMate/data/csv2',))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    # print("Both Processes Completed!")

#Read contents from database
