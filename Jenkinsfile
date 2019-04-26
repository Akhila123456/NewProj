//import hudson.model.*;
//GitCredentials='Gitcred'
//ExcludedGitTags=['Latest','Development','QA','Production']
def CommitHash
def BranchName

pipeline{
     agent{
        dockerfile true
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
    // sh"docker -v"  
     sh"docker build - < Dockerfile"
     sh"docker run"    
     echo "its done"
   }  
    } 
   }
}  
