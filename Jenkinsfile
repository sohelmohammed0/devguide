pipeline {
    agent any

    environment {
        VENV_PATH = "${WORKSPACE}/venv"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/sohelmohammed0/devguide.git'
            }
        }
        stage('Set up Python Environment') {
            steps {
                sh 'python3 -m venv $VENV_PATH'
                sh 'source $VENV_PATH/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'source $VENV_PATH/bin/activate && pytest'
            }
        }
        stage('Build and Deploy') {
            steps {
                script {
                    sh 'source $VENV_PATH/bin/activate && python app.py'
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment Successful!'
        }
        failure {
            echo 'Build Failed!'
        }
    }
}

