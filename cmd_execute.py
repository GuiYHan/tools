# put cmd in cmd, outcome is a string
import subprocess
cmd = "wmic MEMORYCHIP get Capacity"
outcome = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)


# independent totototal independent process, does not influence by pop ups
import subprocess
cmd = "wmic MEMORYCHIP get Capacity"
outcome = subprocess.Popen(cmd, stderr=subprocess.STDOUT, shell=True)

# staart with no admin priviliage
import subprocess
cmd = 'runas /trustlevel:0x20000 "cmd @cmd /k wmic MEMORYCHIP get Capacity"'
outcome = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)