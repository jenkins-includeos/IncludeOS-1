#! /usr/bin/env python

import sys
import os

includeos_src = os.environ.get('INCLUDEOS_SRC',
                               os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))).split('/test')[0])
print 'includeos_src: {0}'.format(includeos_src)
sys.path.insert(0,includeos_src + "/test")

import vmrunner
vm = vmrunner.vms[0]

num_elements = 0
num_header1 = 0
num_content = 0
num_header2 = 0

def increment_element(line):
  global num_elements
  num_elements += 1
  print "num_elements after increment: ", num_elements

def increment_header1(line):
  global num_header1
  num_header1 += 1
  print "num_header1 after increment: ", num_header1

def increment_content(line):
  global num_content
  num_content += 1
  print "num_content after increment: ", num_content

def increment_header2(line):
  global num_header2
  num_header2 += 1
  print "num_header2 after increment: ", num_header2

def check_num_outputs(line):
  assert(num_elements == 22)  # 2 * 11
  assert(num_header1 == 17)
  assert(num_content == 5)
  assert(num_header2 == 17)
  vmrunner.vms[0].exit(0, "SUCCESS")

# All elements in tarball
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/ - element", increment_element)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/l1_f1/ - element", increment_element)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/l1_f1/l2/ - element", increment_element)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/l1_f1/l2/README.md - element", increment_element)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/l1_f1/l2/service.cpp - element", increment_element)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/l1_f1/service.cpp - element", increment_element)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/l1_f1/Makefile - element", increment_element)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/second_file.md - element", increment_element)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/first_file.txt - element", increment_element)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/l1_f2/ - element", increment_element)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/l1_f2/virtio.hpp - element", increment_element)

# README.md's header
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/l1_f1/l2/README.md - name of README.md", increment_header1)
vm.on_output("Mode of README.md: 0000664", increment_header1)
vm.on_output("Uid of README.md: 0001750", increment_header1)
vm.on_output("Gid of README.md: 0001750", increment_header1)
vm.on_output("Size of README.md: 293", increment_header1)
vm.on_output("Mod_time of README.md: 13000173737", increment_header1)
vm.on_output("Checksum of README.md: 027565", increment_header1)
vm.on_output("Typeflag of README.md: 0", increment_header1)
vm.on_output("Linkname of README.md: ", increment_header1)
vm.on_output("Magic of README.md: ustar", increment_header1)
vm.on_output("Version of README.md: ", increment_header1)
vm.on_output("Uname of README.md: ", increment_header1)
vm.on_output("Gname of README.md: ", increment_header1)
vm.on_output("Devmajor of README.md: ", increment_header1)
vm.on_output("Devminor of README.md: ", increment_header1)
vm.on_output("Prefix of README.md: ", increment_header1)
vm.on_output("Pad of README.md: ", increment_header1)

# README.md's content
vm.on_output("README.md is not a folder and has content:", increment_content)
vm.on_output("First block of content: ### IncludeOS Demo Service", increment_content)
vm.on_output("This demo-service should start an instance of IncludeOS that brings up a minimal web service on port 80 with static content.", increment_content)
vm.on_output("Note: Remember to run the bridge creation script for networking to work on qemu ", increment_content)

# Folder l2's header and content (no content)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/l1_f1/l2/ - name of l2", increment_header2)
vm.on_output("Mode of l2: 0000775", increment_header2)
vm.on_output("Uid of l2: 0001750", increment_header2)
vm.on_output("Gid of l2: 0001750", increment_header2)
vm.on_output("Size of l2: 0", increment_header2)
vm.on_output("Mod_time of l2: 13017335436", increment_header2)
vm.on_output("Checksum of l2: 026307", increment_header2)
vm.on_output("Typeflag of l2: 5", increment_header2)
vm.on_output("Linkname of l2: ", increment_header2)
vm.on_output("Magic of l2: ustar", increment_header2)
vm.on_output("Version of l2: ", increment_header2)
vm.on_output("Uname of l2: ", increment_header2)
vm.on_output("Gname of l2: ", increment_header2)
vm.on_output("Devmajor of l2: ", increment_header2)
vm.on_output("Devminor of l2: ", increment_header2)
vm.on_output("Prefix of l2: ", increment_header2)
vm.on_output("Pad of l2: ", increment_header2)

vm.on_output("l2 is a folder", increment_content)

# All elements in tarball's name and typeflag (0 is file and 5 is folder)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/ Typeflag: 5", increment_element)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/l1_f1/ Typeflag: 5", increment_element)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/l1_f1/l2/ Typeflag: 5", increment_element)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/l1_f1/l2/README.md Typeflag: 0", increment_element)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/l1_f1/l2/service.cpp Typeflag: 0", increment_element)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/l1_f1/service.cpp Typeflag: 0", increment_element)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/l1_f1/Makefile Typeflag: 0", increment_element)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/second_file.md Typeflag: 0", increment_element)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/first_file.txt Typeflag: 0", increment_element)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/l1_f2/ Typeflag: 5", increment_element)
vm.on_output("/IncludeOS/test/util/integration/tar/tar_example/l1_f2/virtio.hpp Typeflag: 0", increment_element)

vm.on_output("Something special to close with", check_num_outputs)

# Boot the VM, taking a timeout as parameter
vm.cmake().boot(20).clean()
