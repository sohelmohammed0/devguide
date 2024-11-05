pipeline {
    agent any

    environment {
        IMAGE_NAME = "sohelqt8797/flask_app"
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
                    sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'Dockerhub-PAT') {
                        sh 'docker push ${IMAGE_NAME}:${BUILD_NUMBER}'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'docker stop flask_app || true'
                    sh 'docker rm flask_app || true'
                    sh 'docker run -d --name flask_app -p 5000:5000 ${IMAGE_NAME}:${BUILD_NUMBER}'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
