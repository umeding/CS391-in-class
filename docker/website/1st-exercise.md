# Containerizing a web site

## Prerequisites

* Basic understanding of command-line/terminal usage.
* Docker Desktop (or Docker Engine on Linux) installed and running, run this to
  check (and get the version)
* A simple text editor (like VS Code, Sublime Text, Notepad++, nano, vim).
* Internet access (to download images from Docker Hub).


## Setup: ensure Docker runs

Open your terminal or command prompt.
Run 
```bash
$ docker --version
```

to confirm Docker is installed and accessible.

Run the classic Docker test:

```bash
$ docker run hello-world
```

Observe the output. This command downloads the `hello-world` image (if not
present locally) and runs it in a container. The container prints a message and
exits.

## Task 1: Running a Pre-built Image (Nginx)

In this step we will run a pre-built applications image. `Nginx` is a popular
web server you may want to use to deploy and run your Spark!Bytes application.

Pay attention to the `docker run` flags:

* `-d` (detached): Run the container in the background.
* `-p host_port:container_port`: Map a port on your host machine to a port
  inside the container. Nginx listens on port 80 by default inside its
  container.
* `--name`: Give the container a memorable name.

```bash
# Use port 8080 on your machine, mapping it to port 80 in the container
docker run -d -p 8080:80 --name my-nginx-server nginx:alpine
```


Note: If port `8080` is already in use on your machine, choose a different host
port (e.g. `8081`, `9000`) like `-p 9000:80`. The `:80` part refers to the port
inside the container and usually stays the same for standard images like Nginx.
Open a web browser on your computer and navigate to
[`http://localhost:8080`](http://localhost:8080)
(or the host port you chose). You should see the default Nginx welcome page.

Back in the terminal, see the running container:
```bash
docker ps
```
 (You should see my-nginx-server listed).

Stop the container:

```bash
docker stop my-nginx-server
```

Verify it's stopped (it shouldn't appear in `docker ps` anymore, but will appear
in `docker ps -a` which shows all containers, including stopped ones).

## Task 2: Preparing the Application & Dockerfile

Create a new folder for this project (e.g. `my-docker-app`). Navigate into it in
your terminal.  Inside `my-docker-app`, create a file named `index.html` with
the following content:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My Docker App</title>
  <style> body { font-family: sans-serif; background-color: #lightcyan; } </style>
</head>
<body>
  <h1>Hello from My Own Docker Container!</h1>
  <p>This HTML file was built into a Docker image.</p>
  <p>Current date might be: Thursday, April 17, 2025.</p>
</body>
</html>
```

In the same `my-docker-app` folder, create a file named `Dockerfile` (exactly
that name, no extension) with the following content:

```Dockerfile
# Step 1: Specify the base image
FROM nginx:alpine

# Step 2: Copy our index.html into the Nginx default web root directory
# Format: COPY <source_on_host> <destination_in_image>
COPY index.html /usr/share/nginx/html/index.html

# Step 3: (Optional but good practice) Tell Docker the container listens on port 80
EXPOSE 80

# The nginx:alpine base image already has a CMD to start Nginx,
# so we don't need to specify one here.
```

__Note__: Dockerfile instructions:

* __FROM__: Sets the base image (like inheriting from a class). We're building
  on top of Nginx.
* __COPY__: Copies files from your build context (the `my-docker-app` folder)
  into the image's filesystem.
* __EXPOSE__: Informs Docker which ports the container will listen on (mainly
  for documentation and helps some tools). Doesn't actually publish the port.

## Task 3: Building & Running the Custom Image

We will use the `docker build` command to create an image from a `Dockerfile`.

* `-t <name>:<tag>`: Tag the image with a name and optional tag (like a version,
  latest is default).
* `.`: The build context (the current directory, where `Dockerfile` and
  `index.html` are).

Make sure you are in the `my-docker-app` directory in your terminal.

Build the Docker image: (Don't miss the . at the end!)

```bash
docker build -t my-simple-web:v1 .
```

Watch the output as Docker executes the steps in the Dockerfile. List your
local Docker images to see the new one:

```bash
docker images
```

You should see `my-simple-web` with tag `v1`.

Now, run a container from your custom image: (Using host port 8888, feel free to
change if needed).

```bash
docker run -d -p 8888:80 --name my-app-container my-simple-web:v1
```

Open your web browser and navigate to `http://localhost:8888`. You should see
your custom HTML page!  Check running containers: `docker ps`

## Wrap-up & Cleanup

Review the key commands used: `docker run`, `docker ps`, `docker stop`, `docker
build`, `docker images`.

Process recap:

1. Write app code
1. Write Dockerfile instructions
1. Build Image
1. Run Container from Image.

Stop the custom container:

```bash
docker stop my-app-container
```

Cleanup (Optional but recommended): Remove the containers you created.

```bash
# Remove containers by name
docker rm my-app-container
docker rm my-nginx-server

# Or remove all stopped containers (useful shortcut)
# docker rm $(docker ps -aq)
```

Cleanup Images (Optional): use `docker rmi <image_name_or_id>`, 
*Suggestion*: keep them for now - do this at some later point.

```bash
# docker rmi my-simple-web:v1
# docker rmi nginx:alpine
# docker rmi hello-world
```
