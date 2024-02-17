import ctypes
import time

# You can find the device instance ID by going to the properties of the device in Device Manager, then the Details tab, and selecting "Device instance path" from the Property drop-down menu.
INSTANCE_ID = r""

show_terminal = False

cmd_command = f'/k pnputil /restart-device "{INSTANCE_ID}" && exit'

ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", cmd_command, None, show_terminal)

time.sleep(1)