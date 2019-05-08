//import hudson.model.*;
//GitCredentials='Gitcred'
//ExcludedGitTags=['Latest','Development','QA','Production']
pipeline {
    agent any 
    stages {
        stage('build image') 
        
        {
            steps{
        sh'sudo docker build -t newproj .'
        }
    }
        stage('run image') 
        {
            steps{
                 sh'sudo docker run -it -d --name newproj12 newproj'
                 }
        }
        stage('kubernetes Deploy')
        {
            steps{
                kubernetesDeploy configs: '/home/administrator/.minikube/config', kubeConfig: [path: ''], kubeconfigId: 'kubecon', secretName: '', ssh: [sshCredentialsId: '*', sshServer: ''], textCredentials: [certificateAuthorityData: '', clientCertificateData: '', clientKeyData: '', serverUrl: 'https://']
                 }
        }
    }}
