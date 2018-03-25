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
    lib('fxtest@1.9')
  }
  options {
    ansiColor('xterm')
    timestamps()
    timeout(time: 30, unit: 'MINUTES')
  }
  environment {
    PYTEST_ADDOPTS =
      "--tb=short " +
      "--color=yes " +
      "--driver=SauceLabs " +
      "--variables=capabilities.json"
    PULSE = credentials('PULSE')
    SAUCELABS = credentials('SAUCELABS')
  }
  stages {
    stage('Lint') {
      agent {
        dockerfile true
      }
      steps {
        sh "tox -e flake8"
      }
    }
    stage('Test') {
      parallel {
        stage('py36') {
          agent {
            dockerfile true
          }
          steps {
            writeCapabilities(capabilities, 'capabilities.json')
            sh "tox -e py36"
          }
          post {
            always {
              stash includes: 'results/py36.html', name: 'py36'
              archiveArtifacts 'results/*'
              junit 'results/*.xml'
            }
          }
        }
        stage('py27') {
          agent {
            dockerfile true
          }
          steps {
            writeCapabilities(capabilities, 'capabilities.json')
            sh "tox -e py27"
          }
          post {
            always {
              stash includes: 'results/py27.html', name: 'py27'
              archiveArtifacts 'results/*'
              junit 'results/*.xml'
            }
          }
        }
      }
    }
  }
  post {
    always {
      unstash 'py36'
      unstash 'py27'
      publishHTML(target: [
        allowMissing: true,
        alwaysLinkToLastBuild: true,
        keepAll: true,
        reportDir: 'results',
        reportFiles: "py36.html, py27.html",
        reportName: 'HTML Report'])
    }
    changed {
      ircNotification()
    }
    failure {
      emailext(
        attachLog: true,
        attachmentsPattern: 'results/*.html',
        body: '$BUILD_URL\n\n$FAILED_TESTS',
        replyTo: '$DEFAULT_REPLYTO',
        subject: '$DEFAULT_SUBJECT',
        to: '$DEFAULT_RECIPIENTS')
    }
  }
}
