pipeline {
    agent any

    stages {

        stage('Check Files') {
            steps {
                sh 'ls'
            }
        }

        stage('Setup Virtual Env') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest
                '''
            }
        }

    }
}