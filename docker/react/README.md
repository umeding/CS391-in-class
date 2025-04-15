# Containerizing a React Application

## Prerequisites

* Docker Desktop (or Docker Engine on Linux) installed and running (`docker
  --version`).
* `Node.js` and npm/npx installed (`node -v`, `npm -v`). `create-react-app`
  requires Node.js.
* vscode


## Introduction / Motivation

__The challenge__: React apps aren't just static files initially. They need a
`Node.js` environment to install dependencies (`npm install`) and build
optimized static files (`npm run build`). We don't want Node.js in our final
production image if we just need a web server.

__NOTE__: Check into Multi-stage Docker Builds: Using intermediate stages (like
a builder stage with Node.js) to prepare assets, and then copying only the
necessary results into a final, lightweight production stage (like Nginx).

## Task 1: Quick Pre-built Image Demo (Nginx)

This is to make sure all software (`docker`, etc) runs as intended. In case you
haven't done so, stop and remove things from the previous exercise.

__Hint__: Check it's running: `docker ps` (Optional: check http://localhost:8080).
Stop and remove it: use `bash` commands
Additional hints: remember/see `docker run, ps, stop, rm` commands.

## Task 2: Create React App & Multi-stage Dockerfile

Create/Build the React App: Navigate to `react` directory in the terminal.  Run
`create-react-app` (this is already done) and build it. It is the default
"`hello world`" application. This may take a couple mins:

```bash
$ npm install
```

(Optional) You can quickly run npm start here to see the default React app, then stop it with Ctrl+C.

Create the Dockerfile:

In the `my-react-docker-app` directory (alongside `package.json`, `src`, etc.), create a file named `Dockerfile` (no extension).
Paste the following content into `Dockerfile`:

```Dockerfile
# Stage 1: Build the React application
FROM node:18-alpine AS builder
# 'AS builder' names this stage

# Set the working directory inside the image
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock)
# Copying these first leverages Docker cache if dependencies haven't changed
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the application for production
RUN npm run build
# This creates optimized static files in the /app/build directory

# ---

# Stage 2: Serve the static files with Nginx
FROM nginx:1.25-alpine
# Use a lightweight Nginx image for the final stage

# Copy the built static files from the 'builder' stage
# Format: COPY --from=<stage_name> <source_in_stage> <destination_in_final_image>
COPY --from=builder /app/build /usr/share/nginx/html

# (Optional) If using React Router, you'd need a custom nginx.conf here
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80 (standard HTTP port Nginx listens on)
EXPOSE 80

# Default CMD from nginx image starts the server. No need to add one.
# CMD ["nginx", "-g", "daemon off;"] is implicitly included.
```

`Dockerfile` Notes: 

* Stage 1 (builder): Uses `node:18-alpine`, sets `WORKDIR`, copies
  `package*.json` then `npm install` (cache optimization!), copies remaining
  source code, runs `npm run build`. Remember everything here is temporary
  except the `/app/build` folder contents.
* Stage 2: Starts fresh `FROM nginx:1.25-alpine`. Crucially uses `COPY
  --from=builder` to grab only the built assets from Stage 1 into the Nginx web
  root. Finally, `EXPOSE 80` (port 80) to connect to nginx.

## Task 3: Build & Run the Custom React App Image

Now build the image from the multi-stage Dockerfile and run it.

Make sure you are still in the `my-react-docker-app` directory in your terminal.
Build the image:Bash

```bash
# Tag it as my-react-docker-app version 1
docker build -t my-react-docker-app:v1 .
```

Observe the output. You'll see steps for both Stage 1 and Stage 2 executing.
Notice intermediate containers being removed.

List images: Verify your image was created:

```bash
docker images
```
(Look for `my-react-docker-app` with tag `v1`. Compare its size to the node
image - it should be much smaller).


Run the container:
```bash
# Map host port 3000 to container port 80 (Nginx's default)
docker run -d -p 3000:80 --name my-running-react-app my-react-docker-app:v1
```

* __Note__: Using host port `3000` as it's common for React dev, but any available port works.
* __Verify__: Open your web browser and navigate to `http://localhost:3000`. You
  should see the default Create React App welcome page, now served by Nginx
  within your container!

Check the running container:

```bash
docker ps
```

## Wrap-up and Spark!Bytes

Review these key commands: `docker build`, `docker run`, `docker ps`, `docker
images`, `docker stop`, `docker rm`.

Remember the benefits of multi-stage builds for your __Spark!Bytes__ project:
create a small, optimized production image without `Node.js`, build tools, or
source code, just Nginx and the static assets.

Other possible steps for Spark!Bytes (highly depends on the architecture you chose):

* Use custom `nginx.conf` for React Router
* environment variables
* volumes for data persistence
* Docker Compose for multi-container apps (frontend + backend)
