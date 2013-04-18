#!/bin/bash
usage(){
    echo "Usage: $PROGRAMNAME deploy path"
}
PROGRAMNAME=`basename $0`
if [ $# -lt 1 ];then
    usage
    exit 1
fi
cp -R bootstrap "$1"
cp -R res "$1"
cp -R admin "$1"
cp  *.{cgi,ejs,html,txt} $1
