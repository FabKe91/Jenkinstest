
pipeline {

    agent any

    stages {
        stage('Test') {
            steps {
                echo "Running Test"
                echo "on ${env.BUILD_ID} on ${env.JENKINS_URL}"
                robot transaction_testsuite.robot
            }
        }
    }
}




