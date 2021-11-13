import sqlite3

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


    #calc queries
    def getCalculation(self):
        data = [user_id]
        self.cursor.execute("SELECT * FROM calc WHERE id = ?", data)
        user_calcs = self.cursor.fetchone()
        return


    def createCalculations(healthId, correction_factor, correction_variable, icr_ratio, long_lasting_one, bs_high, bs_low, bs_target, precision, iob, duration):
        data = [healthId, correction_factor, correction_variable, icr_ratio, long_lasting_one, bs_high, bs_low, bs_target, precision, iob, duration]
        self.cursor.execute("INSERT INTO calc (healthId, correction_factor, correction_variable, icr_ratio, long_lasting_one, bs_high, bs_low, bs_target, precision, iob, duration) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
        self.connection.commit()
        return

    def updateCalc(healthId, correction_factor, correction_variable, icr_ratio, long_lasting_one, bs_high, bs_low, bs_target, precision, iob, duration):
        data = [healthId, correction_factor, correction_variable, icr_ratio, long_lasting_one, bs_high, bs_low, bs_target, precision, iob, duration]
        self.cursor.execute("UPDATE todo SET healthID = ?, correction_factor = ?, correction_variable = ?, icr_ratio = ?, long_lasting_one = ?, bs_high = ?, bs_low = ?, bs_target = ?, precision = ?, iob = ?, duration = ? WHERE id = ?", data)
        self.connection.commit()
        return

    
    # user queries
    def createUser(fName, lName, email, password, dob, sex, weight, height):
        hashpass = bcrypt.hash(password)
        data = [fName, lName, email, password, dob, sex, weight, height, hashpass]
        self.cursor.execute("INSERT INTO users (fName, lName, email, password, dob, sex, weight, height) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", data)
        self.connection.commit()
        return

    def getUserData(self):
        data = [user_id]
        self.cursor.execute("SELECT * FROM calc WHERE id = ?", data)
        user = self.cursor.fetchone()
        return

    def GetUser(self, email, password):
        data = [email]
        self.cursor.execute("SELECT * FROM auth WHERE email = %s", data)
        user = self.cursor.fetchone()
        if user == None:
            check = False
            return check
        else:
            check = bcrypt.verify(password, user["password"])
            if check == False:
                print("wrong password")
                return check
            return user
