
pipeline {
  agent any

  options {
    disableConcurrentBuilds()
    timeout(time: 15, unit: 'MINUTES')
  }

  stages {
    stage('Setup') {
      steps {
        sh 'python3 -m venv .venv && .venv/bin/pip install --quiet pytest pip-audit==2.10.1 semgrep==1.180.0'
      }
    }

    stage('Test') {
      steps {
        sh '.venv/bin/pytest --junitxml=report.xml'
      }
    }

    stage('Security') {
      parallel {
        stage('Secrets') {
          steps {
            sh 'gitleaks detect --source . --redact --no-banner'
          }
        }

        stage('SAST') {
          steps {
            sh '.venv/bin/semgrep scan --config .semgrep/rules.yml --error --metrics=off --exclude=.venv .'
          }
        }

        stage('Dependencies') {
          steps {
            sh '.venv/bin/pip-audit -r requirements.txt'
          }
        }
      }
    }

    stage('Secret demo') {
      steps {
        withCredentials([string(credentialsId: 'demo-token', variable: 'TOKEN')]) {
          sh 'echo "Token is set, length: ${#TOKEN}"'
          sh 'echo "$TOKEN"'
          sh 'echo "$TOKEN" | rev'
        }
      }
    }
  }

  post {
    always {
      junit allowEmptyResults: true, testResults: 'report.xml'
    }
  }
}
