
pipeline {
  agent any
  options { disableConcurrentBuilds(); timeout(time: 15, unit: 'MINUTES') }
  stages {
    stage('Setup') {
      steps { sh 'python3 -m venv .venv && .venv/bin/pip install --quiet pytest' }
    }
    stage('Test') {
      steps { sh '.venv/bin/pytest -v' }
    }
  }
}

