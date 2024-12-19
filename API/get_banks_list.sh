#!/bin/bash

TOKEN_FILE="secrets/access_token.json"
ACCESS_TOKEN=$(jq -r '.access' "$TOKEN_FILE")
curl -X GET "https://bankaccountdata.gocardless.com/api/v2/institutions/?country=gb" \
  -H "accept: application/json" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -o data/banks/banks.json

jq . data/banks/banks.json > temp.json && mv temp.json data/banks/banks.json
