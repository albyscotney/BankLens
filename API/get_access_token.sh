#!/bin/bash

SECRET_ID=$1
SECRET_KEY=$2

RESPONSE=$(curl -s -X POST https://bankaccountdata.gocardless.com/api/v2/token/new/ \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d "{\"secret_id\":\"$SECRET_ID\", \"secret_key\":\"$SECRET_KEY\"}")

echo $RESPONSE
