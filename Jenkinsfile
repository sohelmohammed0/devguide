pipeline {
    agent any
    environment {
        VENV_PATH = "${env.WORKSPACE}/venv"
    }
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/sohelmohammed0/devguide.git', credentialsId: 'GitHub-token', branch: 'main'
            }
        }
        stage('Set up Python Environment') {
            steps {
                // Create and activate a Python virtual environment
                sh 'python3 -m venv ${VENV_PATH}'
                sh '. ${VENV_PATH}/bin/activate'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Ensure virtual environment is activated before installing dependencies
                sh '. ${VENV_PATH}/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Run tests in the activated environment
                sh '. ${VENV_PATH}/bin/activate && pytest'
            }
        }
        stage('Build and Deploy') {
            steps {
                // Add any build and deploy steps here
                echo 'Build and deployment steps go here'
            }
        }
    }
    post {
        success {
            echo 'Build Succeeded!'
        }
        failure {
            echo 'Build Failed!'
        }
    }
}

