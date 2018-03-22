#!/usr/bin/env groovy

/** Desired capabilities */
def capabilities = [
  browserName: 'Firefox',
  version: '59.0',
  platform: 'Windows 10'
]

pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        deleteDir()
        checkout scm
        stash 'workspace'
      }
    }
    stage('Lint') {
      steps {
        deleteDir()
        unstash 'workspace'
        ansiColor('xterm') {
          sh "tox -e flake8"
        }
      }
    }
    stage('Test') {
      environment {
        SAUCELABS = credentials('SAUCELABS')
      }
      steps {
        unstash 'workspace'
        ansiColor('xterm') {
          sh "tox"
        }
      }
      post {
        always {
          stash includes: 'results/*', name: 'results'
          archiveArtifacts 'results/*'
        }
      }
    }
  }
}
