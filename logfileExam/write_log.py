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

def main():
    # Specify the log file path
    log_file_path = 'logfile.txt'

    # Clear the contents of the log file if it exists
    if os.path.exists(log_file_path):
        with open(log_file_path, 'w'):
            pass

    # Create an instance of the Logger class
    logger = Logger(log_file_path)

    # Log outputs every second for a total of 5 times
    for i in range(1, 100):
        logger.log_output(f"this is check value {i}")
        time.sleep(1)

if __name__ == "__main__":
    main()