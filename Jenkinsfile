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
            steps {
            sh"""
                docker run --rm \
                -v "$WORKSPACE":/app \
                -w /app \
                python:3.10 \
                python calc.py
            """
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