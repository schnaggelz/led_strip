# LED Strip

Benni's LED strips via Raspberry PI 3 (development) Raspberry PI Zero W ("productive").

**Child learning project**

## Web API

````
curl http://localhost:5000/api/set_text/1234 -d '{"text": "HALLO"}' -H 'Content-Type: application/json'
````

## Required packages on RPi

````
sudo apt install wget curl git python3-dev python3-pip
````

````
sudo pip3 install rpi_ws281x -v
````
