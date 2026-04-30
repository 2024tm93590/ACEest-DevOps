pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/2024tm93590/ACEest-DevOps.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t aceest-fitness:v1 .'
            }
        }

    }
}