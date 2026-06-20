# SynapseGrid
## A DevOps-Driven Healthcare Management System

SynapseGrid is a healthcare management platform developed to demonstrate both business application development and modern DevOps practices. The project integrates healthcare services such as patient management, appointments, doctors, pharmacy, and emergency services with containerization, build automation, orchestration, and monitoring technologies.

---

## Project Objective

The objective of SynapseGrid is to develop a small but functional healthcare application and implement the complete DevOps lifecycle around it.

The project demonstrates:

- Healthcare service management
- REST API development
- PostgreSQL database integration
- Docker containerization
- Docker Compose multi-container management
- Jenkins Continuous Integration
- Kubernetes orchestration
- Prometheus monitoring

---

# Features

- Patient Management
- Appointment Management
- Doctor Management
- Pharmacy Management
- Emergency Services
- Database Health Check
- Dockerized Deployment
- Jenkins Build Automation
- Kubernetes Configuration
- Prometheus Monitoring

---

# Technology Stack

## Backend

- Flask
- Python

## Database

- PostgreSQL

## DevOps

- Docker
- Docker Compose
- Jenkins
- Kubernetes
- Prometheus
- Vault
- Terraform

---

# Project Structure

```
SynapseGrid/

│
├── app/
│   ├── static/
│   ├── templates/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── backups/
│
├── documentation/
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── logs/
│
├── docker-compose.yml
│
└── README.md
```

---

# API Endpoints

## Home

```
/
```

---

## Database Status

```
/dbstatus
```

---

## Patients

```
/patientsdb
```

---

## Appointments

```
/appointmentsdb
```

---

## Doctors

```
/doctorsdb
```

---

## Pharmacy

```
/pharmacydb
```

---

## Emergency

```
/emergencydb
```

---

# Running the Project

## Start Application

```bash
docker compose up -d
```

---

## Start Jenkins

```bash
docker start synapsegrid-jenkins
```

Dashboard:

```
http://localhost:8080
```

---

## Start Prometheus

```bash
docker start synapsegrid-prometheus
```

Dashboard:

```
http://localhost:9090
```

---

# Verify Application

Application:

```
http://localhost:5001
```

Database:

```
http://localhost:5001/dbstatus
```

Patients:

```
http://localhost:5001/patientsdb
```

Appointments:

```
http://localhost:5001/appointmentsdb
```

Doctors:

```
http://localhost:5001/doctorsdb
```

Pharmacy:

```
http://localhost:5001/pharmacydb
```

Emergency:

```
http://localhost:5001/emergencydb
```

---

# Kubernetes

Apply deployment:

```bash
kubectl apply -f k8s/deployment.yaml
```

Apply service:

```bash
kubectl apply -f k8s/service.yaml
```

Verify:

```bash
kubectl get nodes
```

---

# Jenkins

Open Jenkins Dashboard:

```
http://localhost:8080
```

Run:

```
SynapseGrid-CI
```

Click:

```
Build Now
```

Expected:

```
Finished: SUCCESS
```

---

# Monitoring

Prometheus Dashboard:

```
http://localhost:9090
```

---

# System Architecture

SynapseGrid follows a layered architecture:

Users

↓

Flask Application

↓

REST APIs

↓

PostgreSQL Database

↓

Docker

↓

Docker Compose

↓

Jenkins

↓

Kubernetes

↓

Prometheus

---

# Future Enhancements

- User Authentication
- Cloud Deployment
- Mobile Application
- AI-assisted Healthcare
- Advanced Monitoring
- Real-time Notifications

---

# Author

Viketh Hegde

B.Tech Computer Science Engineering

Academic Year 2025–26

---

# License

This project is developed for educational and academic purposes.