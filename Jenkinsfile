pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'sohelqt8797/flask-app'
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
                    docker.build("${DOCKER_IMAGE}:latest")
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'Dockerhub-PAT', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    script {
                        docker.image("${DOCKER_IMAGE}:latest").push()
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                // Example step to deploy on your server or cloud provider
                sh 'docker pull ${DOCKER_IMAGE}:latest'
                sh 'docker stop your_flask_container || true && docker rm your_flask_container || true'
                sh 'docker run -d --name your_flask_container -p 80:5000 ${DOCKER_IMAGE}:latest'
            }
        }
    }
}
