//import hudson.model.*;
//GitCredentials='Gitcred'
//ExcludedGitTags=['Latest','Development','QA','Production']
pipeline {
    agent any 
    stages {
        stage('build image') 
        
        {
            steps{
        sh'docker build -t newproj .'
        }
    }
        stage('run image') 
        {
            steps{
                 sh'docker run -it -d --name newproj12 newproj'
                 }
        }
        stage('kubernetes Deploy')
        {
            steps{
                kubernetesDeploy configs: '', dockerCredentials: [[credentialsId: 'dock_hub', url: 'https://cloud.docker.com/repository/docker/tripathiakhila/newproj2']], kubeConfig: [path: ''], kubeconfigId: 'kubecon', secretName: '', ssh: [sshCredentialsId: '*', sshServer: ''], textCredentials: [certificateAuthorityData: '', clientCertificateData: '', clientKeyData: '', serverUrl: 'https://']
                 }
        }
    }}
