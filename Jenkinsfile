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
          withCredentials([usernamePassword(
             credentialsId: 'dockerhub-creds',
             usernameVariable: 'DOCKER_USER',
             passwordVariable: 'DOCKER_PASS'
        )]) {
            sh '''
            docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ./app
            echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
            docker push ${IMAGE_NAME}:${IMAGE_TAG}
            '''
        }
    }
}

        stage('Deploy Application') {
            steps {
                echo 'Deploying container from Docker Hub image...'
                sh 'docker pull ${IMAGE_NAME}:${IMAGE_TAG}'
                sh 'docker compose down'
                sh 'docker compose up -d'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs....'
        }
    }
}
