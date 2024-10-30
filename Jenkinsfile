pipeline {
    agent any

    environment {
        // Docker credentials for pushing to Docker Hub
        DOCKER_HUB_CREDENTIALS = 'dockerhub-credentials'
        DOCKER_HUB_REPO = 'sohelqt8797/flask-app'
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository from GitHub
                git url: 'https://github.com/sohelmohammed0/devguide.git', credentialsId: 'Git-credentials'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t ${DOCKER_HUB_REPO}:latest .'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Login and push Docker image to Docker Hub
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_HUB_CREDENTIALS}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"
                        sh "docker tag ${DOCKER_HUB_REPO}:latest ${DOCKER_HUB_REPO}:latest"
                        sh "docker push ${DOCKER_HUB_REPO}:latest"
                    }
                }
            }
        }

        stage('Deploy Locally') {
            steps {
                script {
                    // Pull the latest Docker image and run the container locally
                    sh """
                    docker pull ${DOCKER_HUB_REPO}:latest
                    docker stop flask-app || true
                    docker rm flask-app || true
                    docker run -d --name flask-app -p 80:5000 ${DOCKER_HUB_REPO}:latest
                    """
                }
            }
        }
    }

    post {
        always {
            // Clean up workspace after job completes
            cleanWs()
        }
    }
}

