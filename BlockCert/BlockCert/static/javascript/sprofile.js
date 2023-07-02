 //let provider = new ethers.providers.Web3Provider(window.ethereum)
 const provider = ((window.ethereum != null) ? new ethers.providers.Web3Provider(window.ethereum) : ethers.providers.getDefaultProvider());
  let signer

// 1. Connect Metamask with Dapp
async function connectMetamask() {
  // MetaMask requires requesting permission to connect users accounts
  await provider.send("eth_requestAccounts", []);

  signer = await provider.getSigner();

  console.log("Account address s:", await signer.getAddress());
}

// 2. Get balance
async function getBalance() {
  const balance = await signer.getBalance()
  const convertToEth = 1e18;
  console.log("account's balance in ether:", balance.toString() / convertToEth);
}
// 3. read data from the USDT contract on kovan 
const usdtAddress = "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4";

const usdtAbi = [
  // Some details about the token
  [
    {
      "constant": false,
      "inputs": [
        {
          "name": "_address",
          "type": "address"
        },
        {
          "name": "_gpa",
          "type": "uint256"
        },
        {
          "name": "_subjects",
          "type": "bool"
        },
        {
          "name": "_name",
          "type": "string"
        },
        {
          "name": "_id",
          "type": "int256"
        }
      ],
      "name": "setStudent",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "name": "subjects",
          "type": "bool"
        },
        {
          "indexed": false,
          "name": "name",
          "type": "string"
        },
        {
          "indexed": false,
          "name": "id",
          "type": "int256"
        },
        {
          "indexed": false,
          "name": "gpa",
          "type": "uint256"
        }
      ],
      "name": "studentinfo",
      "type": "event"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "countStudents",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "_address",
          "type": "address"
        }
      ],
      "name": "getStudent",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        },
        {
          "name": "",
          "type": "bool"
        },
        {
          "name": "",
          "type": "string"
        },
        {
          "name": "",
          "type": "int256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "getStudent",
      "outputs": [
        {
          "name": "",
          "type": "address[]"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "studentaccts",
      "outputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "name": "students",
      "outputs": [
        {
          "name": "subjects",
          "type": "bool"
        },
        {
          "name": "name",
          "type": "string"
        },
        {
          "name": "gpa",
          "type": "uint256"
        },
        {
          "name": "id",
          "type": "int256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    }
  ]
];

async function readDataFromSmartContract() {

  const usdtContract = new ethers.Contract(usdtAddress, usdtAbi, provider);
  
  const name = await usdtContract.name()
  const symbol = await usdtContract.symbol()
  const decimals = await usdtContract.decimals()
  const totalSupply = await usdtContract.totalSupply()
  const myBalance = await usdtContract.balanceOf("0x5B38Da6a701c568545dCfcB03FcB875f56beddC4")

  console.log(`name = ${name}`)
  console.log(`symbol = ${symbol}`)
  console.log(`decimals = ${decimals}`)
  console.log(`totalSupply = ${totalSupply / 1e6 }`)
  console.log(`myBalance = ${myBalance / 1e6}`)
}





