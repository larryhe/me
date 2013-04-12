#!/bin/bash
usage(){
    echo "Usage: $PROGRAMNAME deploy path"
}
PROGRAMNAME=`basename $0`
if [ $# -lt 1 ];then
    usage
    exit 1
fi
if [ ! -e "$1/res" ];then
    mkdir -p "$1/res"
fi
cp -R res/ "$1/res"
cp  *.{cgi,ejs,html} $1
