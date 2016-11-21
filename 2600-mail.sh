#!/bin/bash
#
# Executes the script given as argument #2,
# then if there is anything printed to stdout,
# it will email the text as the body of the email
# 
# &copy; Michael Craze -- http://projectcraze.us.to

if [ "$#" -ne 2 ] ; then
	echo "Usage: $0 <subject> <2600_script>"
	exit
fi

EMAIL="user@example.com"
SUBJECT=$1
CLSCRIPT=$2
PY=`which python`
MAIL=`which mail`
BODY=`$PY $CLSCRIPT`

# send email if something was posted today
if [ -n "$BODY" ] ; then
	echo $BODY | $MAIL -s $SUBJECT $EMAIL
fi
