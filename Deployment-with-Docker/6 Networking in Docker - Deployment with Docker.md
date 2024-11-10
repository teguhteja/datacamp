# Docker Networking Summary

This document provides a step-by-step summary of Docker networking, focusing on Bridge, Host, and Overlay networks. It includes code examples and explanations to help understand how to manage and utilize Docker networks effectively.

## 1. Introduction to Docker Networking

Docker provides features to manage networks between containers and between containers and external networks. Using commands like `docker network`, you can create, inspect, and manage networks in your Docker environment.

## 2. Types of Docker Networks

### 2.1 Bridge Network

- **Description**: The Bridge network is the default network type when you run a container without specifying a network. It allows containers to communicate with each other but isolates them from the host network.

- **Creating a Bridge Network**:
  ```bash
  docker network create --driver bridge my_bridge_network
  ```
  **Explanation**: This command creates a new Bridge network named `my_bridge_network`. The `--driver bridge` option specifies the network type.

- **Running Containers on a Bridge Network**:
  ```bash
  docker run -d --name my_nginx --network my_bridge_network nginx
  docker run -d --name my_app --network my_bridge_network my_app_image
  ```
  **Explanation**: These commands run two containers (`my_nginx` and `my_app`) on the `my_bridge_network`. They can communicate with each other using their container names.

### 2.2 Host Network

- **Description**: In Host network mode, a container shares the network stack with the host. This is useful for certain applications but is less secure as containers can access host ports directly.

- **Running a Container with Host Network**:
  ```bash
  docker run --network host my_app_image
  ```
  **Explanation**: This command runs a container using the host's network stack. It can directly access the host's network interfaces.

### 2.3 Overlay Network

- **Description**: Overlay networks are used for Docker Swarm, allowing communication between containers on different hosts. This is suitable for large-scale orchestration.

- **Note**: Overlay networks are beyond the scope of this basic course, as they require a Docker Swarm setup.

## 3. Exposing and Linking Containers

- **Exposing Ports**:
  ```bash
  docker run -d -p 8080:80 nginx
  ```
  **Explanation**: This command maps port 80 of the `nginx` container to port 8080 on the host, making the container's web server accessible via the host's IP on port 8080.

- **Linking Containers**:
  ```bash
  docker network connect my_bridge_network my_container
  ```
  **Explanation**: This command connects an existing container to a specified network, allowing it to communicate with other containers on that network.

## 4. Conclusion

Docker networking provides flexible options for container communication and isolation. By understanding and utilizing Bridge, Host, and Overlay networks, you can effectively manage containerized applications in various environments.

For more advanced networking setups, consider exploring Docker Compose and Docker Swarm, which offer more structured and scalable solutions.

---

Thank you for reading this summary. We hope it helps you in your Docker networking endeavors!