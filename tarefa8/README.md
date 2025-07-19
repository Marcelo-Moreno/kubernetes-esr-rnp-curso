# Tarefa 8 - Curso Kubernetes (ESR/RNP)

## Objetivo

- Criar um Deployment e um Service do tipo **ClusterIP** para o app `nginx`
- Criar um Deployment e um Service do tipo **NodePort** para o app `nginx2`
- Demonstrar o acesso interno e externo via `curl` e navegador

## Aplicação dos recursos

```bash
kubectl apply -f clusterip-nginx-deployment.yaml
kubectl apply -f clusterip-nginx-service.yaml
kubectl apply -f nodeport-nginx2-deployment.yaml
kubectl apply -f nodeport-nginx2-service.yaml
