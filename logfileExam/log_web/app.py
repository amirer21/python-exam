from flask import Flask, render_template
from flask_socketio import SocketIO
import os
import time
from threading import Thread

app = Flask(__name__)
socketio = SocketIO(app)

# Specify the absolute path to the log file
log_file_path = 'D:\\python_workspace\\python-exam\\logfileExam\\logfile.txt'

# Store the initial modification time of the log file
initial_modification_time = os.path.getmtime(log_file_path)

def monitor_log_changes():
    global initial_modification_time

    while True:
        # Get the current modification time of the log file
        current_modification_time = os.path.getmtime(log_file_path)

        # Check if the file has been modified since the last check
        if current_modification_time != initial_modification_time:
            # Read the last line of the log file
            with open(log_file_path, 'r') as file:
                lines = file.read().splitlines()
                last_line = lines[-1] if lines else ""

            # Update the initial modification time
            initial_modification_time = current_modification_time

            # Send the updated value to the web page using SocketIO
            socketio.emit('log_update', {'value': last_line}, namespace='/log')

        time.sleep(1)  # Check every 1 second (adjust as needed)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/log')
def handle_connect():
    # Send the initial value to the web page when a client connects
    with open(log_file_path, 'r') as file:
        lines = file.read().splitlines()
        last_line = lines[-1] if lines else ""
    socketio.emit('log_update', {'value': last_line}, namespace='/log')

if __name__ == '__main__':
    # Start the monitoring thread
    monitor_thread = Thread(target=monitor_log_changes)
    monitor_thread.daemon = True
    monitor_thread.start()

    # Start the Flask-SocketIO application
    socketio.run(app, debug=True)