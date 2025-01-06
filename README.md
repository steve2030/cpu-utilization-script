# Monitor and Restart Laravel Service on High CPU Usage

## Overview

This script monitors the CPU usage of your system and automatically restarts the Laravel backend service if CPU usage exceeds a specified threshold (default: 80%). It uses the Python `psutil` library for monitoring CPU usage and interacts with `systemd` to manage the Laravel service.

---

## Features

- Monitors CPU usage in real-time.
- Automatically restarts the specified Laravel backend service when CPU usage exceeds the defined threshold.
- Logs actions with timestamps to the console.

---

## Prerequisites

1. **Python**:
   - Ensure Python 3.6 or higher is installed on your system.
   - Install the required library:
     ```bash
     pip install psutil
     ```

2. **Systemd**:
   - Ensure the Laravel backend service is managed by `systemd` (e.g., `laravel-backend`).

3. **Permissions**:
   - The script uses `sudo` to restart the service, so it must be run with a user account that has appropriate privileges.

---

## Configuration

You can configure the following parameters in the script:

- `CPU_THRESHOLD`: The CPU usage percentage that triggers a service restart (default: `80`).
- `SERVICE_NAME`: The name of the Laravel service to restart (default: `laravel-backend`).
- `CHECK_INTERVAL`: The interval (in seconds) between consecutive CPU usage checks (default: `30`).

---

## Usage

1. **Save the Script**:
   Save the script as `cpu_usage.py`.

2. **Run the Script**:
   Run the script using Python:
   ```bash
   python cpu_usage.py
