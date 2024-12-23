#!/bin/bash

ACCESS_TOKEN=$1
SAVE_PATH=$2

mkdir -p "$(dirname "$SAVE_PATH")"

curl -X GET "https://bankaccountdata.gocardless.com/api/v2/institutions/?country=gb" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -o $SAVE_PATH


jq . $SAVE_PATH > temp.json && mv temp.json $SAVE_PATH
