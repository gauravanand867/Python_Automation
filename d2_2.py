import os
import sys

saved_profile=os.popen('nmcli c').read()
print(saved_profile)