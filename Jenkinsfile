
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
    post {
        always {
           step([$class: 'XrayImportBuilder', endpointName: '/robot', importInParallel: 'false', importToSameExecution: 'false', serverInstance: 'CLOUD-dc5f9784-d685-4454-84cb-d2870c8c7e54'])
        }
    
    }
}




