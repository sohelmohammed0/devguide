pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'sohelqt8797/flask-app'
    }
    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository using the specified branch and credentials
                git branch: 'main', url: 'https://github.com/sohelmohammed0/devguide.git', credentialsId: 'Github-PAT2'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image with a specified tag
                    docker.build("${DOCKER_IMAGE}:latest")
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'Dockerhub-PAT', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    script {
                        // Log in to Docker Hub
                        sh 'echo "$DOCKERHUB_PASS" | docker login -u "$DOCKERHUB_USER" --password-stdin'
                        // Push the Docker image
                        docker.image("${DOCKER_IMAGE}:latest").push()
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Pull the latest image and restart the container
                    sh 'docker pull ${DOCKER_IMAGE}:latest'
                    sh 'docker stop your_flask_container || true && docker rm your_flask_container || true'
                    sh 'docker run -d --name your_flask_container -p 80:5000 ${DOCKER_IMAGE}:latest'
                }
            }
        }
    }
    post {
        always {
            // Clean up any dangling images after deployment
            sh 'docker image prune -f'
        }
    }
}
