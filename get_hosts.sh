#!/bin/bash
cd /home/ec2-user/hosts
unzip -P "$(python spider.py)" host.zip
mv /home/ec2-user/hosts/hosts /var/ftp/hosts