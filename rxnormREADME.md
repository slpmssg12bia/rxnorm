# Cron jobs For Data Parsing 

```
sudo apt update 

sudo apt install unzip

sudo apt install python3-pip -y

```
# Install AWS CLI 
```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

unzip awscliv2.zip

sudo ./aws/install
```

# Configure AWS CLI
```
aws configure

AKIA6CZ442HWM64HSD7R

tnrbtyMG2j+iYOiXP2BiBwpwWCvfe77FDuQndsBM

us-east-1

json
```

# Clone Git Repository
```
git clone https://github.com/slpmssg12bia/nppes.git
```
# cd into the repository
```
cd nppes
```
# change permission of .sh files
```
chmod +x   nppes_clean.sh  nppes_dump_to_s3.sh  nppes_cron.sh
```

# install pip dependencies
```
pip install -r nppes_requirements.txt 
```
# install Cron jobs for Parsing
```
pwd
sudo apt-get install cron
```
# Open Cron Tab
```
sudo su

nano /etc/crontab

1
```
# Create Cron Job
```
0 0 1 * *  root bash /home/ubuntu/nppes/nppes_cron.sh

ctrl x

y

enter
```