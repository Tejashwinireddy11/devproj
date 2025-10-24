pipeline{
    agent any
    stages{
        stage ("Build Docker Image"){
            steps{
                echo "Build Docker Image"
                bat "docker build -t plantcare:v1 ."
            }
        }
        stage ("Docker Login"){
            steps{
                bat "docker login -u tejashwini1108 -p Tejashwini@1108"
            }
        }
        stage("push Docker Iamge to Docker Hub"){
            steps {
                echo "push Docker Image to docker hub"
                bat "docker tag plantcare:v1 tejashwini1108/devproj:t8"
                bat "docker push tejashwini1108/devproj:t8"


            }
        }
        stage("Deploy to Kubernetes"){
            steps{
                bat "kubectl apply -f deployment.yaml --validate=false"
                bat "kubectl apply -f service.yaml"
            }
        }
        stage('Restart Deployment') {
            steps {
                echo "Restarting Deployment to pick up new image..."
                bat "kubectl rollout restart deployment/plantcare-deployment"
            }
        }
    }
    post{
        success{
            echo 'Pipeline completed scucessfull!'

        }
        failure{
            echo "Pipeline failed.Please check the logs."
        }
    }
}