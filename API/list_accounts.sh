#!/bin/bash

ACCESS_TOKEN=$1
CONTRACT_ID=$2

response=$(curl -X GET "https://bankaccountdata.gocardless.com/api/v2/requisitions/$CONTRACT_ID/" \
  -H  "accept: application/json" \
  -H "Authorization: Bearer $ACCESS_TOKEN")

echo $response
