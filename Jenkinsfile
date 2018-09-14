#!/usr/bin/env groovy

def branch = env.BRANCH_NAME ?: 'master'

/** Desired capabilities */
def capabilities = [
  browserName: 'Firefox',
  version: '62.0',
  platform: 'Windows 10'
]

pipeline {
  agent any
  libraries {
    lib('fxtest@1.9')
  }
  triggers {
    pollSCM(branch == 'master' ? 'H/5 * * * *' : '')
    cron(branch == 'master' ? 'H * * * *' : '')
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
        }
        stage('py27') {
          agent {
            dockerfile true
          }
          steps {
            writeCapabilities(capabilities, 'capabilities.json')
            sh "tox -e py27"
          }
        }
      }
    }
  }
  post {
    changed {
      ircNotification()
    }
  }
}
