from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import parse_qs
from betes_db import BetesDB

class MyRequestHandler(BaseHTTPRequestHandler):

    def handleNotFound(self):
        self.send_response(404)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("Not Found", "utf-8"))




    def handleRegister(self):
        length = int(self.headers["Content-Length"])
        request_body = self.rfile.read(length).decode("utf-8")
        parsed_body = parse_qs(request_body)

        auth_fName = parsed_body['fName'][0]
        auth_lName = parsed_body['lName'][0]
        auth_email = parsed_body['email'][0]
        auth_password = parsed_body['password'][0]
        

        db = BetesDB()
        db.createUser(auth_fName, auth_lName, auth_email, auth_password )

        self.send_response(201)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

    
    def verifyUser(self):
        
        length = int(self.headers["Content-Length"])
        request_body = self.rfile.read(length).decode("utf-8")
        parsed_body = parse_qs(request_body)

        user_email = parsed_body['email'][0]
        user_password = parsed_body['password'][0]
            
        db = BetesDB()
        user = db.GetUser(user_email, user_password)

        if user == False:
            #make 401 error
            self.handle401()

        else:
            self.send_response(201)
            # save user ID into the session data
            self.sessionData["userId"] = user["id"]
            self.end_headers()
            print("true")


    def handleListCalcVar(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        #dummy db
        db = BetesDB()
        allRecords = db.getCalculation()
        #print(allRecords)
        self.wfile.write(bytes(json.dumps(allRecords), "utf-8"))


    def handleCreateCalc(self):
        
        #step 1
        length = int(self.headers["Content-Length"])
        #step 2
    
        request_body = self.rfile.read(length).decode("utf-8")
        #step 3
        parsed_body = parse_qs(request_body)
        #step 4
        u_correction_factor = parsed_body['correction_factor'][0]
        u_correction_variable = parsed_body['priority'][0]
        u_icr_ratio = parsed_body['icr_ration'][0]
        u_long_lasting_one = parsed_body['long_lasting_one'][0]
        u_bs_high = parsed_body['bs_high'][0]
        u_bs_low = parsed_body['bs_low'][0]
        u_bs_target = parsed_body['bs_target'][0]
        u_precision = parsed_body['precision'][0]
        u_iob = parsed_body['iob'][0]
        u_duration = parsed_body['duration'][0]
        #TO_DO.append(task)
        #dummy db
        db = BetesDB()
        db.createCalculations(u_correction_factor, u_correction_variable, u_icr_ratio, u_long_lasting_one, u_bs_high, u_bs_low, u_bs_target, u_precision, u_iob, u_duration)

        #respond to client
        self.send_response(201)
        self.send_header("Content-Type", "application/json")
        self.end_headers()


    def handleUpdateCalc(self, task_id):
        db=BetesDB()
        calcRecord = db.getCalculation(task_id)

        if calcRecord != None:

            length = int(self.headers["Content-Length"])
            request_body = self.rfile.read(length).decode("utf-8")
            parsed_body = parse_qs(request_body)

            u_correction_factor = parsed_body['correction_factor'][0]
            u_correction_variable = parsed_body['priority'][0]
            u_icr_ratio = parsed_body['icr_ration'][0]
            u_long_lasting_one = parsed_body['long_lasting_one'][0]
            u_bs_high = parsed_body['bs_high'][0]
            u_bs_low = parsed_body['bs_low'][0]
            u_bs_target = parsed_body['bs_target'][0]
            u_precision = parsed_body['precision'][0]
            u_iob = parsed_body['iob'][0]
            u_duration = parsed_body['duration'][0]

            db.updateCalc(u_correction_factor, u_correction_variable, u_icr_ratio, u_long_lasting_one, u_bs_high, u_bs_low, u_bs_target, u_precision, u_iob, u_duration)

            self.send_response(201)
            #self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
        else:
            self.handleNotFound()
