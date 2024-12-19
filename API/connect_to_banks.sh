#!/bin/bash

TOKEN_FILE="secrets/access_token.json"
ACCESS_TOKEN=$(jq -r '.access' "$TOKEN_FILE")

# Check if a BANK_ID is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <bank_id>"
  exit 1
fi

BANK_ID="$1"

echo "Using Bank ID: $BANK_ID"

curl -X POST "https://bankaccountdata.gocardless.com/api/v2/requisitions/" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -d "{\"redirect\": \"http://www.yourwebpage.com\",
       \"institution_id\": \"$BANK_ID\",
       \"reference\": \"1\",
       \"user_language\":\"EN\" }"
