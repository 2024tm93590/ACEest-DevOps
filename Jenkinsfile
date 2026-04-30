pipeline {
    agent any

    stages {

        stage('Check Files') {
            steps {
                sh 'ls'
            }
        }

        stage('Simulate Test Execution') {
            steps {
                sh '''
                echo "Running unit tests..."
                echo "All test cases passed successfully"
                '''
            }
        }

    }
}