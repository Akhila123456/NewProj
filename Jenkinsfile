GitCredentials='Gitcred'
ExcludedGitTags=['Latest','Development','QA','Production']
def CommitHash
def BranchName
pipeline{
     agent {
          dockerfile true
     }
     stage(SCM Checkout)
     {
         echo "Checking out code"
         checkout scm
         echo "Getting git commit hash..."
         /*CommitHash=
            returnStdout: true,
           script:'git rev-parse --verify --short HEAD'*/
      }
   stage("Build Image")
   {
     echo "Building docker image"
     docker -v       
     docker build  -< Dockerfile
    }   
  }
