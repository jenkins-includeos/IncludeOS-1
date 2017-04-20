pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''./install.sh
'''
      }
    }
  }
  environment {
    INCLUDEOS_SRC = '$WORKSPACE'
    INCLUDEOS_PREFIX = '$WORKSPACE/INCLUDEOS_INSTALL'
  }
}