import psutil
import time

def system_monitor():
    while True:
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        print(f"CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage}%")
        time.sleep(10)

if __name__ == "__main__":
    try:
        system_monitor()
    except KeyboardInterrupt:
        print("Monitoring stopped.")