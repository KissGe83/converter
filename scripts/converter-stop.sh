#!/bin/bash
microk8s kubectl delete -f ../k8s/converter-deployment.yaml
microk8s kubectl delete -f ../k8s/converter-service.yaml
microk8s kubectl delete -f ../k8s/converter-ingress.yaml
microk8s kubectl delete -f ../k8s/converter-hpa.yaml

