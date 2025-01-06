import psutil
import subprocess
import time
from datetime import datetime

# Configuration
CPU_THRESHOLD = 80  # CPU usage threshold percentage
SERVICE_NAME = "laravel-backend"  # Name of the Laravel backend service
CHECK_INTERVAL = 30  # Time (in seconds) between CPU checks


def get_cpu_usage():
    """Get the current CPU usage as a percentage."""
    return psutil.cpu_percent(interval=1)


def restart_service(service_name):
    """Restart the specified service."""
    try:
        print(f"{datetime.now()}: High CPU usage detected. Restarting the {service_name} service...")
        # Restart the service using systemctl
        subprocess.run(["sudo", "systemctl", "restart", service_name], check=True)
        
        # Check if the service restarted successfully
        result = subprocess.run(["systemctl", "is-active", service_name], capture_output=True, text=True)
        if result.stdout.strip() == "active":
            print(f"{datetime.now()}: {service_name} service restarted successfully.")
        else:
            print(f"{datetime.now()}: Failed to restart {service_name} service. Please check manually.")
    except subprocess.CalledProcessError as e:
        print(f"{datetime.now()}: Error restarting service: {e}")


def main():
    """Main loop to monitor CPU usage and restart service if needed."""
    while True:
        cpu_usage = get_cpu_usage()
        print(f"{datetime.now()}: Current CPU usage: {cpu_usage}%")
        
        if cpu_usage > CPU_THRESHOLD:
            restart_service(SERVICE_NAME)
        
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
