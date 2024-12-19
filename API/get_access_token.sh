#!/bin/bash

CONFIG_FILE="secrets/config.json"

SECRET_ID=$(jq -r '.secret_id' "$CONFIG_FILE")
SECRET_KEY=$(jq -r '.secret_key' "$CONFIG_FILE")

curl -X POST "https://bankaccountdata.gocardless.com/api/v2/token/new/" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d "{\"secret_id\":\"$SECRET_ID\", \"secret_key\":\"$SECRET_KEY\"}" \
  -o Secrets/access_token.json