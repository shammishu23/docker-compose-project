# DevOps CI/CD Pipeline Project 

This project demonstrates a complete CI/CD pipeline using Jenkins, Docker, and AWS EC2.

The pipeline automatically builds a Docker image, pushes it to Docker Hub, deploys the application to AWS EC2, performs health checks, and supports rollback to previous versions.

---

##  Technologies Used

- GitHub
- Jenkins
- Docker
- Docker Hub
- AWS EC2
- Linux
- Python Flask

---

##  CI/CD Pipeline Flow

1. Developer pushes code to GitHub
2. Jenkins triggers the pipeline
3. Docker image is built
4. Image is pushed to Docker Hub
5. Jenkins deploys the container to AWS EC2
6. Application health check is performed
7. Email notification is sent for build status

---

## 🔁 Rollback Feature

The pipeline supports manual rollback using Jenkins parameters.

Example:

ROLLBACK_TAG = build-24

This redeploys a previous Docker image version.

---

## 📦 Deployment

Application runs inside a Docker container on AWS EC2.


---

##  Pipeline Stages

- Clean Workspace
- Clone Repository
- Build Docker Image
- Push Image to Docker Hub
- Deploy to AWS EC2
- Application Health Check
- Email Notification

---

## Project Goal

The goal of this project is to understand how DevOps tools integrate together to automate build, deployment, and monitoring processes in a CI/CD workflow.

---

## Author

Sujitha Chadalavada
