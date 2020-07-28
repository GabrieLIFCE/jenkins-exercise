pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh '/usr/local/bin/pip install pytest'
            }
        }
        stage('Unit test') {
            steps {
                sh 'pystest'
            } 
        }
    }
}