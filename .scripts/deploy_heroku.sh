#!/bin/bash
# This shell script is prepared for deploying an application to Heroku through Travis
# It is triggered only commits to the master or develop branches. Pulls are ignored.
#
# The script is prepared for Python, change the TRAVIS_PYTHON_VERSION and DEPLOY_PYTHON_VERSION for your language.
#
# Note that it makes use of the following environmental variables from Travis:
# - TRAVIS_PULL_REQUEST: used to ignore pulls
# - TRAVIS_BRANCH: used to deploy only from the master branch
# - TRAVIS_PYTHON_VERSION: change this for the correct one for the language you are using
#
# And requires the following custom environmental variables:
# - DEPLOY_PYTHON_VERSION: custom variable, used to indicate the version which will be used for deployment

if [ "$TRAVIS_PULL_REQUEST" == "false" ] && [ "$TRAVIS_PYTHON_VERSION" == "$DEPLOY_PYTHON_VERSION" ] && [ "$TRAVIS_BRANCH" == "master" ]; then

  echo "Deploying site"

  # The Heroku gem is installed
  gem install heroku
  git remote add heroku git@heroku.com:$HEROKU_APP.git

  # A configuration file is created and set up for Heroku
  echo "Host heroku.com" >> ~/.ssh/config
  echo "   StrictHostKeyChecking no" >> ~/.ssh/config
  echo "   CheckHostIP no" >> ~/.ssh/config
  echo "   UserKnownHostsFile=/dev/null" >> ~/.ssh/config

  # Sets up keys
  heroku keys:clear
  yes | heroku keys:add

  # Pushes to Heroku. This is forced so it will work even if the app is running.
  yes | git push heroku master -f

else

   echo "Site won't be deployed"

fi
