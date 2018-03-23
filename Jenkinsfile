#!/usr/bin/env groovy

/** Desired capabilities */
def capabilities = [
  browserName: 'Firefox',
  version: '59.0',
  platform: 'Windows 10'
]

pipeline {
  agent any
  libraries {
    lib('fxtest@1.10')
  }
  environment {
    PYTEST_PROCESSES = "${PYTEST_PROCESSES ?: "auto"}"
    PYTEST_ADDOPTS =
      "-n=${PYTEST_PROCESSES} " +
      "--tb=short " +
      "--color=yes " +
      "--driver=SauceLabs " +
      "--variables=capabilities.json"
    PULSE = credentials('PULSE')
    SAUCELABS = credentials('SAUCELABS')
  }
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
        ansiColor('xterm')
        writeCapabilities(capabilities, 'capabilities.json')
        sh "tox -e flake8"
      }
    }
    stage('Test') {
      parallel {
        stage('py27') {
          steps {
            unstash 'workspace'
            ansiColor('xterm')
            writeCapabilities(capabilities, 'capabilities.json')
            sh "tox -e py27"
          }
        }
        stage('py36') {
          steps {
            unstash 'workspace'
            ansiColor('xterm')
            writeCapabilities(capabilities, 'capabilities.json')
            sh "tox -e py36"
          }
        }
      }
    }
  }
  post {
    always {
      stash includes: 'results/*', name: 'results'
      archiveArtifacts 'results/*'
    }
  }
}
