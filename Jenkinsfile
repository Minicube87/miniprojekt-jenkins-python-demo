pipeline{
    agent any

    stages{
        stage("Clean before build"){
            steps{
                sh "rm -rf ./*"
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage("Execute shell script"){
            steps{
                sh './prepare.sh'
            }
        }

        // DOcker container sind isolierte dh 
        // todo workspace ordner verknüpfen
        // bei args irgentwie
        stage("Setup dockercontainer"){
            agent {
                docker {
                    image 'python:3.10' 
                    args '-v ${pwd()}:/'
                }
            }
            steps{
                sh 'python calc.py'
            }
        }

        stage("Show results"){
            steps{
                sh 'cat results.txt'
            }
        }    

    }
    post{
        always{
            echo "ALWAYS"
        }
        success{
            sh "rm -rf ./*"
        }
        failure{
           echo "FAILURE"
        }
    }
}