#!/bin/bash
microk8s kubectl apply -f ../k8s/converter-deployment.yaml
microk8s kubectl apply -f ../k8s/converter-service.yaml
microk8s kubectl apply -f ../k8s/converter-hpa.yaml
microk8s kubectl apply -f ../k8s/converter-ingress.yaml


