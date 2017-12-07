#! groovy

#
# This Jenkinsfile is provided as an example of how MetaBrite builds packages
# based on this sample.  It references a handful of internal tools, so you
# will need to make your own modifications if you wish to use it in your own
# build pipeline.
#

package com.metabrite

def utils = new utils()
def notifier = new notifications()

ENVIRONMENT_VARIABLES = []

STASH_NAME = "mb_sample_package-${env.BUILD_NUMBER}"

node('ubuntu') {

  utils.withNotificationErrorHandling(this) {
    utils.withContext(ENVIRONMENT_VARIABLES) {

      stage('Checkout') {
        deleteDir()
        checkout scm
        stash STASH_NAME
      }

      stage('flake8') {
        sh '''#!/bin/bash -l
          tox -e flake8
        '''
      }

      stage('Test') {
        sh '''#!/bin/bash -l
          tox
        '''
      }

      stage('Publish to PyPi') {
        sh '''#!/bin/bash -l
          tox -e release
        '''
      }

    }
  }

}
