import pyfiglet
import sys
import time
import webbrowser
from web3 import Web3, HTTPProvider
from eth_account import Account
import requests
import json
import config
from colorama import Fore, Style, init

# Initialize colorama
init()

def animated_print(text, delay=0.001):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_logo():
    ascii_art = pyfiglet.figlet_format("LIKHON SCRIPTS", font="slant")
    animated_print(Fore.LIGHTMAGENTA_EX + ascii_art + Style.RESET_ALL)

def print_warning():
    warning_text = Fore.YELLOW + "WARNING: This script is for educational purposes only. Do not use without explicit permission." + Style.RESET_ALL
    animated_print(warning_text)

def print_donation_info():
    donation_text = Fore.CYAN + "Support the author: 0x00fC876d03172279E04CC30E5edCE103c3d23C1A" + Style.RESET_ALL
    animated_print(donation_text)

def open_telegram_link():
    telegram_url = "https://t.me/LikhonScripts"
    webbrowser.open_new(telegram_url)
    animated_print(Fore.GREEN + "Join us on Telegram: " + Style.RESET_ALL + telegram_url)

def print_transaction_info(batch_number, tx_hash, receipt):
    print(Fore.YELLOW + f"Batch {batch_number}: " + Fore.GREEN + "Transaction successful!" + Style.RESET_ALL)
    print(Fore.CYAN + f"  Transaction Hash: {tx_hash}" + Style.RESET_ALL)
    print(Fore.MAGENTA + f"  Block Number: {receipt.blockNumber}" + Style.RESET_ALL)
    print(Fore.BLUE + f"  Gas Used: {receipt.gasUsed}" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + f"  Cumulative Gas Used: {receipt.cumulativeGasUsed}" + Style.RESET_ALL)
    print(Fore.LIGHTRED_EX + f"  Transaction Index: {receipt.transactionIndex}" + Style.RESET_ALL)
    print()

# Print Logo and Warnings
print_logo()
print_warning()
time.sleep(0.001)  # Wait for 2 seconds
print_donation_info()
time.sleep(2)  # Wait for 2 seconds

# Function to load configuration and prompt for missing values
def load_config():
    if not config.owner_private_key:
        config.owner_private_key = input("Enter Owner's Private Key: ")
    if not config.contract_abi:
        config.contract_abi = input("Enter Contract ABI: ")

# Load configuration
load_config()

# Connect to BSC Testnet
web3 = Web3(HTTPProvider(config.bsc_testnet_url))
assert web3.is_connected(), "Failed to connect to BSC Testnet"

# Prepare contract details
contract_address = Web3.to_checksum_address(config.contract_address)
contract_abi = json.loads(config.contract_abi)

# Load Contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Fetch and Parse Addresses
url = "https://raw.githubusercontent.com/equilibre-finance/wallets-data/main/airdrop.txt"
response = requests.get(url)
data = response.text.split('\n')
addresses = [Web3.to_checksum_address(line.split(',')[0].strip()) for line in data if line]

# Your wallet address (the owner's address)
owner_address = Account.from_key(config.owner_private_key).address

# Prepare and Send Transactions in Batches
nonce = web3.eth.get_transaction_count(owner_address)
batch_size = 50  # Define your batch size
for i in range(0, len(addresses), batch_size):
    batch_addresses = addresses[i:i + batch_size]
    transaction = contract.functions.airdropTokens(batch_addresses).build_transaction({
        'chainId': 97,  # BSC Testnet Chain ID
        'gas': 2000000,  # Set appropriate gas limit
        'gasPrice': web3.to_wei('10', 'gwei'),
        'nonce': nonce,
    })
    nonce += 1  # Increment nonce for each transaction

    # Sign and Send Transaction
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key=config.owner_private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

    # Get Transaction Receipt and Print Info
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print_transaction_info(i // batch_size + 1, tx_hash.hex(), receipt)

animated_print(Fore.LIGHTBLUE_EX + "Airdrop Completed Successfully." + Style.RESET_ALL)

# Open Telegram link at the end
open_telegram_link()
