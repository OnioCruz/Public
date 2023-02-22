#!/bin/bash

sudo systemctl stop httpd
sudo rm -rf /var/www/html/*
sudo yum remove httpd wget unzip -y
[root@scriptbox scripts]# cat 2_websetup.sh
#!/bin/bash

# Installing Dependencies
echo "###########################"
echo "Installing packages."
echo "###########################"
sudo yum install wget unzip httpd -y > /dev/null
echo

# Start and Enable Service
echo "###########################"
echo "Start & Enable HTTPD Service."
echo "###########################"
sudo systemctl start httpd
sudo systemctl enable httpd
echo

# Creating Temp Directory
echo "###########################"
echo "Starting Artifact Deployment"
echo "###########################"
mkdir -p /tmp/webfiles
cd /tmp/webfiles
echo

wget https://www.tooplate.com/zip-templates/2129_crispy_kitchen.zip
unzip 2129_crispy_kitchen.zip > /dev/null
sudo cp -r 2129_crispy_kitchen/* /var/www/html/
echo

# Bounce Service
echo "###########################"
echo "Restarting HTTPD service"
echo "###########################"
systemctl restart httpd
echo

# Clean Up
echo "###########################"
echo "Removing Temporary Files"
echo "###########################"
rm -rf /tmp/webfiles
echo

sudo systemctl status httpd
ls /var/www/html