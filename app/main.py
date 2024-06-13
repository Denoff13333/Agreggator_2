import socket
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from models import session, AccessLog
from config.settings import config
from sqlalchemy import func
from datetime import datetime
import click

def get_current_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

@click.group()
def cli():
    pass

@cli.command()
@click.option('--ip', help='Filter by IP address')
@click.option('--start', help='Start date (YYYY-MM-DD)')
@click.option('--end', help='End date (YYYY-MM-DD)')
def view(ip, start, end):
    if ip is None:
        ip = get_current_ip()
    query = session.query(AccessLog)
    if ip:
        query = query.filter(AccessLog.ip_address == ip)
    if start:
        start_date = datetime.strptime(start, '%Y-%m-%d')
        query = query.filter(AccessLog.timestamp >= start_date)
    if end:
        end_date = datetime.strptime(end, '%Y-%m-%d')
        query = query.filter(AccessLog.timestamp <= end_date)
    
    logs = query.all()
    for log in logs:
        click.echo(f"{log.timestamp} {log.ip_address} {log.request_method} {log.request_path} {log.response_code} {log.user_agent}")

@cli.command()
def stats():
    ip_stats = session.query(AccessLog.ip_address, func.count(AccessLog.id)).group_by(AccessLog.ip_address).all()
    for ip, count in ip_stats:
        click.echo(f"{ip}: {count}")

if __name__ == '__main__':
    cli()
