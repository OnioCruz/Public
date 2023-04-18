#!/bin/bash

# update package list
sudo apt update

# download wget for future code
sudo apt-get install -y wget

# install dependencies
sudo apt install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common

# install curl for jenkins part of the code
sudo apt install -y curl

# install kubernetes
sudo curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt update
sudo apt install -y kubectl

# install jenkins
curl -fsSL https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee \
    /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
    https://pkg.jenkins.io/debian binary/ | sudo tee \
    /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install -y fontconfig openjdk-11-jre
sudo apt-get install -y jenkins

# install ansible
sudo apt install -y ansible

# install docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io

# install grafana
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
sudo apt update
sudo apt install -y grafana

# install prometheus
wget https://github.com/prometheus/prometheus/releases/download/v2.30.0/prometheus-2.30.0.linux-amd64.tar.gz
tar -xzf prometheus-2.30.0.linux-amd64.tar.gz
sudo mv prometheus-2.30.0.linux-amd64 /usr/local/prometheus

# install terraform
wget https://releases.hashicorp.com/terraform/1.0.7/terraform_1.0.7_linux_amd64.zip
sudo unzip terraform_1.0.7_linux_amd64.zip -d /usr/local/bin/

# install gitlab
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash
sudo apt-get install -y gitlab-ce

# install nagios
sudo apt-get install -y nagios3 nagios-plugins

# install splunk
wget -O splunk-8.2.2.1-ae7fbb097bda-Linux-x86_64.tgz 'https://www.splunk.com/bin/splunk/DownloadActivityServlet?architecture=x86_64&platform=linux&version=8.2.2.1&product=splunk&filename=splunk-8.2.2.1-ae7fbb097bda-Linux-x86_64.tgz&wget=true'
sudo tar -zxvf splunk-8.2.2.1-ae7fbb097bda-Linux-x86_64.tgz -C /opt
sudo /opt/splunk/bin/splunk start --accept-license --answer-yes --no-prompt --seed-passwd password123

# install git
sudo apt-get install -y git

# install python3 and pip
sudo apt-get install -y python3 python3-pip

# Install Nexus
wget https://download.sonatype.com/nexus/3/latest-unix.tar.gz
sudo tar -zxvf latest-unix.tar.gz -C /opt
sudo mv /opt/nexus-* /opt/nexus
sudo adduser --disabled-password --gecos "" nexus
sudo chown -R nexus:nexus /opt/nexus
sudo sed -i '$a RUN_AS_USER="nexus"' /opt/nexus/bin/nexus.rc
sudo ln -s /opt/nexus/bin/nexus /etc/init.d/nexus
sudo update-rc.d nexus defaults
sudo service nexus start

# Install SonarQube
wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-8.9.2.46101.zip
sudo unzip sonarqube-8.9.2.46101.zip -d /opt
sudo mv /opt/sonarqube-* /opt/sonarqube
sudo adduser --disabled-password --gecos "" sonarqube
sudo chown -R sonarqube:sonarqube /opt/sonarqube
sudo sed -i 's|#sonar.jdbc.username=|sonar.jdbc.username=sonarqube|g' /opt/sonarqube/conf/sonar.properties
sudo sed -i 's|#sonar.jdbc.password=|sonar.jdbc.password=sonarqube|g' /opt/sonarqube/conf/sonar.properties
sudo sed -i 's|#sonar.jdbc.url=jdbc:postgresql://localhost/sonarqube|sonar.jdbc.url=jdbc:postgresql://localhost/sonarqube|g' /opt/sonarqube/conf/sonar.properties
sudo sed -i 's|#sonar.web.host=127.0.0.1|sonar.web.host=0.0.0.0|g' /opt/sonarqube/conf/sonar.properties
sudo ln -s /opt/sonarqube/bin/linux-x86-64/sonar.sh /etc/init.d/sonarqube
sudo update-rc.d sonarqube defaults
sudo service sonarqube start

# Install Slack
wget https://downloads.slack-edge.com/linux_releases/slack-desktop-4.16.0-amd64.deb
sudo dpkg -i slack-desktop-4.16.0-amd64.deb
sudo apt-get install -f -y

# one more update to finish it off
sudo apt-get update