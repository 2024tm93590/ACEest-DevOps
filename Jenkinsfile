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
                bat 'dir'
            }
        }

        stage('Run Pytest') {
            steps {
                bat 'python -m pytest'
            }
        }

    }
}