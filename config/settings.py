import os

class Config:
    LOG_DIR = os.getenv('LOG_DIR', 'C:/Users/Denil/apache2/apache-log-aggregator/logs')
    LOG_MASK = os.getenv('LOG_MASK', '*.log')
    basedir = os.path.abspath(os.path.dirname(__file__))
    DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../app.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    CRON_INTERVAL = os.getenv('CRON_INTERVAL', '*/5 * * * *')

config = Config()
