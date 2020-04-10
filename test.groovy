badge = "nana-banana"


pipeline {
    agent any
    stages {
        stage('check ping to google') {
            steps {
                addBadge(icon: 'yellow.gif', text: badge)
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
                removeBadges()
                addBadge(icon: 'completed.gif', text: badge)
            }
        }
    }
}