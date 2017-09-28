#!/bin/bash

#Add details userid&pwd
DATE=$(date +%d-%m-%y)
BACKUP_DIR="/backup/test-backup"
USER_ID="root"
PASSWD="redhat"
MYSQL="/usr/bin/mysql"
MYSQLDUMP="/usr/bin/mysqldump"

mkdir -p $BACKUP_DIR/$DATE
#Get list of databases

databases=`$MYSQL -u$USER_ID -p$PASSWD -e "SHOW DATABASES;" | grep -Ev "(Database|information_schema)"`

#Dump each Database with seperate name

for db in $databases; do
echo $db
$MYSQLDUMP --force --opt --user=$USER_ID -p$PASSWD --databases $db | gzip | pv > $DIR/$db.sql.gz
done

