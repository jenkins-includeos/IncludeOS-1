pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        node(label: 'build')
        sh './install.sh'
      }
    }
  }
  environment {
    INCLUDEOS_SRC = '$WORKSPACE'
    INCLUDEOS_PREFIX = '$WORKSPACE/INCLUDEOS_INSTALL'
  }
}