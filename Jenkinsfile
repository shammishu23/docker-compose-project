pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t day8-python-app ./app'
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
}
