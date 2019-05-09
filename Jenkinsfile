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
        /*stage('run image') 
        {
            steps{
                 sh'docker run -it -d --name newproj12a5 newproj'
                
                 }
        }*/
       
            
        stage('push image')
        {  // when {
             //     branch 'master'
               //  }
           /* script {
                 //withDockerServer([uri: "tcp://<my-docker-socket>"]) {
                 withDockerRegistry([credentialsId: 'dock_hub', url: ""]) {
            // we give the image the same version as the .war package
                def image = docker.build("<myDockerRegistry>/<myDockerProjectRepo>:${branchVersion}", "--build-arg PACKAGE_VERSION=${branchVersion} ./tmp-docker-build-context")
                image.push()
        }*/
            steps{
                script{
              docker.withRegistry("",'dock_hub') 
                {
                 sh 'docker push tripathiakhila/newproj2:latest'
                }
            }
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
