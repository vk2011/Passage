pipeline{
    agent any
    
    stages{
        stage ("checkout"){
            steps{
                git branch: "main", url: "https://github.com/vk2011/Passage.git", credentialsId: "git-credentials"

                echo "git pull successful"
            }
        }
        stage ("build stage"){
            steps{
                bat "docker --version"
                bat "docker-compose --version"
                bat "docker-compose -f docker-compose.yml -p passage build "
            }
        }
        stage ("deploy stage"){
            steps{

                bat "docker-compose -f docker-compose.yml -p passage up -d"
            }
        }
    }
}