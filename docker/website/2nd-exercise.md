# Containerizing a React application

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
Instructor: Quickly demonstrate running/stopping a pre-built image to reinforce basic commands.
Students:
Run Nginx briefly:Bash
Check it's running: docker ps (Optional: check http://localhost:8080).
Stop and remove it:Bash
Instructor Note: This just ensures they remember/see run, ps, stop, rm in action.

## Task 2: Create React App & Multi-stage Dockerfile 
Instructor: Guide students through creating a basic React app and then the Dockerfile. Explain each part of the multi-stage file.
Students:
Create the React App:
Navigate to a suitable directory (e.g., your Desktop or a development folder) in the terminal.
Run create-react-app (this might take a few minutes):Bash
Change into the new directory:Bash
(Optional) You can quickly run npm start here to see the default React app, then stop it with Ctrl+C.
Create the Dockerfile:
In the my-react-docker-app directory (alongside package.json, src, etc.), create a file named Dockerfile (no extension).
Paste the following content into Dockerfile:
Dockerfile
Instructor Note: Explain each section carefully:
Stage 1 (builder): Uses node:18-alpine, sets WORKDIR, copies package*.json then npm install (cache optimization!), copies remaining source code, runs npm run build. Explain that everything here is temporary except the /app/build folder contents.
Stage 2: Starts fresh FROM nginx:1.25-alpine. Crucially uses COPY --from=builder to grab only the built assets from Stage 1 into the Nginx web root. EXPOSE 80.

Step 4: Task 3 - Build & Run the Custom React App Image (10 mins)
Instructor: Guide students through building the image from the multi-stage Dockerfile and running it.
Students:
Make sure you are still in the my-react-docker-app directory in your terminal.
Build the image:Bash
Observe the output. You'll see steps for both Stage 1 and Stage 2 executing. Notice intermediate containers being removed.
List images: Verify your image was created:Bash(Look for my-react-docker-app with tag v1. Compare its size to the node image if you like - it should be much smaller).
Run the container:Bash
Note: Using host port 3000 as it's common for React dev, but any available port works.
Verify: Open your web browser and navigate to http://localhost:3000. You should see the default Create React App welcome page, now served by Nginx within your container!
Check the running container: docker ps

Step 5: Wrap-up & Cleanup (5 mins)
Instructor:
Review key commands: docker build, docker run, docker ps, docker images, docker stop, docker rm.
Reiterate the benefit of multi-stage builds: created a small, optimized production image without Node.js, build tools, or source code, just Nginx and the static assets.
Mention next steps: Using custom nginx.conf for React Router, environment variables, volumes for data persistence, Docker Compose for multi-container apps.
