#!/bin/bash
# This script deploys the application using the POM cofiguration
# It is triggered only commits to the master or develop branches. Pulls are ignored

  echo "$TRAVIS_PYTHON_VERSION"
  echo "$TRAVIS_BRANCH"
  echo "$TRAVIS_PULL_REQUEST"
if [ "$TRAVIS_PULL_REQUEST" == "false" ] && [ "$TRAVIS_PYTHON_VERSION" == "$DEPLOY_PYTHON_VERSION" ] && [ "$TRAVIS_BRANCH" == "master" ]; then

  echo "Deploying site"

  gem install heroku
  git remote add heroku git@heroku.com:$HEROKU_APP.git

  echo "Host heroku.com" >> ~/.ssh/config
  echo "   StrictHostKeyChecking no" >> ~/.ssh/config
  echo "   CheckHostIP no" >> ~/.ssh/config
  echo "   UserKnownHostsFile=/dev/null" >> ~/.ssh/config

  heroku keys:clear

  yes | heroku keys:add
  yes | git push heroku master

else

   echo "Site won't be deployed"

fi
