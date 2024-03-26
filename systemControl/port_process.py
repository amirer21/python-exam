import psutil

def get_process_info():
    # Iterate over all running processes
    for proc in psutil.process_iter(['pid', 'name', 'exe', 'connections']):
        try:
            # Fetch connections for the process
            connections = proc.info['connections']
            # Filter processes with active connections
            if connections:
                for conn in connections:
                    if conn.laddr and conn.status == psutil.CONN_ESTABLISHED:
                        print(f"PID: {proc.pid}, Name: {proc.info['name']}, Path: {proc.info['exe']}, Port: {conn.laddr.port}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass  # This process no longer exists or access is denied

if __name__ == "__main__":
    get_process_info()