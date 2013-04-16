#!/bin/bash
usage(){
    echo "Usage: $PROGRAMNAME deploy path"
}
PROGRAMNAME=`basename $0`
if [ $# -lt 1 ];then
    usage
    exit 1
fi
cp -R bootstrap "$1/bootstrap"
cp -R res "$1/res"
cp -R admin "$1/admin"
cp  *.{cgi,ejs,html,txt} $1
