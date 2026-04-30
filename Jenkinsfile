pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {

        stage('Check Files') {
            steps {
                sh 'ls'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install pytest'
            }
        }

        stage('Run Pytest') {
            steps {
                sh 'pytest'
            }
        }

    }
}