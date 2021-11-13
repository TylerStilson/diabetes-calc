import sqlite3
from passlib.hash import bcrypt
import urllib.parse

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class BetesDB:
    def __init__(self):
        self.connection = sqlite3.connect("users.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()
        return

    
    def createCalcTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS calc (id SERIAL PRIMARY KEY, bs_target INTEGER(10), corr_factor INTEGER(10), carb_ratio INTEGER(10), precision INTEGER(10))")
        self.connection.commit()

    def deleteCalcTable(self):
        self.cursor.execute("DROP TABLE calc")
        self.connection.commit()


    
    def getCalculation(self):
        self.cursor.execute("SELECT * FROM calc WHERE id = 1")
        user_calcs = self.cursor.fetchone()
        return user_calcs


    def createCalculations(bs_target, corr_factor, carb_ratio, precision):
        data = [bs_target, corr_factor, carb_ratio, precision]
        self.cursor.execute("INSERT INTO calc (bs_target, corr_factor, carb_ratio, precision) VALUES (?, ?, ?, ?)", data)
        self.connection.commit()
        return

    def updateCalc(bs_target, corr_factor, carb_ratio, precision):
        data = [bs_target, corr_factor, carb_ratio, precision]
        self.cursor.execute("UPDATE todo SET (bs_target, corr_factor, carb_ratio, precision) VALUES (?, ?, ?, ?)", data)
        self.connection.commit()
        return

    