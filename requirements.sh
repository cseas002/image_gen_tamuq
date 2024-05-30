#!/bin/bash

sudo apt-get update
pip install flask
sudo apt-get install -y python3-pip
# Run on 3.11
#pip install jax
#pip install jaxlib
#pip install jax-metal
pip install keras
pip install numpy
pip install matplotlib
pip install notebook
pip install pandas
#pip install keras-cv
pip install tensorflow keras_cv --upgrade --quiet
sudo apt-get install -y jq


sed -i '$ a\export PATH="$PATH:/users/cseas002/.local/bin"' ~/.bashrc
source ~/.bashrc


# INSTALL DOCKER

# Add Docker's official GPG key:
sudo apt-get update
sudo apt -y install jq
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:4!

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Verify installation
docker --version

# Give access to the user
sudo chown $USER:docker /var/run/docker.sock
sudo chmod 660 /var/run/docker.sock