# obm-test
Tests for OpenBodyMind

# Create git branches structure
git clone https://github.com/chebo/obm-test.git
git checkout -b master
git commit -a -m "Brand new Master branch"
git push origin master

git checkout -b staging
git commit -a -m "Brand new Staging branch"
git push origin staging

git branch -a

# Jenkins Dockerfile
FROM jenkins/jenkins:lts-alpine
USER root
RUN apk add --no-cache python3 && \
 python3 -m ensurepip && \
 pip3 install --upgrade pip setuptools && \
 if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
 if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
 rm -r /root/.cache
RUN apk add pkgconf
RUN apk add build-base
RUN apk add python3-dev

#docker build -t jenkins_py .
#docker run -p 8080:8080 -p 50000:50000 -v ~/jenkins_home:/var/jenkins_home jenkins_py

#!/bin/bash
apt-get install python3
pwd
cd /usr/bin/
ls -l
uname -a
which python
python -v
pip3 install --upgrade virtualenv
virtualenv -v python3 --no-site-packages venv
source veenv/bin/activate
python -v
pip install -r requirements.txt
set -e
pycodestyle --exclude venv ./
deactivate






