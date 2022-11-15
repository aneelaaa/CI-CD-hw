pipeline {
   agent any

   stages {
      stage('Build') {
        steps {
           echo 'Building...'
           echo "Running ${env.BUILD_ID} ${env.BUILD_DISPLAY_NAME} on ${env.NODE_NAME} and JOB ${env.JOB_NAME}"
        }
      }
      stage('Run sample.py') {
        steps{
           sh "dir ${JENKINS_HOME}"
           sh "python sample.py"
        }
      }
      stage('Run test.py') {
         steps {
            echo 'Launching simple test...'
            sh "python --version"
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
