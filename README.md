## Installing docker on Mac

from https://runnable.com/docker/install-docker-on-macos

- Download Docker.
- Double-click the DMG file, and drag-and-drop Docker into your Applications folder.
- You need to authorize the installation with your system password.
- Double-click Docker.app to start Docker.
- The whale in your status bar indicates Docker is running and accessible.
- Docker presents some information on completing common tasks and links to the documentation.
- You can access settings and other options from the whale in the status bar.

### Run rabbitmq

docker run --rm --name rabbit --env RABBITMQ_DEFAULT_USER=admin --env RABBITMQ_DEFAULT_PASS=mypass rabbitmq:latest

### build worker (make sure you're in the project path)

docker build . -t worker

### Link and start a worker

<pre>docker run --link rabbit -v $(pwd):/app worker</pre>

### Run the code

docker exec -i -t <worker_name> /bin/bash

python -m container_app.submit_jobs

## List things with docker

docker ps

## kill containers

docker kill vigorous_haslett
