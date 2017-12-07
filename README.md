# eth-priv-to-addr

### What is this?
`eth-priv-to-addr` is a docker utility meant to be invoked to ensure the correctness of multiple implementations for deriving an Ethereum account address from a given private key.

[MyEtherWallet](https://github.com/myetherwallet/myetherwallet) uses `eth-priv-to-addr` as part of their [derivationChecker](https://github.com/MyEtherWallet/MyEtherWallet/blob/develop/spec/integration/derivationChecker.int.ts) integration test.

##### The derivation checker utility assumes that you have:
1. Docker installed/available
2. [dternyak/eth-priv-to-addr](https://hub.docker.com/r/dternyak/eth-priv-to-addr/) pulled from DockerHub

##### Docker setup instructions:
1. Install docker (on macOS, [Docker for Mac](https://docs.docker.com/docker-for-mac/) is suggested)
2. `docker pull dternyak/eth-priv-to-addr`

##### Run Derivation Checker
```bash
docker run -e key=<key_1>,<key_2>,<key_3> dternyak/eth-priv-to-addr:latest
```
