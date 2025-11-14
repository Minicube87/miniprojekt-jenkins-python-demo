pipeline{
    agent{
        label any
    }
    stages{
        stage("Clean before build"){
            steps{
                sh "rm -rf ./*"
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
                    image 'python:3.10' 
                    args '-u'
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