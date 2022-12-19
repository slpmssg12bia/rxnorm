# Create Environment 
Ubuntu, t2micro, generate key (or select existing), select default security group, configure storage: 20, 
modify IAM role > select AmazonS3fullaccess, user must have SSH security access, connect with putty, log into server as user: ubuntu

# Update Environment 

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

aws key

aws secret key

us-east-1

json
```

# Clone Git Repository
```
git clone https://github.com/slpmssg12bia/rxnorm.git
```
# cd into the repository
```
cd rxnorm
```
# Recreate bash Files
```
touch rxnorm_clean.sh
nano rxnorm_clean.sh

#!/bin/bash
rm -rf rxnormdump

ctrl X
Y
---------------------------------
touch rxnorm_dump_to_s3.sh
nano rxnorm_dump_to_s3.sh

#!/bin/bash
aws s3 sync rxnormdump/ s3://viquity-database-import-us-east-1/Jobs/rxnorm/rxnormdump-"$(date +%d-%m-%y-%H-%M)"/

ctrl X
Y
------------------------
touch rxnorm_cron.sh
nano rxnorm_cron.sh

#!/bin/bash
cd /home/ubuntu/rxnorm
python3 rxnorm_cron.py

ctrl X
Y
```
# Delete Original bash files
```
rm clean.sh  dump_to_s3.sh  cron.sh
```

# Change Permissions of bash Files
```
chmod +x   rxnorm_clean.sh  rxnorm_dump_to_s3.sh  rxnorm_cron.sh
```

# install pip dependencies
```
pip install -r rxnorm_requirements.txt 
```
# install Cron jobs for Parsing
```
pwd

sudo apt-get install cron
```
# Open Cron Tab
```
sudo su

pip install -r rxnorm_requirements.txt 

nano /etc/crontab
```
# Create Cron Job ~ https://crontab.guru/examples.html
```
0 0 10 * *  root bash /home/ubuntu/rxnorm/rxnorm_cron.sh
!!!CARRIAGE RETURN after line above!!!!!

ctrl x

y

enter
```
