//import hudson.model.*;
//GitCredentials='Gitcred'
//ExcludedGitTags=['Latest','Development','QA','Production']
    /* def createNamespace (namespace)
    {
    echo "Creating namespace ${namespace} if needed"
    sh "[ ! -z \"\$(kubectl get ns ${namespace} -o name 2>/dev/null)\" ] || kubectl create ns ${namespace}"
    }*/
/*def helmInstall (namespace, ID) {
    echo "Installing ${ID} in ${namespace}"

    script {
        release = "${release}-${namespace}"
        sh "helm repo add helm ${HELM_REPO}; helm repo update"
        sh """
            helm upgrade --install --namespace ${namespace} ${release} \
                --set imagePullSecrets=${IMG_PULL_SECRET} \
                --set image.repository=${DOCKER_REG}/${IMAGE_NAME},image.tag=${DOCKER_TAG} helm/acme
        """
        sh "sleep 5"
    }
}
*/

pipeline {
    
    environment{
     registry_url = "https://cloud.docker.com/repository/docker/tripathiakhila/kubeim" // Docker Hub
     docker_creds_id = "dock_hub" // name of the Jenkins Credentials ID
     build_tag = "latest"
    }
     parameters {
        string (name: 'GIT_BRANCH',           defaultValue: 'master',  description: 'Git branch to build')
        booleanParam (name: 'DEPLOY_TO_PROD', defaultValue: false,     description: 'If build and tests are good, proceed and deploy to production without manual approval')
                }
    agent any 
    stages {
        stage('build image') 
        {
          steps{
                sh'docker build -t tripathiakhila/kubeim:latest .'
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
        stage('Helm test')
        {
            // run helm chart linter
            helmLint(chart_dir)

        }
        stage('Deploy to dev') {
            steps {
                script {
                    namespace = 'development'
                    ID = "tripathiakhila/kubeim:latest"
                    echo "Deploying application ${ID} to ${namespace} namespace"
                   // createNamespace (namespace)

                    // Remove release if exists
                    //helmDelete (namespace, "${ID}")

                    // Deploy with helm
                    echo "Deploying"
                    helmInstall(namespace, "${ID}")
                }
            }
        }

       stage('kubernetes Deploy')
        {
           steps{
                 echo "running kubectl test"
                 sh "kubectl get nodes"
                 kubernetesDeploy configs: '**/Deployment.yaml', kubeConfig: [path: ''], kubeconfigId: 'kube_con', secretName: '', ssh: [sshCredentialsId: '*', sshServer: ''], textCredentials: [certificateAuthorityData: '', clientCertificateData: '', clientKeyData: '', serverUrl: 'https://']
                 //kubectl --kubeconfig=("/home/administrator/.kube get ns development || kubectl --kubeconfig=/home/administrator/.kube  create ns development")      
                }
        }
    }
}
