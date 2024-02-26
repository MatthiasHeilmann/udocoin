# udocoin

A Blockchain-project as part of the class "Distributed Systems" in the winter semester 2023 of the course TINF21AI2 at DHBW Mannheim.

# Guides

The following paragraphs explain how to run the miner-application and the wallet app

## Udocoin Miner

Before starting, you might need to open a Powershell window as an Administrator and execute the following command to be able to execute the Udocoin Powershell starting script.

```sh
set-executionpolicy remotesigned
```

### Docker/docker-compose

To run the udocoin miner application, with Docker you need to have Docker Desktop and docker-compose installed on your machine. 

If you don't have a public and a private key, you also need to have at least Python 3.8 to generate keys. (See References for testing keys)

In your terminal, change your directory to udocoin/udocoin_miner

```sh
cd udocoin_miner
```

Execute the start files and follow the instructions in the terminal.

Windows:
```sh
start.ps1
```

Other operating systems:
```sh
source start.sh
```

Building the docker containers will take some time. Keep in mind you will have to have the Docker Desktop app running while building the application.

The server will be running on [localhost:80](http://localhost).

Go to [localhost/miner](http://localhost/miner) to check information about your server and the blockchain.

### Without Docker

To run the udocoin miner application without Docker, you need to have at least Python 3.8 installed.

Change the directory to udocoin/udocoin_miner/application

```sh
cd udocoin_miner/application
```

Create and activate a Python virtual environment and install required packages

Windows:

```sh
python -m venv venv
venv\Scripts\activate.ps1
pip install -r requirements.txt
```

Other operation systems:

```sh
python3 -m venv venv
source venv/Scripts/activate
pip3 install -r requirements.txt
```

And then start the server

Windows:

```sh
python run.py
```

Other operating systems:

```sh
python3 run.py
```

Follow the instructions in the terminal and the server will be running on [localhost:5000](http://localhost:5000).

Go to [localhost:5000/miner](http://localhost:5000/miner) to check information about your server and the blockchain.

## Udocoin Wallet

To create and send transactions, the wallet app should be used. Alternatively, you can use the file "post_to_localhost.py" to create a transaction and post it to your locally hosted Udocoin Miner. You can download the APK-File [here](https://drive.google.com/file/d/1RBWDwRG7Wh2-fMB4cK8w0fA7ZUQAFamD/view?usp=drive_link) and install it on your android device with an android version of at least 7.1.1. It is recommended to use a USB-cable to transfer the app to the mobile device.

The app was developed and tested on 

* Google Pixel 3a (Android version 13)
* Samsung Galaxy A52 (Android version 13)

If there are problems with the installation of the APK-file, try to open the project in Android Studio to run the development version.

The app will notify you that it's running with an unlicensed version of Chaquopy. Please don't mind, there are no licensing issues as Chaquopy has gone open source under the MIT license.

If you don't get asked to grant camera-permission, go to your device's settings > apps > Udocoin Wallet and allow camera usage.

Scan the private key from sources/keys/server/privkey.png to immediately gain access to an account with balance if the seed server on our aws ec2 instance is running :)

## Tests

### Consensus

To test the consensus algorithm you can access the endpoint /consensus_test or execute:

```sh
python udocoin_miner/tests/consensus_test.py
```

```sh
python3 udocoin_miner/tests/consensus_test.py
```

### Transactions

To test transactions without using the mobile app execute:

```sh
python udocoin_miner/tests/post_to_localhost.py
```

```sh
python3 udocoin_miner/tests/post_to_localhost.py
```

# References

| Name | Link |
| --- | --- |
| Primary GitHub Repository | https://github.com/LorenzMu/udocoin |
| Thesis | https://drive.google.com/file/d/1oxez2EUX-5tV6rElotlojEpF0cuj_UPQ/view |
| Slides | https://drive.google.com/file/d/1cIJzTRuKEQbGstQIJW4WPHlkCkoC6eFM/view |
| Wallet APK | https://drive.google.com/file/d/1RBWDwRG7Wh2-fMB4cK8w0fA7ZUQAFamD/view?usp=drive_link |
| Sources gDrive | https://drive.google.com/drive/folders/1zLEWjr3jMXuw4lIt8uKNWesUSG-uYkJ3 |
