pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }
            steps {
                sh 'python -m compileall run.py app/'
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }
            steps {
                sh 'pip install -r test_requirements.txt'
                sh 'python -m pytest --verbose --cov --cov-report=html --junitxml=reports/result.xml'
            }
            post {
                always {
                    junit 'reports/result.xml'
                }
            }
        }
    }
}