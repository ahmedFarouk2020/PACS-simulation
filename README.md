# PACS-simulation
Simple client-server-database interaction

# Functionalities
* Sending image data
* Ping server

# Improvements
* Better GUI
* Better control for user
* timeout
* Waiting drawings
* Closing connection by client

# Setup

1. From the command line create a virtual environment and activate.
```sh
# Windows (CMD)
> python -m venv .venv
> .venv\Scripts\activate

# Linux
> python3 -m venv .venv
> source .venv/bin/activate
```

2. Install dependencies **No dependencies


3. Run the server.
```sh
> cd <folder-containing-program-files>
> python server.py --optional <ip address> <port number>
```

4. Run the client.
```sh
> cd <folder-containing-program-files>
> python client.py --optional <ip address> <port number>
```
