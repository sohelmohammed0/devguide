pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'sohelqt8797/flask-app'
        DOCKER_CREDENTIALS = 'dockerhub-credentials' // Create and use a Docker ID in Jenkins credentials
        GIT_REPO = 'https://github.com/sohelmohammed0/devguide.git'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: "${GIT_REPO}", branch: 'main'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:latest")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', "${DOCKER_CREDENTIALS}") {
                        docker.image("${DOCKER_IMAGE}:latest").push()
                    }
                }
            }
        }
        
        stage('Deploy to Server') {
            steps {
                // Replace this with actual SSH or deployment steps
                sh 'docker pull your-dockerhub-username/your-image-name:latest'
                sh 'docker stop your-container-name || true'
                sh 'docker rm your-container-name || true'
                sh 'docker run -d --name your-container-name -p 80:80 your-dockerhub-username/your-image-name:latest'
            }
        }
    }
    
    post {
        always {
            cleanWs() // Cleans workspace after job
        }
    }
}

