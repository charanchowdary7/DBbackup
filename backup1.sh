#!/bin/bash

#Backup folder
cd /home/vagrant/mysql/

#Get List of databases
LISTDB=$( echo 'show databases' | mysql -uroot -p'redhat' )

#save current date
DATE=`date +%y-%m-%d`

#List of databases

for SQL in $LISTDB
do
if [ $SQL != "information_schema" ] && [ $SQL != "mysql" ] && [ $SQL != "performance_schema" ]; then

#BackupDatabase
mysqldump --force --opt -uroot -p'redhat' $SQL  > ${sql}_`date +"%y-%m-%d"`.sql

#compress file tar.bz2
#tar jcf ${sql}_`date +"%y-%m-%d"`.sql.tar.bz2 ${sql}_`date +"%y-%m-%d"`.sql

#delete backups
#rm ${sql}_`date +"%y-%m-%d"`.sql
fi
done

