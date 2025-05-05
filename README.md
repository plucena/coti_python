PROMPTS

running using Python 3.10.9

pip install dotenv
pip install coti-web3


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

compile @PrivateStorage.sol
cd contracts 
solc --abi PrivateStorage.sol -o . --overwrite

given @PrivateStorage.abi  deployed on Coti Testnet at 0x536A67f0cc46513E7d27a370ed1aF9FDcC7A5095 create a @web3.py program  witha function to invoke setPrivateNumber and another function to getPrivateNumber from @PrivateStorage.abi.   


