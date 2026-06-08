import logging
from flask import Flask

app = Flask(__name__)

# Налаштування логування [cite: 941-942]
logging.basicConfig(filename='logfile.log', level=logging.DEBUG)

@app.route('/')
def hello():
    app.logger.info('Processing default request') # Генерація логу при запиті [cite: 945]
    return 'Hello World from ELK Practical!'

if __name__ == '__main__':
    app.run()