#!/usr/bin/env bash
# This script sets up the web servers for web deployment of web_static

# update and upgrade system files
sudo apt update && sudo apt -y upgrade > /dev/null
# install nginx if not already installed
if [[ ! -f /usr/sbin/nginx ]]; then
    sudo apt -y install nginx > /dev/null
else
    echo -e "\t--- NGINX is already installed ---"
fi

# Allow Nginx HTTP on firewall
sudo ufw allow 'Nginx HTTP'

# create directories if not existing / do nothing if existing
for dir in /data/web_static/{shared,releases/test}; do
    sudo mkdir -p "$dir"
done

# create fake file index.html
fakebody=\
"<html>
<head>
  <title>Welcome to Onifemi.tech</title>
</head>
<body style='background-color: #f2f2f2; font-family: Arial, sans-serif; text-align: center; padding: 50px;'>
  <h1 style='color: #333333;'>Welcome to Onifemi.tech</h1>
  <p style='color: #666666; font-size: 18px;'>Thank you for visiting Onifemi.tech! We provide quality information and resources on various topics.</p>
  <p style='color: #666666; font-size: 18px;'>Feel free to explore the website and discover useful content.</p>
  <p style='color: #666666; font-size: 18px;'>If you have any questions, please don't hesitate to contact us.</p>
</body>
</html>"
echo -e "$fakebody" | sudo tee /data/web_static/releases/test/index.html

# create a forced symbolic link
sudo ln -sf  /data/web_static/releases/test /data/web_static/current

# give folder ownership to ubuntu and group Recursively
sudo chown -hR ubuntu:ubuntu /data/

# edit config file (append config after listen blah blah)
# sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo sed -i '/listen 80 default_server;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
# restart nginx service
sudo service nginx restart
echo ".......restarting nginx service......"

echo -e "\t SCRIPT RAN SUCCESSFULLY"
