badge = "nana-banana"
ping_dest = env.PING_DEST

pipeline {
    agent any
    stages {
        stage('check ping to google') {
            steps {
                addBadge(icon: 'yellow.gif', text: badge)
                script {
                    for(int i=0; i<2 ;i++) {
                        sh "ping ${ping_dest} -c 5"
                    }
                }
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