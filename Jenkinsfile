pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'sohelqt8797/flask-app:latest' // Update this to match your Docker image name
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout the correct branch
                git branch: 'main', url: 'https://github.com/sohelmohammed0/devguide.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    // Push the Docker image to Docker Hub with credentials
                    docker.withRegistry('https://registry.hub.docker.com', 'DOCKER_HUB_CREDENTIALS') {
                        sh 'docker push $DOCKER_IMAGE'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Deploy the Docker image
                    sh 'docker pull $DOCKER_IMAGE'
                    sh 'docker stop flask-container || true'  // Stop the container if it is already running
                    sh 'docker rm flask-container || true'     // Remove the container if it exists
                    sh 'docker run -d --name flask-container -p 80:80 $DOCKER_IMAGE'
                }
            }
        }
    }
}

