#!/bin/bash
mysqldump -u root -predhat Database1 | gzip > /home/vagrant/Dump/mysqldump_`date +"%y-%m-%d"`.sql.gz

