//import hudson.model.*;
//GitCredentials='Gitcred'
//ExcludedGitTags=['Latest','Development','QA','Production']
pipeline {
    agent any 
    stages {
        stage('build image') 
        
        {
            steps{
        sh'docker build -t hh .'
        }
    }
        stage('run image') 
        
        {
            steps{
        sh'docker run -it -d --name app hh'
        }
    }
    }}
