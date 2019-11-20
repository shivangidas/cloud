## Installing docker on Mac

from https://runnable.com/docker/install-docker-on-macos

- Download Docker.
- Double-click the DMG file, and drag-and-drop Docker into your Applications folder.
- You need to authorize the installation with your system password.
- Double-click Docker.app to start Docker.
- The whale in your status bar indicates Docker is running and accessible.
- Docker presents some information on completing common tasks and links to the documentation.
- You can access settings and other options from the whale in the status bar.

## rabbitmq

<pre>docker pull rabbitmq:latest</pre>

## Run with docker-compose

<pre>docker-compose build 
docker-compose up --scale worker=2</pre>

## Or manually

- Run rabbitmq

<pre>
docker run --rm --name rabbit --env RABBITMQ_DEFAULT_USER=admin --env RABBITMQ_DEFAULT_PASS=mypass rabbitmq:latest</pre>

- build worker (make sure you're in the project path)

<pre>docker build . -t worker</pre>

- Link and start a worker

<pre>docker run --link rabbit -v $(pwd):/app worker</pre>

## Run the code

<pre>
docker exec -i -t < worker_name > /bin/bash
python -m container_app.submit_jobs</pre>

with arguments

<pre>
python -m container_app.submit_jobs (difficulty) (time_in_seconds) (number_of_tasks)
</pre>

## List things with docker

<pre> docker ps </pre>

## Kill containers

<pre>docker kill vigorous_haslett</pre>

Kill all

<pre>docker kill $(docker ps -a -q)</pre>

Remove all stopped containers

<pre>docker rm $(docker ps -a -q)</pre>
