This repo is made of 5 main components:

1. data - this is private trasnactional data. It will not sync to github
2. secrets - These are private access keys
3. API - These are the functions needed to interact with gocardless API.
4. src - This is the source code.
5. processes - These are the executable scripts

# Getting Started

To get started, you should create a config folder. It must contain
1. `secrets.json`: This must come from https://bankaccountdata.gocardless.com/user-secrets/ under `developers/user_secrets`
2. `my_banks.json`: This should be a list of all your bank account providers IDs