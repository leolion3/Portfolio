# MiniHTTPServer

A minimal python HTTP Server (similar to the built in module `http.server`).

Supports only GET requests and requires no external libraries.

Provided by Leonard Haddad in accords with the MIT License.

## Usage

The server runs on port `80` and listens on all interfaces (`0.0.0.0`) by default.

To change this, execute the script while adding the IP address and ports to listen on.

```bash
./server # serves http on http://0.0.0.0:80 
./server 8080 # serves http on http://0.0.0.0:8080
./server 127.0.0.1 8080 # serves http on http://127.0.0.1:8080
```  