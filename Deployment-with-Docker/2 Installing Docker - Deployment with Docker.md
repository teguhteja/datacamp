# Docker Installation Guide on Linux

## Introduction

Welcome to the second part of the "Deployment with Docker" course. In this section, we will discuss the steps required to install Docker on a Linux system. Before proceeding with the installation, it is important to ensure that your system meets the necessary requirements.

## System Requirements

- **Supported Operating Systems:** Linux distributions such as Ubuntu, CentOS, or Debian. Docker is also available for Windows and macOS, but our focus here is on Linux.
- **Kernel Version:** Linux kernel version 3.10 or newer.
- **CPU:** 64-bit processor.
- **Memory:** Minimum of 512 MB RAM, with 4 GB or more recommended for production environments.

## Installation Steps

### Step 1: Update Package Index

First, update the package index on your system to ensure you have the latest package information.

```bash
sudo apt-get update
```

### Step 2: Install Required Packages

Install the necessary packages for Docker. This includes `docker-ce`, `docker-ce-cli`, `containerd.io`, `docker-buildx-plugin`, and `docker-compose-plugin`.

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

**Explanation:**
- `docker-ce`: Docker Community Edition, the core Docker software.
- `docker-ce-cli`: Command-line interface for Docker.
- `containerd.io`: A container runtime required by Docker.
- `docker-buildx-plugin`: A plugin for building Docker images.
- `docker-compose-plugin`: A plugin for running multi-container Docker applications.

### Step 3: Verify Installation

After installation, verify that Docker is installed correctly by running the following command:

```bash
sudo docker run hello-world
```

**Explanation:**
- This command runs a test container that prints a "Hello from Docker!" message, indicating that Docker is installed and functioning correctly.

## Recommendations

- **Linux Installation:** It is recommended to install Docker Engine on Linux rather than Docker Desktop for better performance and stability.
- **Windows Installation:** For Windows users, installing Docker Desktop is suggested as it simplifies the installation process.

## Conclusion

By following these steps, you should have successfully installed Docker on your Linux system. Thank you for following along, and see you in the next video!

---

*Note: If you encounter any errors during installation, ensure that your system meets all the requirements and that you have administrative privileges to install software.*