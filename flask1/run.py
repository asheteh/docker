import os
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

data = {}
app = Flask(__name__)

@app.route("/")
def index():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")
    print(get_discoverable_reports())
    if app_name:
        return "App loading .................."

    return "Hello from Flask"

def test1():
    print("\n\n Inside test1 \n\ns")
    data['test'] = "Test 1"

def test2():
    data['test-2'] = "Test 2"

def test3():
    data['test3'] = "Test 3"

@app.route("/get_discoverable_reports")
def get_discoverable_reports():
    test1()
    test2()
    test3()
    print("\n\n*** Inside \n\n ")
    #load_discoverable_report_cache()
    return data


'''
scheduler = BackgroundScheduler()
scheduler.add_job(func=test1, trigger="interval", seconds = 20)
scheduler.add_job(func=test2, trigger="interval", seconds = 20)
scheduler.add_job(func=test3, trigger="interval", seconds = 20)
scheduler.start()
'''
if __name__ == "__main__":
   
    
    app.run()