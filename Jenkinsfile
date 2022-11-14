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
           echo 'List...'
        }


        }

   stage('runpy') {
        steps{      
          sh 'python PyTest_Homework/tests.py'
        }
        }
   stage('Create a new build') {
     steps {
       echo 'Deploying...'
     }
   }
  }
} 
