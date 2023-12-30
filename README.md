# LikhonScripts-AirdropTool  Automate your cryptocurrency airdrops with the LikhonScripts-AirdropTool.

This Python script simplifies the process of distributing tokens in batch on the Ethereum blockchain, making it ideal for token creators and project managers.

## Features - Batch processing of token airdrops. - Easy to use with a clear, colorful console interface. - Supports BSC Testnet and Ethereum Mainnet. - Automated Telegram link opening for community engagement.

## Prerequisites - Python 3.x - `web3`, `eth_account`, `requests`, `pyfiglet`, and `colorama` Python packages. -
An Ethereum wallet with enough ETH to cover gas fees. -
The ABI of the ERC20 token contract.  
## Installation Clone the repository: ```bash git clone https://github.com/LikhonScripts/AirdropAutomator/ cd LikhonScripts-AirdropTool``

Install required packages:

bashCopy code

`pip install -r requirements.txt`

Usage
-----

1.  Update the `config.py` file with your contract details and private key.
2.  Run the script:
    
    bashCopy code
    
    `python x.py`
    
3.  Follow the on-screen instructions.

Mainnet Deployment
------------------

To use the script on the Ethereum Mainnet:

*   Ensure you have sufficient ETH in your wallet for gas fees.
*   Update the `config.py` with Mainnet details and contract address.
*   Test with a small number of addresses before a full-scale airdrop.

Donations
---------

Support the development of this and other tools:

*   ETH: `0x00fC876d03172279E04CC30E5edCE103c3d23C1A`

Community
---------

Join our community on Telegram: [LikhonScripts](https://t.me/LikhonScripts)

Disclaimer
----------

This script is for educational purposes only. Use it at your own risk. The author is not responsible for any misuse or financial loss.

License
-------

MIT

vbnetCopy code
