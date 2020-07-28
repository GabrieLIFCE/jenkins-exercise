pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'pip install pytest'
            }
        }
        stage('Unit test') {
            steps {
                sh 'pystest'
            } 
        }
    }
}