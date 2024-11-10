# Step-by-Step Guide on Managing Docker Images and Containers

This document provides a step-by-step guide on managing Docker images and containers, as described in the subtitle file. It includes explanations of Docker concepts, commands, and best practices.

## Introduction to Docker Images and Containers

- **Docker Images**: A Docker image is a blueprint or a package that contains all the necessary packages, libraries, and applications ready to be executed.
- **Docker Containers**: A container is an instance that runs based on the blueprint provided by a Docker image.

## Managing Docker Images

### Viewing Docker Images

To view the list of Docker images available on your host, use the following command:

```bash
sudo docker images
```

This command will display a list of images that have been built or pulled on your local host.

### Removing Docker Images

If you need to remove an image to free up space, use the following command:

```bash
sudo docker rmi <image_name>
```

For example, to remove an image named `fast_app`, you would use:

```bash
sudo docker rmi fast_app
```

**Note**: Ensure that no containers are using the image before attempting to remove it.

### Checking for Residual Containers

If you encounter issues while pushing images, check for any residual containers using:

```bash
sudo docker ps -a
```

Remove any containers that are still referencing the image before deleting the image itself.

## Tagging Docker Images

Docker images can be tagged to manage versions or differentiate between builds. To add a new tag to an image, use:

```bash
sudo docker tag <existing_image>:<existing_tag> <new_image>:<new_tag>
```

For example, to tag an image `tutof` with a new version `v1.0`, use:

```bash
sudo docker tag tutof:latest tutof:v1.0
```

## Docker Layers

Docker uses a layered file system to build images. Each instruction in a Dockerfile creates a new layer. This system offers:

- **Efficiency**: Shared layers can be used across multiple images, saving space and download time.
- **Speed**: Only changed layers are rebuilt, speeding up the build process.
- **Transparency**: Each layer and its changes are visible, aiding in debugging and understanding the image contents.

## Logging into Docker Hub

To push images to Docker Hub, you must first log in:

```bash
sudo docker login
```

Enter your Docker Hub username and password when prompted.

## Pushing Docker Images to Docker Hub

Before pushing, ensure your image is tagged with your Docker Hub username:

```bash
sudo docker tag <image_name>:<tag> <username>/<image_name>:<tag>
```

Then push the image:

```bash
sudo docker push <username>/<image_name>:<tag>
```

For example:

```bash
sudo docker push yourusername/tutof:v1.0
```

## Conclusion

Understanding Docker images and containers, along with how Docker uses layers, prepares you to use Docker efficiently in software development. This guide provides the foundational steps to manage Docker images and containers effectively.

Thank you for following this guide. We hope it is beneficial for your Docker journey.