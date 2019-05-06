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
                 sh'docker run -it -d --name newproj1 newproj'
                 }
        }
        /*stage('kubernetes Deploy')
        {
            steps{
                kubernetesDeploy configs: '/home/administrator/.kube', kubeConfig: [path: ''], kubeconfigId: 'kubecon', secretName: '', ssh: [sshCredentialsId: '*', sshServer: ''], textCredentials: [certificateAuthorityData: '', clientCertificateData: '', clientKeyData: '', serverUrl: 'https://']
                 }
        }*/
    }}
