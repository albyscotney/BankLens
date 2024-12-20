#!/bin/bash

TOKEN_FILE="secrets/access_token.json"
ACCESS_TOKEN=$(jq -r '.access' "$TOKEN_FILE")

curl -X GET "https://bankaccountdata.gocardless.com/api/v2/requisitions/8126e9fb-93c9-4228-937c-68f0383c2df7/" \
  -H  "accept: application/json" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -o data/banks/my_banks.json
