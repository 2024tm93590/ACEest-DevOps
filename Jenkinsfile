pipeline {
    agent any

    stages {

        stage('Check Files') {
            steps {
                sh 'ls'
            }
        }

        stage('Install Python & Pip') {
            steps {
                sh '''
                apt-get update
                apt-get install -y python3 python3-pip
                '''
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