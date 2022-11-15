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
        sh "pip install xmlrunner"
        sh "ls -la"
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
