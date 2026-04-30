pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Check Files') {
            steps {
                sh 'ls'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install pytest'
            }
        }

        stage('Run Pytest') {
            steps {
                sh 'python3 -m pytest'
            }
        }

    }
}