Need to Install Below:
-Ganache
-Python 3.8
-pip install black
-pip install py-solc-x
pip install python-dotenv
Reads environment variables
Microsoft C++ Build Tools
https://github.com/smartcontractkit/full-blockchain-solidity-course-py/discussions/206
https://docs.microsoft.com/en-us/answers/questions/136595/error-microsoft-visual-c-140-or-greater-is-require.html
https://stackoverflow.com/questions/71142893/pip-install-web3-error-microsoft-visual-c-14-0-or-greater-is-required
-pip install web3 [Requires above Microsoft C++ Build Tools ]
restart Visual Studia Code
If you are working on VS Code, then after installing web3 via pip, just restart the VS Code editor. It will then find Web3.

Be careful about the below line:
from web3 import Web3 <- Small and Capital 'W'

Again, installing web3 requires Visual Studio Build Tools to be installed

Install Ganache
Install nodejs latest version
Install yarn package management:  npm install --global yarn
https://classic.yarnpkg.com/lang/en/docs/install/#windows-stable
npm install -g ganache
ganache-cli --version

Install Brownie [pip is recommended]
git clone https://github.com/eth-brownie/brownie.git
cd brownie
python3 -m venv venv

Install Below Visual Studio Code Extensions
-Bracker Pair Colorized
-Solidity [Developer: Juan Blanco]

-Python 3.8 or hogher

