#!/bin/bash

BANK_ID=$1
ACCESS_TOKEN=$2

REFERENCE=$(date +%s)

RESPONSE=$(curl -X POST "https://bankaccountdata.gocardless.com/api/v2/requisitions/" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -d "{\"redirect\": \"http://www.yourwebpage.com\",
       \"institution_id\": \"$BANK_ID\",
       \"reference\": \"$REFERENCE\",
       \"user_language\":\"EN\" }")

echo $RESPONSE



