# Python File Transfer Tool

This is a super duper mega simple file transfer tool which may be used to transfer files between two different systems on the same network.

(\*) Note: The file is sent in an unencrypted manner.

## Usage

The script can be ran in either send or receive mode, with either the sender or the receiver acting as the host.

It can either be ran with all arguments given when running the command, or by merely supplying the ip address and setting the remaining variables through prompts.

Syntax:

```bash
ptransfer <IP Address> [[s]end/[r]eceive] [reversed (T/F)] [filepath] [port]
```

- IP Address: The Interface to listen on/connect to.
- Mode (Optional): \[s]end or \[r]eceive.
- Reversed (Optional): \[f]alse or \[t]rue. Usually the sender acts as the server, but this can be reversed on machines where opening a port is disallowed.
- Filepath (Optional): Path to the file to send.
- Port (Optional): Port to connect to/listen on.

Note: While the arguments are optional, it is mandatory to include them in a row (script does not use getopt!). If the port is supplied, then all arguments preceeding it need to be supplied as well!

Running without arguments:

```bash
#> ptransfer 127.0.0.1
Please select type send/receive
#> r
Would you like to run in reverse connection mode (sender connects to receiver)?
- True: Receiver must start script FIRST.
- False (default): Sender must start script FIRST.
(*) Note: Android and Java variants dont support reverse mode!
(True/False) #> f
```

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

$$B\rightarrow A:\text{"SIZE:current size"}$$

If the file exists, the server proceeds sending the remaining *m-n* bytes of the file, otherwise, it sends all *m*-bytes of the file.

$$A\rightarrow B:\text{"Ready for transfer!"}$$

$$B\rightarrow A:\text{"Beginning file transfer..." (printed on client side)}$$

$$A\rightarrow B:\text{File data in chunks of 2MB}$$

(\*) The client calculates the received data by himself. After receiving all *m*-bytes of the file, the client checks the file hash against that of the server.

$$B\rightarrow A:\text{"GIVE ME HASH"}$$

$$A\rightarrow B:\text{Original file hash}$$

If the hashes dont match, the client prompts for deletion of the data.

With the last message, the connection terminates.