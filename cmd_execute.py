# put cmd in cmd, outcome is a string
import subprocess
cmd = "wmic MEMORYCHIP get Capacity"
outcome = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
