pipeline {
    agent any
    
    environment {
        // Replace these with your Docker credentials and image name
        DOCKER_CREDENTIALS_ID = 'Dockerhub-PAT'
        DOCKER_IMAGE = 'sohelqt8797/flask-app'
    }
    
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/sohelmohammed0/devguide.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    docker.build("${DOCKER_IMAGE}:${env.BUILD_ID}")
                }
            }
        }
        
        stage('Push Docker Image') {
            steps {
                script {
                    // Login and push to Docker Hub or other registry
                    docker.withRegistry('', "${DOCKER_CREDENTIALS_ID}") {
                        docker.image("${DOCKER_IMAGE}:${env.BUILD_ID}").push()
                        docker.image("${DOCKER_IMAGE}:${env.BUILD_ID}").push("latest")
                    }
                }
            }
        }
        
        stage('Deploy') {
            steps {
                // Deploy the container (e.g., using Kubernetes or Docker Compose)
                echo "Deploying the application..."
                // Here, you could integrate Kubernetes deployment commands or Docker Compose
                // Example: sh 'kubectl apply -f k8s-deployment.yaml'
            }
        }
    }
    
    post {
        success {
            echo "Build, push, and deployment successful!"
        }
        failure {
            echo "Build, push, or deployment failed."
        }
    }
}
