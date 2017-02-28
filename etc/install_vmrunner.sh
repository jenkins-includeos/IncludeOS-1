#!/bin/bash

# Installs the vmrunner python package

INCLUDEOS_SRC=${INCLUDEOS_SRC-$HOME/IncludeOS}
INCLUDEOS_PREFIX=${INCLUDEOS_PREFIX-/usr/local}
#INCLUDEOS_VMRUNNER_INSTALL=${INCLUDEOS_VMRUNNER_INSTALL-GLOBAL} 

# Install vmrunner globally if specified
pushd $INCLUDEOS_SRC/vmrunner
if [ "$INCLUDEOS_PREFIX" = "/usr/local" ]; then
	sudo python setup.py install
else 
	python setup.py install --prefix=$INCLUDEOS_PREFIX/bin
fi
popd
