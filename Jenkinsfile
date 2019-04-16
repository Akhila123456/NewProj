

GitCredentials='Gitcred'
ExcludedGitTags=['Latest','Development','QA','Production']
def CommitHash
def BranchName

node
{
   stage(SCM Checkout)
     {
         echo "Checking out code"
         checkout scm
         echo "Getting git commit hash..."
         CommitHash=
            returnStdout: true,
            script:'git rev-parse --verify --short HEAD'
      }
      stage("Build Image")
      {
            echo "Building docker image"
            docker build -t ${ImageTag} -f Dockerfile -t latest --label commit-hash=\"${CommitHash}\"
                 
      }   
     
     
}







