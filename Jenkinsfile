pipeline {
    agent any

    environment {
        IMAGE_NAME = "sujithachadalavada/day8-python-app"
        IMAGE_TAG = "build-${BUILD_NUMBER}"
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

    stage('Deploy to EC2') {
        steps {
            sshagent(['ec2-ssh-key']) {
                sh '''
                ssh -o StrictHostKeyChecking=no ubuntu@13.232.197.6 << 'EOF'
                docker pull ${IMAGE_NAME}:${IMAGE_TAG}
                docker stop app || true
                docker rm app || true
                docker run -d -p 5000:5000 --name app ${IMAGE_NAME}:${IMAGE_TAG}
                docker image prune -f
                'EOF'
                '''
          }
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
