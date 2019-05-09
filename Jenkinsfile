//import hudson.model.*;
//GitCredentials='Gitcred'
//ExcludedGitTags=['Latest','Development','QA','Production']
pipeline {
    //def app;
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
                 sh'docker run -it -d --name newproj12@ newproj'
                
                 }
        }
       
            
        stage('push image')
        {  // when {
             //     branch 'master'
               //  }
            
            steps{
              //docker.withRegistry('git_cred','https://cloud.docker.com/repository/docker/tripathiakhila/newproj2') 
                //{
               sh 'docker push newproj:latest'
                 //}
            }
        }
       //stage('kubernetes Deploy')
        //{
           // steps{
              //  kubernetesDeploy configs: '<path id="absolute.path.id">     <fileset dir="/home/administrator/.kube">         <include name="config"/>     </fileset> </path> <property name="absolute.path" value="${toString:absolute.path.id}" /> <echo>file absolute path: ${absolute.path}</echo>', dockerCredentials: [[credentialsId: 'dock_hub', url: 'https://cloud.docker.com/repository/docker/tripathiakhila/newproj2']], kubeConfig: [path: ''], kubeconfigId: 'kubecon', secretName: '', ssh: [sshCredentialsId: '*', sshServer: ''], textCredentials: [certificateAuthorityData: '', clientCertificateData: '', clientKeyData: '', serverUrl: 'https://']
                // }
        //}
    }
}
