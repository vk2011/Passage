pipeline{
    agent any
    
    stages{
        stage ("checkout"){
            steps{
                git branch: "main", url: "https://github.com/vk2011/Passage.git", credentialsId: "git-credentials"
            }
        }
        stage ("build stage"){
            steps{

                sh "docker-compose -f docker-compose.yml -p passage build "
            }
        }
        stage ("deploy stage"){
            steps{

                sh "docker-compoes -f docker-compose.yml -p passage up -d"
            }
        }
    }
}