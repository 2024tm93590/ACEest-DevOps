pipeline {
    agent any

    stages {

        stage('Check Files') {
            steps {
                sh 'ls'
            }
        }

        stage('Check Python') {
            steps {
                sh 'python --version || python3 --version'
            }
        }

        stage('Install Pytest (user mode)') {
            steps {
                sh 'python3 -m pip install --user pytest || python -m pip install --user pytest'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest || python -m pytest'
            }
        }

    }
}