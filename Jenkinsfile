pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning the repository...'
                git 'https://github.com/sohelmohammed0/devguide.git'  // replace with your repository URL
		git credentialsId: 'Git-creds', url: 'https://github.com/sohelmohammed0/devguide.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker image...'
                    docker.build('sohelqt8797/flask-app')i
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    echo 'Pushing Docker image to Docker Hub...'
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                        docker.image('sohelqt8797/flask-app').push()
                    }
                }
            }
        }
    }
}


