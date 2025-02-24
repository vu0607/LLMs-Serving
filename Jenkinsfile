pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Running tests...'
                }
            }
        stage('Test') {
            steps {
                echo 'Building image for deployment...'
                }
            }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline success'
        }
        failure {
            echo 'Pipeline Failure'
        }
    }

}