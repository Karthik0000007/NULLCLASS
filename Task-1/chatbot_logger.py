import csv
import os
from datetime import datetime

LOG_FILE = "customer_service_interactions.csv"

def log_interaction(user_id, message, response, topic, satisfaction=None):
    log_exists = os.path.exists(LOG_FILE)
    with open(LOG_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not log_exists:
            writer.writerow(["timestamp", "user_id", "message", "response", "topic", "satisfaction"])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"), user_id, message, response, topic, satisfaction])
