# Tarefa 5 - Curso Kubernetes - (ESR/RNP)

## Objetivo

Demonstrar uso de `Deployment`, `rollout`, `update` e `rollback` no Kubernetes.

## Etapas

1. Criação do deployment com 10 réplicas
2. Rollout inicial
3. Atualização da imagem
4. Rollout da nova versão
5. Rollback para versão anterior

## Comandos utilizados

```bash
kubectl apply -f nginx-deployment.yaml
kubectl get deployments
kubectl get pods -o wide
kubectl rollout status deployment/nginx-deploy
kubectl set image deployment/nginx-deploy nginx=nginx:1.25
kubectl rollout history deployment/nginx-deploy
kubectl rollout undo deployment/nginx-deploy
kubectl describe deployment nginx-deploy
