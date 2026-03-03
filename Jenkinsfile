pipeline {
    agent any

    environment {
        IMAGE_NAME = "sujithachadalavada/day8-python-app"
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

     stage('Build & Push Image') {
      steps {
        script {
            docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-creds') {
                def appImage = docker.build("${env.IMAGE_NAME}:${env.IMAGE_TAG}", "./app")
                appImage.push()
            }
        }
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
