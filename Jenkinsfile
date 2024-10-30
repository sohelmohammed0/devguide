pipeline {
    agent any 

    environment {
        VENV_PATH = 'venv'  // Define the path for the virtual environment
    }

    stages {
        stage('Set up Python Environment') {
            steps {
                // Create a Python virtual environment
                sh 'python3 -m venv ${VENV_PATH}'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Activate the virtual environment and install dependencies
                sh '''
                . ${VENV_PATH}/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Activate the virtual environment and run tests
                sh '''
                . ${VENV_PATH}/bin/activate
                pytest
                '''
            }
        }

        stage('Build and Deploy') {
            steps {
                // Placeholder for build and deployment steps
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
