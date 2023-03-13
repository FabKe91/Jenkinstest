
pipeline {

    agent any

    stages {
        stage('Test') {
            steps {
                echo "Running Test"
                echo "on ${env.BUILD_ID} on ${env.JENKINS_URL}"
                sh '/Users/Fabian.Keller/Library/Python/3.9/bin/robot transaction_testsuite.robot'
            }
        }
    }
}




