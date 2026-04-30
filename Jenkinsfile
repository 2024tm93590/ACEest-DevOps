pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/2024tm93590/ACEest-DevOps.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t washifa2024tm93590/aceest-fitness:v4.1 .'
            }
        }

        stage('Push Docker Image') {
            steps {
                bat 'docker push washifa2024tm93590/aceest-fitness:v4.1'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f k8s/deployment.yaml'
                bat 'kubectl apply -f k8s/service.yaml'
            }
        }
    }
}