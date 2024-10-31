pipeline {
    agent any
    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub') // Add Docker Hub credentials in Jenkins
        DOCKER_IMAGE = 'ohelqt8797flask-app'
    }
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/sohelmohammed0/devguide.git'
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
                // Example of deploying using Docker container restart
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

