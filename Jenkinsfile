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

        stage("Setup dockercontainer"){
            agent {
                docker {
                    image 'python:3' 
                    args -v '$WORKSPACE:/workspace -w /workspace'
                }
            }
            steps{
                sh './prepare.sh'
                sh 'python calc.py'
            }
        }

        stage("Show results"){
            steps{
                sh 'cat result.txt'
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