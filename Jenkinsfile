pipeline {
    agent any

    environment {
        IMAGE_NAME = "day8-python-app"
        IMAGE_TAG = "v1"
    }

    stages {

        stage('Clean Workspace') {
            steps {
                echo 'Cleaning old workspace...'
                deleteDir()
            }
        }

        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ./app"
            }
        }

        stage('Deploy Application') {
            steps {
                echo 'Deploying with Docker Compose...'
                sh 'docker compose down'
                sh 'docker compose up -d --build'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}
