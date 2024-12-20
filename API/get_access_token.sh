#!/bin/bash

FILENAME=$1
SECRET_FILE=secrets/secrets/$FILENAME
ACCESS_TOKEN_FILE=secrets/access_token/$FILENAME

SECRET_ID=$(jq -r .secret_id $SECRET_FILE)
SECRET_KEY=$(jq -r .secret_key $SECRET_FILE)

echo "SECRET_ID: $SECRET_ID"
echo "SECRET_KEY: $SECRET_KEY"

mkdir -p secrets/access_token

curl -X POST https://bankaccountdata.gocardless.com/api/v2/token/new/ \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d "{\"secret_id\":\"$SECRET_ID\", \"secret_key\":\"$SECRET_KEY\"}" \
  -o $ACCESS_TOKEN_FILE