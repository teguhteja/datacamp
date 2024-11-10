# Docker Basics: Step-by-Step Summary

This document provides a step-by-step summary of Docker basics, as described in the subtitle file. It includes explanations of key Docker components and commands, along with code snippets and their explanations.

## Key Components of Docker

1. **Docker Client**: 
   - The interface used by users to interact with Docker. When you run Docker commands, you are communicating with the Docker Daemon through the Docker Client.
   - Example command: `sudo docker run`

2. **Docker Daemon (Docker Engine)**:
   - A background process responsible for building, running, and managing containers. It can communicate with other daemons to manage containers across multiple hosts.

3. **Docker Image**:
   - A package containing all the necessary libraries and dependencies for an application, ready to be run as a container.

4. **Docker Container**:
   - An instance of a Docker Image, providing isolation for the application and its dependencies from the surrounding environment.

## Docker Commands

### Pulling an Image

To pull an image from a container registry, use the following command:

```bash
sudo docker pull nginx
```

- **Explanation**: This command pulls the `nginx` image from the Docker Hub, a public container registry. The `sudo` prefix is used for administrative privileges.

### Running a Container

To run a container from an image, use:

```bash
sudo docker run --name mynginx -d -p 8080:80 nginx
```

- **Explanation**:
  - `--name mynginx`: Assigns the name `mynginx` to the container.
  - `-d`: Runs the container in detached mode (in the background).
  - `-p 8080:80`: Maps port 8080 on the host to port 80 on the container, allowing access to the application via `localhost:8080`.

### Stopping a Container

To stop a running container, use:

```bash
sudo docker stop mynginx
```

- **Explanation**: Stops the container named `mynginx`. You can also use the container ID instead of the name.

### Starting a Container

To start a stopped container, use:

```bash
sudo docker start mynginx
```

- **Explanation**: Restarts the container `mynginx` with its previous configuration.

### Listing Containers

To list all running containers, use:

```bash
sudo docker ps
```

- **Explanation**: Displays a list of currently running containers, including their IDs, names, and status.

To list all containers, including stopped ones, use:

```bash
sudo docker ps -a
```

- **Explanation**: Shows all containers, whether they are running or stopped.

### Removing a Container

To remove a container, first stop it, then remove it:

```bash
sudo docker stop mynginx
sudo docker rm mynginx
```

- **Explanation**: Stops and then removes the container named `mynginx` from the system.

## Docker Hub and Registries

- **Docker Hub**: A public registry that stores various Docker images. Users can find official images, community-contributed images, and create their own accounts to store and share images.
- **Private Registries**: Organizations can use private registries to store Docker images in a controlled environment.

## Conclusion

Understanding these basic Docker components and commands provides a solid foundation for working with Docker. By mastering these, you can efficiently manage and deploy applications in isolated environments.

For further exploration, consider looking into Docker orchestration tools like Kubernetes, which can manage containerized applications at scale.