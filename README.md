# Ricochet Keeper
This repository contains [Apache Airflow DAGs](https://airflow.apache.org/docs/apache-airflow/stable/concepts/dags.html) for executing keeper operations for Ricochet Exchange.

# Usage
You will need to run this using Docker and Docker Compose.
```
docker-compose up
```
:information_source: This will take a while the first time you do it
:warning: You may need to increase your Docker memory to > 4GB, default is 2GB

# Setup
After starting up Airflow, navigate to `Admin > Connections` and setup the following:
* A `HTTP` connection called `infura` with the connection's `Extra` as:
```
{
"http_endpoint_uri": "YOUR_INFURA_HTTP_URI",
"wss_endpoint_uri": "YOUR_INFURA_WSS_URI"
}
```

* Navigate to `Admin > Variables` and add the following:
  * `distributor-address` - the address used for executing `distribute` transactions
  * `harvester-address` - the address used for executing `harvest` transactions
  * `reporter-address` - the address used for reporting to Tellor
  * `closer-address` - the address used for closing streams
  * `ricochet-exchange-addresses` - add these addresses to value field:
  ```


  [ "0xBe79a6fd39a8E8b0ff7E1af1Ea6E264699680584", "0xeb367F6a0DDd531666D778BC096d212a235a6f78", "0x5786D3754443C0D3D1DdEA5bB550ccc476FdF11D", "0xe0A0ec8dee2f73943A6b731a2e11484916f45D44", "0x8082Ab2f4E220dAd92689F3682F3e7a42b206B42", "0x3941e2E89f7047E0AC7B9CcE18fBe90927a32100", "0x71f649EB05AA48cF8d92328D1C486B7d9fDbfF6b", "0x47de4Fd666373Ca4A793e2E0e7F995Ea7D3c9A29", "0x94e5b18309066dd1E5aE97628afC9d4d7EB58161", "0xdc19ed26aD3a544e729B72B50b518a231cBAD9Ab", "0xC89583Fa7B84d81FE54c1339ce3fEb10De8B4C96", "0x9BEf427fa1fF5269b824eeD9415F7622b81244f5", "0x0A70Fbb45bc8c70fb94d8678b92686Bb69dEA3c3", "0x93D2d0812C9856141B080e9Ef6E97c7A7b342d7F", "0xE093D8A4269CE5C91cD9389A0646bAdAB2c8D9A3", "0xA152715dF800dB5926598917A6eF3702308bcB7e", "0x250efbB94De68dD165bD6c98e804E08153Eb91c6", "0x98d463A3F29F259E67176482eB15107F364c7E18" ]

  ```
  * `ricochet-lp-addresses` - the addresses of markets with `harvest` methods
  ```
  [ "0x0cb9cd99dbC614d9a0B31c9014185DfbBe392eb5"]
  ```
  * `tellor-assets` - the mapping of Coingecko token names and their Tellor request ID
  ```
  {
    "ethereum": 1,
    "wrapped-bitcoin": 60,
    "maker": 5,
    "matic-network": 6,
    "idle": 79,
    "richochet": 77
  }
  ```
  :warning: `richochet` is not a typo, that's the Coingecko ID for RIC token price
* Create an `HTTP` **for each** of the public addresses you used in the previous step:
  * Set the name this connection as the public address
  * Set the `Login` to the public address
  * Set the `Password` to the private key for the public address

## Optional
* Navigate to `Admin > Variables` and add the following to change dag schedule:
  * `distribution-schedule-interval` - Dag `distribute` (Default - `0 * * * *`)
  * `harvester-schedule-interval` - Dag `harvester` (Default - `0 * * * *`)
  * `watch-schedule-interval` - Watch stream dag (Default - `50 * * * *`)
  * `tellor-schedule-interval` - Reporting to Tellor (Default - `*/5 * * * *`)
  * `swap-schedule-interval` - Swap RIC stream to matic (Default - `0 * * * *`)
  * `block-poll-schedule-interval` - Block poll (Default - `*/15 * * * *`)
  * `close-schedule-interval` - Close streams (Default - `None`)
  * `max-gas-price` - To set the max gas price (Default - `33`)

# Run
Run the keeper using Docker Compose
```
echo -e "AIRFLOW_UID=$(id -u)" > .env
docker-compose up
```
Airflow runs on port 80 so navigate to http://localhost to access the UI. Once things have booted up, log in with username `airflow` and password  `airflow`.

## Run as daemon
Use:
```
echo -e "AIRFLOW_UID=$(id -u)" > .env
docker-compose up -d
```
