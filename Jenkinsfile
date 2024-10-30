pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository
                git url: 'https://github.com/sohelmohammed0/devguide.git', credentialsId: 'Git-creds'
            }
        }
        
        stage('Set up Python Environment') {
            steps {
                // Create and activate the virtual environment using a dot (.) instead of source
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                // Run tests
                sh '''
                    . venv/bin/activate
                    python -m unittest discover -s tests
                '''
            }
        }
        
        stage('Build and Deploy') {
            steps {
                // Example deployment step
                sh '''
                    . venv/bin/activate
                    python deploy.py
                '''
            }
        }
    }
    
    post {
        failure {
            echo 'Build Failed!'
        }
        success {
            echo 'Build Succeeded!'
        }
    }
}

