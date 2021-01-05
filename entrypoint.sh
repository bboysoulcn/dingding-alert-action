#!/bin/sh

export

if [ -z "$DING_SECRET" ]
then
  echo "You must provide DING_SECRET"
  exit 1
fi

if [ -z "$DING_BASE_URL" ]
then
  echo "You must provide DING_BASE_URL"
  exit 1
fi
if [ -z "$MSG" ]
then
  echo "You must provide MSG"
  exit 1
fi
if [ -z "$TITLE" ]
then
  echo "You must provide TITLE"
  exit 1
fi



python /main.py $DING_SECRET $DING_BASE_URL $MSG $TITLE
