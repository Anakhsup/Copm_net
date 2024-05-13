import csv 
import subprocess
import socket
import time


domains = ["google.com", "facebook.com", "twitter.com", "linkedin.com", "youtube.com",
            "instagram.com", "amazon.com", "reddit.com", "stackoverflow.com", "github.com"]

def ping_websites(domains):
    with open("ping_data.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file) 
        csv_writer.writerow(['Domain', 'IP', 'Timestamp', 'Ping Result (ms)'])

        for domain in domains:
            try:
                ip = socket.gethostbyname(domain)
                for _ in range(1):
                    start_time = time.time() 
                    ping_result = subprocess.run(['ping', '-c', '1', domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)                   
                    end_time = time.time()
                    ping_time = (end_time - start_time) * 1000
                    csv_writer.writerow([domain, ip, time.time(), ping_time]) 
            
            except Exception as e:
                print(f"Error pinging {domain}: {e}")        

ping_websites(domains)