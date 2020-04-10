badge = "nana-banana"


pipeline {
    agent any
    stages {
        stage('add_badge') {
            steps {
                addBadge(icon: 'completed.gif', text: badge)
            }
        }
        stage('check ping to google') {
            steps {
                sh 'ping 8.8.8.8 -c 5'
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