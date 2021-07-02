# Python File Transfer Tool

This is a super duper mega simple file transfer tool which may be used to transfer files between two different systems on the same network.

Note: The file is sent in an unencrypted manner, so DO NOT USE THIS ON A PUBLIC NETWORK / ACCROSS THE BIG EVIL WWB

## Usage

The sending PC acts as the server. The tool needs to be run with the IPv4 Address of the sending PC.

Sender:

```bash
./ptransfer own_ipv4_address
```

Receiver:

```bash
./ptransfer sender_ipv4_address
```

The mode Sender/Receiver needs to be picked after the above command is run (you will get a prompt). The sender needs to specify the full filename including the file extension. Note that the path of the sent file is relative to the current directory from which this script is run.

## Function

The file is read in and sent in chunks of up to 2 MB of data per cycle (speeds may be slower based on network performance). After the file is completely sent,
the hash of the original file on the server's end is computed and then sent to the receiving end to compare to the hash of the received file in order to insure data
integrity. If the hashes do not match, you will be prompted whether or not you want to keep the local file. 

## Author

Leonard Haddad

Provided in accords with the MIT License