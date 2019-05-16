//import hudson.model.*;
//GitCredentials='Gitcred'
//ExcludedGitTags=['Latest','Development','QA','Production']
def kubectlTest() {
    // Test that kubectl can correctly communication with the Kubernetes API
    echo "running kubectl test"
    sh "kubectl get nodes"

}
def helmDeploy(Map args) {
    //configure helm client and confirm tiller process is installed

    if (args.dry_run) {
        println "Running dry-run deployment"

        sh "/usr/local/bin/helm upgrade --dry-run --debug --install ${args.name} ${args.chart_dir} --set ImageTag=${args.tag},Replicas=${args.replicas},Cpu=${args.cpu},Memory=${args.memory},DomainName=${args.name} --namespace=${args.name}"
    } else {
        println "Running deployment"
        sh "/usr/local/bin/helm upgrade --install ${args.name} ${args.chart_dir} --set ImageTag=${args.tag},Replicas=${args.replicas},Cpu=${args.cpu},Memory=${args.memory},DomainName=${args.name} --namespace=${args.name}"

        echo "Application ${args.name} successfully deployed. Use helm status ${args.name} to check"
    }
}


pipeline {
    //def app;
     registry_url = "https://cloud.docker.com/repository/docker/tripathiakhila/kubeim" // Docker Hub
    docker_creds_id = "dock_hub" // name of the Jenkins Credentials ID
    build_tag = "latest"
    agent any 
    stages {
        stage('build image') 
        {
          steps{
                sh'docker build -t tripathiakhila/kubeim:latest .'
              }
            script{
                    def pwd= pwd()
                    def chart_dir = "${pwd}/charts/newegg-nginx"            
            }  
        }
       /* stage('run image') 
        {
            steps{
                 sh'docker run -it -d --name kubecon4 tripathiakhila/kubeim'
                
                 }
        }*/
       
            
        /*stage('push image')
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
                 sh 'docker push tripathiakhila/kubeim:latest'
                }
            }
        }
        }*/
       stage('kubernetes Deploy')
        {
           steps{
                 kubernetesDeploy configs: '**/Deployment.yaml', kubeConfig: [path: ''], kubeconfigId: 'kube_con', secretName: '', ssh: [sshCredentialsId: '*', sshServer: ''], textCredentials: [certificateAuthorityData: '', clientCertificateData: '', clientKeyData: '', serverUrl: 'https://']
                 //kubectl --kubeconfig=("/home/administrator/.kube get ns development || kubectl --kubeconfig=/home/administrator/.kube  create ns development")      
                }
        }
    }
}
