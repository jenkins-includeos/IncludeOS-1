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
    INCLUDEOS_INSTALL = '$WORKSPACE/INCLUDEOS_INSTALL'
  }
}