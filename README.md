# Windows Device Restarter

This simple Python script provides a quick way to restart a specific device on Windows using its device instance ID. It's particularly useful for resetting hardware like Wi-Fi adapters that may require a restart to function properly after the system wakes up from sleep or encounters connectivity issues.

## Prerequisites

Before you run this script, you will need:

- Python installed on your Windows machine.
- Administrative privileges to execute device management commands (PnPUtil).

## Usage

1. Find the device instance ID for the device you want to restart:
    - Open Device Manager.
    - Find the device in the list.
    - Right-click the device and select Properties.
    - Go to the Details tab.
    - Select "Device instance path" from the Property drop-down menu.
    - Copy the device instance ID.

2. Clone this repository to your local machine using `git clone` or download the ZIP.

3. Open the script `WinDevRes.py` in a text editor or IDE.

4. Replace the placeholder text in `INSTANCE_ID` with your device's instance ID copied from Device Manager.

    ```python
    INSTANCE_ID = r"Your_Copied_Device_Instance_ID"
    ```

5. Execute the script as an Administrator:
    - Simply run the Python script.
    - If administrative privileges are required, you will be prompted to grant them.
    - Alternatively, run the script from an elevated command prompt or PowerShell window.

## Configuration

- The script has a `show_terminal` variable which you can set to `True` or `False` depending on whether you want to show the terminal window or not.

## Important Notes

- Running device management commands requires administrative privileges. The script will prompt for these privileges if not already running with them.
- Use this script responsibly and only with devices you understand. Incorrect use may lead to system instability.
