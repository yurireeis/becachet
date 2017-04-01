FROM jenkinsci/jenkins:lts

USER root

RUN apt-get -y update && \
  apt-get -q -y install sudo python3 python3-dev python3-pip

RUN pip3 install virtualenv virtualenvwrapper

RUN adduser jenkins sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

RUN mkdir /var/jenkins_home/environments

USER jenkins

ENV WORKON_HOME /var/jenkins_home/environments
