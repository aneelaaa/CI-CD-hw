pipeline {
   agent any

   stages {
      stage('Builing param') {
        steps {
           echo 'Building...'
           echo "Running ${env.BUILD_ID} ${env.BUILD_DISPLAY_NAME} on ${env.NODE_NAME} and JOB ${env.JOB_NAME}"
        }
      }
      stage('List home dir') {
        steps{
           sh "dir ${JENKINS_HOME}"
        }
      }
      stage('Run test.py') {
         steps {
            echo 'Launching simple test...'
            sh "pytest test.py"
         }
      }
      stage('Deploy') {
         steps {
            echo 'Deploying...'
         }
      }
   }
} 
