# Tarefa 6 - Curso Kubernetes (ESR/RNP)

## Objetivo
Criar e expor um registro Docker privado dentro do cluster Kubernetes, acessível via serviço interno.

## Estrutura criada

- Namespace: `private-registry`
- Deployment com `registry:2`
- Service do tipo `ClusterIP` na porta 5000
- Pod auxiliar `curl-pod` para testes

## Como testar

Entre no pod **curl-pod**:

```sh
kubectl exec -n private-registry -it curl-pod -- sh 
```

Dentro do pod **curl-pod:**
```sh
curl registry-service:5000/v2/
```

**Retorno esperado:**

`{}`
