pipeline {
     agent any
     triggers {
          pollSCM('* * * * *')
     }
     stages {
          stage("Unit test") {
               steps {
                    sh "./gradlew test"
               }
          }
    }
}