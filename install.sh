#!/bin/bash
usage(){
    echo "Usage: $PROGRAMNAME deploy path"
}
PROGRAMNAME=`basename $0`
if [ $# -lt 1 ];then
    usage
    exit 1
fi
cp *.cgi "$1/cgi-bin/"
cp *.{html,css,js,ejs,txt} $1
