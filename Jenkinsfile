 pipeline {
   agent any
   stages {
     stage('build') {
       steps {
         echo 'Building weather image..'
         sh 'docker build -t weather-images WeatherApp/.'
       }
     }
     stage('push') {
       steps {
         echo 'Creating image tag..'
         sh 'docker tag weather-images:latest 532706939733.dkr.ecr.eu-central-1.amazonaws.com/weather-images:latest'
         echo 'Pushing image to ECR..'
         sh 'docker push 532706939733.dkr.ecr.eu-central-1.amazonaws.com/weather-images:latest'
       }
     }

     stage('deploy to eks') {
       steps {
         sshagent(credentials: ['eks_cred']) {
           echo 'Deploying..'
           sh 'ssh ubuntu@ec2-54-93-91-47.eu-central-1.compute.amazonaws.com "kubectl rollout restart deployment weather"'
         }
       }
     }
   }
 }
