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

    # def end_headers(self):                           #send cookies to client first
    #     self.send_header("Access-Control-Allow-Origin", self.headers["Origin"])
    #     self.send_header("Access-Control-Allow-Credentials", "true")
    #     BaseHTTPRequestHandler.end_headers(self)    #call the original end_headers()


    def handleCreateTable(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        db = BetesDB()
        db.createCalcTable()

        self.send_response(201)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

    
    def handleDeleteTable(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        db = BetesDB()
        db.deleteCalcTable()

        self.send_response(201)
        self.send_header("Content-Type", "application/json")
        self.end_headers()



    def handleRetrieveCalc(self):
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
        bs_target = parsed_body['bs_target'][0]
        corr_factor = parsed_body['corr_factor'][0]
        carb_ratio = parsed_body['carb_ratio'][0]
        precision = parsed_body['precision'][0]
        
        #TO_DO.append(task)
        #dummy db
        db = BetesDB()
        db.createCalculations(bs_target, corr_factor, carb_ratio, precision)

        #respond to client
        self.send_response(201)
        self.send_header("Content-Type", "application/json")
        self.end_headers()


    def handleUpdateCalc(self, task_id):
        db = BetesDB()

        length = int(self.headers["Content-Length"])
        request_body = self.rfile.read(length).decode("utf-8")
        parsed_body = parse_qs(request_body)

        bs_target = parsed_body['bs_target'][0]
        corr_factor = parsed_body['corr_factor'][0]
        carb_ratio = parsed_body['carb_ratio'][0]
        precision = parsed_body['precision'][0]

        db.updateCalc(bs_target, corr_factor, carb_ratio, precision)

        self.send_response(201)
        #self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()


    def do_OPTIONS(self):
        self.loadSession()
        self.send_response(204)
        #self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


    def do_GET(self):
        print("request path is:", self.path)
        if collection == "calculations":
            self.handleRetrieveCalc()
            
        else:
            self.handleNotFound()




    def do_POST(self):
        print("request path is:", self.path)
        if self.path == "/setup_calc":
            self.handleCreateCalc
        else:
            self.handleNotFound()




    def main ():
    #change 
    #to pull port from heroku
    db = BetesDB()
    db.deleteCalcTable
    db.createCalcTable
    db = None

    port = 8080
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    listen = ("0.0.0.0", port)
    server = HTTPServer(listen, MyRequestHandler)
    print("the server is running!")
    server.serve_forever()
    print("This will never, ever execute.")

main()
        
