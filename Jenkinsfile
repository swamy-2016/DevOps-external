version: v1.0
pipeline:
  agent any
  stages:
    - stage: Build
      steps:
        - echo "Building the application..."
    - stage: Test
      steps:
        - echo "Running tests..."
        - sh 'pytest'
    - stage: Deploy
      steps:
        - echo "Deploying the application..."