# BankLens

<p align="center">
  <img src="https://github.com/user-attachments/assets/658ebc10-7b35-4626-a841-21a787dfeb9e" alt="BankLens Logo" width="600"/>
</p>


BankLens is a repository designed to manage and analyze transactional data securely and efficiently. You connect your bank accounts with the Gocardless API. Below is an overview of the repository’s structure and instructions to get started. (More info to come)

## Repository Structure

The repository contains the following main components:

1. **data**
   - Contains private transactional data.
   - This directory will not sync to GitHub to maintain data privacy.

2. **secrets**
   - Holds private access keys.

3. **API**
   - Includes functions required to interact with the GoCardless API.

4. **src**
   - Contains the source code for the core functionality of the project.

5. **processes**
   - Includes executable scripts to run various processes.

6. **config**
   - A number of files that the user needs to edit in order to setup with personal accounts.

## Getting Started

To begin working with BankLens, you need to set up a configuration folder with the following files:

1. **`config/secrets.json`**
   - Obtain this file from the GoCardless developers’ portal: [GoCardless User Secrets](https://bankaccountdata.gocardless.com/user-secrets/).
   - This file contains essential access keys and configurations.

2. **`config/my_banks.json`**
   - This file should list of strings of all your bank account provider IDs. If you have multiple accounts with the same bank, only include it once. 
   - Example format:
    ```json
    {
      "bank_ids": ["<bankID1>", "<bankID2>", "..."]
    }
    ```

### Steps to Set Up

1. Create a `config` folder in the root directory of the repository.
2. Add `secrets.json` to the `config` folder.
3. Generate you private access keys using `processes/setup.ipynb`.
4. Generate the list of available banks using `processes/setup.ipynb`.
5. Specify your banks in `config/my_banks.json`.
6. Request access to each bank using `processes/setup.ipynb`.
7. Follow the onscreen instructions in the browser

## Notes
- Use environment variables or a `.gitignore` file to avoid accidental exposure of private data. By default the `secrets/` and `data/` are not tracked.

For additional guidance or support, feel free to raise an issue in this repository.
