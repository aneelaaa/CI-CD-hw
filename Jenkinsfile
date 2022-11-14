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
           sh 'pwd'
        }


        }

   stage('runpy') {
        steps{      
          sh '~/Documents/PyTest_Homework/tests.py'
        }
        }
   stage('Create a new build') {
     steps {
       echo 'Deploying...'
     }
   }
  }
}
