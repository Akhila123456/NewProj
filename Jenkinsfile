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
                sh'docker build -t kubeim:latest .'
              
               }
        }
        /*stage('run image') 
        {
            steps{
                 sh'docker run -it -d --name kubecon1 kubeim'
                
                 }
        }*/
       
            
        stage('push image')
        {  // when {
             //     branch 'master'
               //  }
           // script {
                 //withDockerServer([uri: "tcp://<my-docker-socket>"]) {
                // withDockerRegistry([credentialsId: 'dock_hub', url: ""]) {
            // we give the image the same version as the .war package
               // def image = docker.build("<myDockerRegistry>/<myDockerProjectRepo>:${branchVersion}", "--build-arg PACKAGE_VERSION=${branchVersion} ./tmp-docker-build-context")
              //  image.push()
        //}
            steps{
                script{
              docker.withRegistry("",'dock_hub') 
                {
                 sh 'docker push tripathiakhila/newproj2:latest'
                }
            }
        }
        }
       stage('kubernetes Deploy')
        {
           steps{
                 kubernetesDeploy configs: '**/*.yaml', kubeConfig: [path: ''], kubeconfigId: 'kube_con', secretName: '', ssh: [sshCredentialsId: '*', sshServer: ''], textCredentials: [certificateAuthorityData: '', clientCertificateData: '', clientKeyData: '', serverUrl: 'https://']
                 //kubectl --kubeconfig=("/home/administrator/.kube get ns development || kubectl --kubeconfig=/home/administrator/.kube  create ns development")      
                }
        }
    }
}
