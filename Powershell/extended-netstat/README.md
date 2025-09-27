# Netstat Connections Monitor

This tool can be used to monitor active connections, figure out which services they are coming from, and use DNS reverse lookup to find server names for connected services.

Optionally, the output can be exported to a csv file.

# Usage

```powershell
./scan-connections.ps1 [Optional CSV Export Path]
```

# Output

The connected services are output in a list. Entries from services that have not been logged before are highlighted in yellow.
The list takes a minute to populate due to the DNS reverse lookup and is refreshed every 90 seconds.

```
Proto PID    Process/Service                          Remote                Port   State      DNS                       
--------------------------------------------------------------------------------------------------------------
TCP  6732   aswToolsSvc                              xxx.xxx.xx.0          443    Established 
TCP  6276   AvastSvc                                 x.xx.xx.xxx           443    Established xx-xx-xx-xxx.deploy.static.akamaitechnologies.com
TCP  6276   AvastSvc                                 xx.xxx.xxx.xx         443    Established xx.xxx.xxx.xx.bc.googleusercontent.com
... Other entries ...
```
