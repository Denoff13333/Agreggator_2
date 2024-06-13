import sys
import os
import re
import glob
from datetime import datetime

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from app.models import AccessLog, session
from config.settings import config

log_pattern = re.compile(r'(?P<ip>\S+) \S+ \S+ \[(?P<time>.*?)\] "(?P<method>\S+) (?P<path>\S+).*" (?P<status>\d+) \S+ "(?P<agent>.*?)"')

def parse_logs():
    log_files = glob.glob(os.path.join(config.LOG_DIR, config.LOG_MASK))
    for log_file in log_files:
        with open(log_file) as f:
            for line in f:
                match = log_pattern.match(line)
                if match:
                    data = match.groupdict()
                    log_entry = AccessLog(
                        ip_address=data['ip'],
                        timestamp=datetime.strptime(data['time'], '%d/%b/%Y:%H:%M:%S %z'),
                        request_method=data['method'],
                        request_path=data['path'],
                        response_code=int(data['status']),
                        user_agent=data['agent']
                    )
                    session.add(log_entry)
            session.commit()

if __name__ == '__main__':
    parse_logs()
