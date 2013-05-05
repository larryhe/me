#!/bin/bash
usage(){
    echo "Usage: $PROGRAMNAME path-of-db id-of-blog"
}
PROGRAMNAME=`basename $0`
if [ $# -lt 1 ];then
    usage
    exit 1
fi
db=`cat $1`
sqlite3 ${db} "select b.title,b.content,b.created_date, t.desc from blog b, tag t where b.tag = t.id and b.id =$2"
