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

## List of available Distros

This script has a Java GUI-Equivalent, as well as an Android app. Here is a list of available distros:

<ul style="margin-bottom: 10px;">
	<li><a target="_blank" rel="noopener noreferrer" href="https://github.com/leolion3/Simple-File-Transfer-PC/releases"><i class="fa-solid fa-desktop"></i> PC Release <i class="fa fa-external-link"></i></a></li>
	<li><a target="_blank" rel="noopener noreferrer" href="https://play.google.com/store/apps/details?id=software.isratech.filetransferos"><i class="fa-solid fa-mobile"></i> Android App <i class="fa fa-external-link"></i></a></li>
	<li><a target="_blank" rel="noopener noreferrer" href="https://github.com/leolion3/Portfolio/tree/master/Python/FileSender"><i class="fa-solid fa-terminal"></i> Python CLI Tool <i class="fa fa-external-link"></i></a></li>
	<li><a target="_blank" rel="noopener noreferrer" href="https://github.com/leolion3/Simple-File-Transfer-PC"><i class="fa-solid fa-code"></i> PC Source <i class="fa fa-external-link"></i></a></li>
	<li><a href="https://github.com/leolion3/Simple-File-Transferer-Android" target="_blank"><i class="fa-solid fa-code"></i> Android Source <i class="fa fa-external-link"></i></a></li>
	</ul>
</li>

## Author

Leonard Haddad

Provided in accords with the MIT License

## Network Protocol

The script uses a proprietary protocol through TCP. The exchanged messages are displayed below. In hindsight, it would've been smarter to use JSON for information exchange (or refrain from using sockets in the first place in favour of TLS), perhaps it will get updated in the future, stay tuned!

Before doing a transfer, the server allows pings to be received to support the scan feature of mobile and java clients. Here is the initial protocol step (**A** is the **sender**/server, **B** the **receiver**/client):

$$B\rightarrow A:\text{PING}$$
$$A\rightarrow B:\text{REPLY}$$

If **B** sends a ping, it receives a reply from the server, otherwise (if it sends **init**) the following messages are exchanged:

$$B\rightarrow A:\text{"init"}$$
$$A\rightarrow B:\text{File name}$$
$$B\rightarrow A:\text{"Received Name"}$$
$$A\rightarrow B:\text{File size}$$

At this point the client has the file name and size. Now they proceed to check whether the file already exists, and if so, read the existing *n*-bytes into a new file, while renaming the existing file into `file name_old.ext`. 

The next message sent to **A** is either of:

$$B\rightarrow A:\text{"NONEXISTENT"}$$

or

$$B\rightarrow A:\text{"SIZE:current\textunderscore size"}$$

If the file exists, the server proceeds sending the remaining *m-n* bytes of the file, otherwise, it sends all *m*-bytes of the file.

$$A\rightarrow B:\text{"Ready for transfer!"}$$
$$B\rightarrow A:\text{"Beginning file transfer..." (printed on client side)}$$
$$A\rightarrow B:\text{File data in chunks of 2MB}$$

(\*) The client calculates the received data by himself. After receiving all *m*-bytes of the file, the client checks the file hash against that of the server.

$$B\rightarrow A:\text{"GIVE\textunderscore ME\textunderscore HASH"}$$
$$A\rightarrow B:\text{Original file hash}$$

If the hashes dont match, the client prompts for deletion of the data.

With the last message, the connection terminates.