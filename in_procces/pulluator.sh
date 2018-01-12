#!/bin/bash
# $1 - what
# $2 - where
# $3 - host
# $4 - user

if [ $# == 0 ];
then
  echo "Need parameters!";
  exit 1;
fi

echo "Pulling $1 to $2";
scp -v $1 $4@$3:$2;
if [ $? == 0 ];
then
  echo "Pulling to $3 complite!";
else
  echo "";
  echo "Erorr $1 not pull!!";
fi
