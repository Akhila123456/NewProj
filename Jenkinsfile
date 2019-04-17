//import hudson.model.*;
GitCredentials='Gitcred'
ExcludedGitTags=['Latest','Development','QA','Production']
def CommitHash
def BranchName
pipeline{
     agent{
         Dockerfile true
     }
     stages{
     stage("SCM Checkout")
     {
       steps{
         echo "Checking out code"
         checkout scm
         echo "Getting git commit hash..."
         /*CommitHash=
            returnStdout: true,
           script:'git rev-parse --verify --short HEAD'*/
          }
      }
   stage("Build Image")
   { 
    steps{
     echo "Building docker image"
     //docker -v  
 
   // sh "sudo docker build -t  testing ."
   // echo "its done"
                
         
    }  
    } 
   }
}  
