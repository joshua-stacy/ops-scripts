#!/bin/bash

date=`date +%m_%d_%Y`

cd /

df -h > /var/log/disk_usage-$date

sudo du -h --max-depth=1 >> /var/log/disk_usage-$date
