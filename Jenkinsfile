pipeline {
   agent any

   stages {
      stage('Build') {
        steps {
           echo 'Building...'
           echo "Running ${env.BUILD_ID} ${env.BUILD_DISPLAY_NAME} on ${env.NODE_NAME} and JOB ${env.JOB_NAME}"
        }
      }
      stage('List') {
        steps{
           sh "dir ${JENKINS_HOME}"
        }
      }
      stage('Test') {
         steps {
            echo 'Launching simple test...'
            sh "pytest test.py"
         }
      }
      stage('Deploy') {
         steps {
            echo 'Deploying...'
            sh "git checkout release"
       
            sh "git merge origin/main"
           
            sh "git status"
            sh "git push https://aneelaaa:iRKF2Lvx2qAyuma@github.com/aneelaaa/CI-CD-hw.git origin/release"
         }
      }
   }
} 
