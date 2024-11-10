# Step-by-Step Guide: Using Docker in CI/CD with GitLab CI

This document provides a step-by-step guide on how to integrate Docker with GitLab CI for continuous integration and deployment. It includes code snippets and explanations to help you set up a CI/CD pipeline that automatically builds and pushes Docker images to DockerHub.

## Introduction to DevOps and CI/CD

**DevOps** is a combination of Development and Operations aimed at shortening the development life cycle and delivering high-quality software continuously. Docker plays a crucial role in DevOps by ensuring consistent environments from development to production.

**CI/CD** (Continuous Integration/Continuous Deployment) pipelines automate the process of building, testing, and deploying applications, ensuring they run in the same environment, thus avoiding the "works on my machine" problem.

## Using Docker in CI/CD Pipelines

Docker is commonly used in CI/CD pipelines to ensure applications are built, tested, and distributed in a consistent environment. This accelerates the deployment process and reduces errors.

## Integration with GitLab CI

GitLab CI is a popular CI/CD platform that can be integrated with Docker. You can define CI/CD steps using a `.gitlab-ci.yml` file to build, test, and deploy your application as a Docker container.

### Example: GitLab CI for Auto Build and Push to DockerHub

Below is an example of a `.gitlab-ci.yml` file that automates the building and pushing of Docker images to DockerHub.

```yaml
image: docker:latest

services:
  - docker:dind

variables:
  DOCKER_DRIVER: overlay2
  DOCKER_IMAGE_NAME: $CI_REGISTRY_USER/tuto_fast # Replace with your image and repo name

before_script:
  - echo "$CI_REGISTRY_PASSWORD" | docker login -u "$CI_REGISTRY_USER" --password-stdin

build:
  stage: build
  script:
    - docker build -t $DOCKER_IMAGE_NAME:latest .
    - docker push $DOCKER_IMAGE_NAME:latest
```

### Explanation of the `.gitlab-ci.yml` File

1. **Image and Services**:
   - `image: docker:latest`: Specifies the Docker image to use for the CI job.
   - `services: - docker:dind`: Enables Docker-in-Docker service to run Docker commands within the GitLab CI runner.

2. **Variables**:
   - `DOCKER_DRIVER: overlay2`: Sets the Docker storage driver.
   - `DOCKER_IMAGE_NAME`: Defines the Docker image name using GitLab CI environment variables.

3. **Before Script**:
   - Logs into DockerHub using the `CI_REGISTRY_USER` and `CI_REGISTRY_PASSWORD` environment variables, which should be set in GitLab CI/CD settings.

4. **Build Stage**:
   - `docker build -t $DOCKER_IMAGE_NAME:latest .`: Builds the Docker image from the source code.
   - `docker push $DOCKER_IMAGE_NAME:latest`: Pushes the built image to DockerHub.

### Setting Up GitLab CI/CD

To use the `.gitlab-ci.yml` file:

1. **Add the File**: Include the `.gitlab-ci.yml` file in your Git repository.
2. **Set Environment Variables**: In GitLab, navigate to CI/CD settings and add `CI_REGISTRY_USER` and `CI_REGISTRY_PASSWORD` to store your DockerHub username and password securely.

With this setup, every push to the Git repository will trigger GitLab CI to automatically build a new Docker image and push it to DockerHub.

## Conclusion

This guide provides a comprehensive overview of integrating Docker with GitLab CI for automated CI/CD pipelines. By following these steps, you can ensure consistent and efficient deployment of your applications.

Feel free to reach out if you have any questions or need further assistance!