//import hudson.model.*;
//GitCredentials='Gitcred'
//ExcludedGitTags=['Latest','Development','QA','Production']
pipeline {
    agent {
        docker
    
    stages {
        stage('Test') {
            steps {
                sh 'docker build -t image .'
            }
        }
    }
}
}
