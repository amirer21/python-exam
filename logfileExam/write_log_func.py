import time
import os

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file

    def log_output(self, *outputs):
        with open(self.log_file, 'a') as file:
            for output in outputs:
                print(output)
                file.write(str(output) + '\n')

def clear_log_file(log_file_path):
    if os.path.exists(log_file_path):
        with open(log_file_path, 'w'):
            pass

def save_to_logfile(value, log_file_path='logfile.txt'):
    logger = Logger(log_file_path)
    logger.log_output(value)

def main():
    log_file_path = 'logfile.txt'
    clear_log_file(log_file_path)

    for i in range(1, 100):
        save_to_logfile(f"this is check value {i}")
        time.sleep(1)

if __name__ == "__main__":
    main()
