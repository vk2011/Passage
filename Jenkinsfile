pipeline{
    agent any
    
    stages{
        stage ("checkout"){
            steps{
                git branch: "main", url: "https://github.com/vk2011/Passage.git", credentialsId: "git-credentials"
            }
        }
        stage{
            steps("build stage"){

                sh "docker-compose -f docker-compose.yml -p passage build "
            }
        }
        stage{
            steps("deploy stage"){

                sh "docker-compoes -f docker-compose.yml -p passage up -d"
            }
        }
    }
}