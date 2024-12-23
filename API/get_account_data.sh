ACCOUNT=$1
TOKEN=$2
TYPE=$3
RESPONSE=$(curl -X GET "https://bankaccountdata.gocardless.com/api/v2/accounts/$ACCOUNT/$TYPE/" \
    -H "accept: application/json" \
    -H "Authorization: Bearer $TOKEN")

echo "$RESPONSE"
