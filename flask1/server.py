import sys
import web
import json
import time
import utils
import logging
import os
import cacheloader
import bot_controller
from flask import Flask

app = Flask(__name__)

print("Server.py imports done")

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename = utils.base_dir + 'fns_ke_server.log', level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)
tracer = logging.getLogger('elasticsearch')
tracer.setLevel(logging.CRITICAL) # or desired level


port = int(os.getenv('PORT', 8000))

@app.route("/")
def POST(self):
        
        print("###############################################")
        logger.info("#########################################")
        
        web.header('Content-Type', 'application/json')
		
        data = web.data()
        data =  data.decode('utf-8')
        print("**************************",type(data))
        user_data = json.loads(data)
        logger.info("#### REQUEST JSON : %s", str(user_data))
        
        b4_millis = int(round(time.time() * 1000))
        print('b4_millis --->', b4_millis)
        
        result = bot_controller.fetch_response(user_data, cacheloader)
        logger.info("#### RESPONSE JSON : %s", str(result).encode("ascii", "ignore"))
        
        after_millis = int(round(time.time() * 1000))
        
        print('after_millis --->', after_millis)
        time_taken = round((after_millis - b4_millis) / 1000, 2)
        print('time taken --->', time_taken)
        logger.info("#### TimeTaken : %s", str(time_taken))
            
        return json.dumps(result)


if __name__ == "__main__":
    cacheloader.load_model_cache()
    cacheloader.load_user_cache()
    cacheloader.load_discoverable_report_cache()
    #app.run()
    #app.run()
    app.run(host='0.0.0.0', port=port, debug=True)

