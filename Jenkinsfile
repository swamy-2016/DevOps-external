pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        echo 'Building the application...'
      }
    }

    stage('Test') {
      steps {
        bat 'py -m venv .venv'
        bat '.venv\\Scripts\\python -m pip install -r requirements.txt'
        bat '.venv\\Scripts\\python -m pytest -q'
      }
    }

    stage('Deploy') {
      steps {
        echo 'No deployment configured; this stage is a placeholder.'
      }
    }
  }
}