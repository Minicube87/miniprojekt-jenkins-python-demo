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
                stash name: 'numbers', includes: 'numbers.txt'
            }
        }

        stage("Setup dockercontainer"){
            agent {
                docker {
                    image 'python:3' 
                }
            }
            steps{
                unstash 'numbers'
                sh 'python calc.py'
                stash name: 'result', includes: 'result.txt'
            }
        }

        stage("Show results"){
            steps{
                unstash 'result'
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