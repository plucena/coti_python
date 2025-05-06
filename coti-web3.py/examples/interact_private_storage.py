import os
from dotenv import load_dotenv
from web3 import Web3
from eth_account import Account
from web3.utils.coti import CotiNetwork, init_web3

# Load environment variables
load_dotenv()

# Contract details
CONTRACT_ADDRESS = "0x6aA33b6357230e44bCEB1CA5c5c580112d0e13a4"
CONTRACT_ABI = [
    {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [],
        "name": "privateNumber",
        "outputs": [
            {
                "internalType": "ctUint64",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "ctUint64",
                        "name": "ciphertext",
                        "type": "uint256"
                    },
                    {
                        "internalType": "bytes",
                        "name": "signature",
                        "type": "bytes"
                    }
                ],
                "internalType": "struct itUint64",
                "name": "value",
                "type": "tuple"
            }
        ],
        "name": "setPrivateNumber",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

# Initialize Web3 and account
w3 = init_web3(CotiNetwork.TESTNET)
private_key = os.getenv("ACCOUNT_PRIVATE_KEY")
account = Account.from_key(private_key)
w3.eth.default_account = account.address

# Load the contract
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

def set_private_number(value: int):
    """Set the private number in the contract."""
    # Encrypt the value using the account's AES key
    encrypted_value = w3.coti.encrypt_value(value, account)
    
    # Prepare the transaction
    tx = contract.functions.setPrivateNumber(encrypted_value).build_transaction({
        'from': account.address,
        'nonce': w3.eth.get_transaction_count(account.address),
    })
    
    # Sign and send the transaction
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    
    # Wait for the transaction to be mined
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Transaction successful with hash: {tx_hash.hex()}")

def get_private_number():
    """Get the private number from the contract."""
    # Call the contract function
    encrypted_value = contract.functions.privateNumber().call()
    
    # Decrypt the value using the account's AES key
    decrypted_value = w3.coti.decrypt_value(encrypted_value, account)
    print(f"Private Number: {decrypted_value}")

def menu():
    """Simple menu to interact with the contract."""
    while True:
        print("\n1. Set Private Number")
        print("2. Get Private Number")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            value = int(input("Enter the private number: "))
            set_private_number(value)
        elif choice == '2':
            get_private_number()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu() 