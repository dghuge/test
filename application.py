import os
import logging
from logging.handlers import RotatingFileHandler

from decouple import config
from flask import Flask
from flask_cors import  CORS,cross_origin
from dotenv import  load_dotenv

# logger = logging.getLogger(__name__)
# formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# logger.setLevel(logging.DEBUG)
# handler = RotatingFileHandler('/opt/python/log/application.log', maxBytes=1024, backupCount=5)
# handler.setFormatter(formatter)

application = Flask(__name__)
#application.logger.addHandler(handler)

logging.basicConfig(filename='record.log', level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')

@application.route('/', methods = ['GET','POST'])
@cross_origin()
def home():
    try:
        load_dotenv()
        application.logger.info('picking config using dotenv...')
        return os.environ['DOTE']
    except:
        try:
            application.logger.info('picking config using decouple...')
            return config('DECOUP','nodata decoupe')
        except Exception as e:
            application.logger.error('Error with env'+e)
            # logger.error('error with env'+e)


if __name__ == '__main__':
    application.run(debug=True)