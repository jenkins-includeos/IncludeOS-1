pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh './install.sh'
        node(label: 'build')
        ansiColor(colorMapName: 'xterm')
      }
    }
  }
  environment {
    INCLUDEOS_SRC = '$WORKSPACE'
    INCLUDEOS_PREFIX = '$WORKSPACE/INCLUDEOS_INSTALL'
  }
}