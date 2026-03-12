pipeline {
     agent any

    parameters {
        string(name: 'ROLLBACK_TAG', defaultValue: '', description: 'Enter Docker image tag to rollback (example: build-24)')
    }

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
            when {
                expression { params.ROLLBACK_TAG?.trim() }
            }

            steps {
                echo "Rolling back to version: ${params.ROLLBACK_TAG}"

                sshagent(['ec2-ssh-key']) {

                    sh """
                    ssh -o StrictHostKeyChecking=no ubuntu@13.201.66.185 "
                    docker pull ${IMAGE_NAME}:${params.ROLLBACK_TAG} &&
                    docker stop app || true &&
                    docker rm app || true &&
                    docker run -d -p 5000:5000 --name app ${IMAGE_NAME}:${params.ROLLBACK_TAG} &&
                    docker image prune -f
                    "
                    """
                }
            }
        }
    }

    post {
    success {
        emailext(
            to: 'chadalavadasujitha8@gmail.com',
            subject: "Jenkins Build SUCCESS #${BUILD_NUMBER}",
            body: """
Build SUCCESS

Job: ${JOB_NAME}
Build Number: ${BUILD_NUMBER}
URL: ${BUILD_URL}
"""
        )
    }
    failure {
        emailext(
            to: 'chadalavadasujitha8@gmail.com',
            subject: "Jenkins Build FAILED #${BUILD_NUMBER}",
            body: "Build failed. Check Jenkins logs."
        )
    }
}
}


