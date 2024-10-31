pipeline {
    agent any
    i
    environment {
        DOCKER_IMAGE = 'sohelqt8797/flask-app:latest' // Update this to match your Docker image name
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/sohelmohammed0/devguide.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'DOCKER_HUB_CREDENTIALS') {
                        sh 'docker push $DOCKER_IMAGE'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'docker pull $DOCKER_IMAGE'
                    sh 'docker stop flask-container || true'
                    sh 'docker rm flask-container || true'
                    sh 'docker run -d --name flask-container -p 80:80 $DOCKER_IMAGE'
                }
            }
        }
    }
}

