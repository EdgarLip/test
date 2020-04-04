pipeline {
    agent any
//     options {
//         skipStagesAfterUnstable()
//     }
    stages {
        stage('check ping to google') {
            steps {
                sh 'ping 8.8.8.8'
                junit 'reports/**/*.xml'
            }
        }
        stage('check working dir'){
            steps {
                sh 'pwd'
            }
        }
        stage('run python script ') {
            steps {
                sh 'python3 hello_world.py'
            }
        }
    }
}