# Powershell Reverse TCP Payload Generator

By: Leonard Haddad

## Usage

### [Batchfile]

[Setup]:

* Change path_to_template_file in batchfile to the path containing the template file
* Change path_to_script in batchfile to the path containing the python file

[Usage]:

```
shellgen.cmd ip_address port

```

ip_address - Address that the payload should connect to using reverse connection (attacker IP address)
port       - The port to connect to

[Note]: When using the batch file, the path to the output file is set to the current directory, and the path to the template file is read out of the batch file

 
### [Python]

[Usage]:

```
shellgen.py export_path template_path ip_address port

```

export_path   - The path to export the payload.ps1 file to
template_path - Template file path (including filename and extension)
ip_address    - Attacker IP Address
port          - Attacker port

## Disclaimer

Privilege Escalation Exploit - By lokiuox on <a href="https://forums.hak5.org/topic/45439-powershell-real-uac-bypass">Hak5 Forums</a>
Powershell TCP Reverse Shell - By bascoe10 on <a href="https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md">Github</a>
