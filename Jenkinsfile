pipeline {
    agent any

    stages {

        stage('Check Files') {
            steps {
                sh 'ls'
            }
        }

        stage('Run Tests in Docker') {
            steps {
                sh '''
                docker run --rm -v $(pwd):/app -w /app python:3.10 \
                sh -c "pip install pytest && pytest"
                '''
            }
        }

    }
}