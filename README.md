# Tux Says Script for Docker Image

This script gets an enviroment variable and displays it with Tux (just as `cowsays` or [docker/whalesays](https://hub.docker.com/r/docker/whalesay) Docker Image).

This script is intended for creating a Docker Image while I was learning Docker basics

### How to run the script

```bash
	# Store the environment variable
	export MSG=[your_message_without_spaces]

	# Linux and Mac
	python3 main.py
	# Windows (PowerShell)
	Python main.py
```

Remember that this script is not meant to be executed with the Python interpreter as shown, but is intended for use with Docker containers.
