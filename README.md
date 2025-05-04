# ML Pipeline with Docker, Argo Workflows, ArgoCD and Google Kubernetes Engine

This project demonstrates a modular machine learning pipeline with three stages — **data preprocessing**, **model training**, and **evaluation** — orchestrated using **Argo Workflows** on **Google Kubernetes Engine (GKE)**. All pipeline steps are containerized with **Docker** and deployed via **GitOps** using **ArgoCD**.

##  Features

- ML pipeline split into modular containers for preprocessing, training, and evaluation
- Argo Workflows for Kubernetes-native orchestration
- Shared Persistent VolumeClaim for data transfer between steps
- Dockerized pipeline with images pushed to DockerHub
- GitOps-based deployment using ArgoCD
- Runs entirely on Google Kubernetes Engine (GKE)

##  Docker Setup

Each stage is containerized with its own Dockerfile.

To build and push:

```bash
# Example for preprocessing
cd preprocessing
docker build -t <dockerhub-username>/ml-preprocess .
docker push <dockerhub-username>/ml-preprocess
```
Repeat for training and evaluation

## GKE Setup
1. Create GKE Cluster

```bash
gcloud container clusters create ml-cluster \
  --num-nodes=3 \
  --region=us-central1
```

2. Connect to kubectl
```bash
gcloud container clusters get-credentials ml-cluster --region=us-central1
```
## Argo Setup
1. Install Argo Workflows
```bash
kubectl create namespace argo
kubectl apply -n argo -f https://github.com/argoproj/argo-workflows/releases/latest/download/install.yaml
```
2.Apply RBAC Fix
``` bash
kubectl apply -f argo-workflow-controller-cluster-role.yaml
 kubectl apply -f argo-rbac.yaml
```
3. Submit Workflow
``` bash
kubectl create -f workflow/ml-pipeline.yaml -n argo
```

4. Access Argo Workflows UI
```bash
kubectl -n argo port-forward svc/argo-server 2746:2746
```
![argoCD_UI](https://github.com/user-attachments/assets/35544875-9d01-429b-9215-42136f2cda44)

