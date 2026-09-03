pipeline {
    agent any

    environment {
        IMAGE_NAME = "myapp"
        IMAGE_TAG = "${BUILD_NUMBER}"
        CONTAINER_NAME = "demo-container"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh '''
                    docker run -d \
                    -p 5000:5000 \
                    --name ${CONTAINER_NAME} \
                    ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }

        stage('Test Application') {
            steps {
                sh '''
                    sleep 5
                    curl -f http://localhost:5000
                '''
            }
        }
    }
}
