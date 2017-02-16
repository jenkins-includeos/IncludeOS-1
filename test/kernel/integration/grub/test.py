#! /usr/bin/env python

import sys
import os
import subprocess

includeos_src = os.environ.get('INCLUDEOS_SRC',
                               os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))).split('/test')[0])

from vmrunner import vmrunner

vm = vmrunner.vms[0];

# Build, run and clean
vm.cmake()

# Cmake changes to build dir
os.chdir("..")

# Use grubify-script
grubify = includeos_src + "/etc/scripts/grubify.sh"

# Create the GRUB image
subprocess.check_call(["bash",grubify,"build/test_grub", "-c"])

# Boot the image
vm.boot(multiboot = False)
