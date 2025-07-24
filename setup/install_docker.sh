#!/bin/bash

echo "[+] Updating system..."
sudo apt update

echo "[+] Removing old Docker versions..."
sudo apt remove -y docker docker-engine docker.io containerd runc
sudo apt purge -y docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-buildx-plugin

echo "[+] Installing dependencies..."
sudo apt install -y ca-certificates curl gnupg lsb-release apt-transport-https software-properties-common

echo "[+] Adding Docker GPG key and repository..."
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

echo "[+] Installing Docker Engine and Compose plugin..."
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-buildx-plugin

echo "[+] Enabling Docker daemon..."
sudo systemctl enable docker
sudo systemctl start docker

echo "[+] Adding current user to Docker group..."
sudo usermod -aG docker $USER

echo "[✓] Docker setup complete!"
echo "⚠️ You may need to log out and log back in or run: newgrp docker"
