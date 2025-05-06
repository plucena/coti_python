PROMPTS

running using Python 3.10.9

python3 -m venv coti-env

source coti-env/bin/activate

pip install dotenv

pip install coti-web3

pip install Flask

*run programs using python3*


run onboarding example
```
cd coti-python-examples/coti-web3/examples         
python onboard.py

Creation done!
PK
ADDRESS
RuntimeError: Account balance is 0 so user cannot be onboarded.

https://faucet.coti.io
testnet address

python onboard.py
enter PK this time

.coti-python-examples/coti-python-examples/coti-web3/.env is updated with
ACCOUNT_PRIVATE_KEY=
ACCOUNT_ENCRYPTION_KEY=
```


list tokens

```
gemini 2.5 @coti-python-examples @coti-web3

create a program in web3.py  python that list all the COTI  tokens stored in coti main  network at this address 
0xb44E90707A29890942AE1D6595D6A52BA2Ba762e

use coti rpc address to connect
````

```
now do the same thing for COTI  testnet
````

deploy smart contracts

```
requires solc compiler
https://docs.soliditylang.org/en/latest/installing-solidity.html


gemini 2.5 @coti-python-examples @coti-web3 @PrivateStorage.sol

write a @coti-web3.py program to compile and deploy @PrivateStorage.sol  on Coti Testnet

will probably  fail signing
```

check smart contract on  testnet

```
https://testnet.cotiscan.io/address/0xb44E90707A29890942AE1D6595D6A52BA2Ba762e
```

```
compile @PrivateStorage.sol 


cd contracts solc --abi PrivateStorage.sol -o . --overwrite

@claude-3.7-sonnet

given  COTI smartcontract @PrivateStorage.abi   deployed on Coti Testnet at 0x5220aa2B4FeC347F751AaE0930d784f5139C526E create a @coti-web3.py  program with 2 separate functions and a menu invoke setPrivateNumber and getPrivateNumber from @PrivateStorage.abi use ACCOUNT_PRIVATE_KEY and use AES KEY 63f49d1ef7b1510060edcec934828b09 to decrypt ctUint64 type


```


create API

```
@gemini

Create a Flask REST API on a separate script that imports and calls functions from private_storage_menu.py

API should have two methods

GET privatenumber  calls function on private_storage_menu.py  no input poarams, 
should call the initialization start() before calling 
get_private_number(account, web3)

SET /privatenumber calls function on 
private_storage_menu.py int_value as the only param 
should call the initialization start() before calling 
set_private_number(account, web3, int_value)


check http://127.0.0.1:5000/privatenumber
```



