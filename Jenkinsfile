//import hudson.model.*;
//GitCredentials='Gitcred'
//ExcludedGitTags=['Latest','Development','QA','Production']
pipeline {
    agent any 
    stages {
        stage('build image') 
        
        {
        sh'docker build -t hh .'
        }
    }
}

