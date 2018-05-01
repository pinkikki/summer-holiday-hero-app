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
                    image 'blurrcat/alpine-python-psycopg2:1.0'
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
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