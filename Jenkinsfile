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
            steps {
              script {
                  def tag = params.ROLLBACK_TAG?.trim() ? params.ROLLBACK_TAG : IMAGE_TAG
                  echo "Deploying image: ${tag}"
              
                  sshagent(['ec2-ssh-key']) {

                    sh """
                    ssh -o StrictHostKeyChecking=no ubuntu@13.126.44.170 "
                    docker pull ${IMAGE_NAME}:${tag}
                    docker stop app || true 
                    docker rm app || true 
                    docker run -d -p 5000:5000 --name app ${IMAGE_NAME}:${tag}
                    docker image prune -f
                    "
                    """
                }
            }
        }
    }
}

stage('Application Health Check'){
    steps {
        echo "Checking if application is running..."

        sh '''
        sleep 10
        curl -f http://13.232.240.89:5000 || exit 1
        '''
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


