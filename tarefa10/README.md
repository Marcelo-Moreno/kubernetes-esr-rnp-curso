# Tarefa 10 - Curso Kubernetes (ESR/RNP)

## Objetivo

Realizar o deploy de uma aplicação usando Helm, modificar parâmetros no `values.yaml`, aplicar o deploy com as novas configurações e registrar evidências.

## Aplicação escolhida

WordPress, utilizando o Helm Chart da Bitnami.

## Estrutura dos arquivos

- `pv-manual2.yaml`: PersistentVolume para o WordPress
- `pv-mariadb.yaml`: PersistentVolume para o MariaDB
- `pvc-wordpress.yaml`: PersistentVolumeClaim vinculado ao PV do WordPress
- `pvc-mariadb.yaml`: PersistentVolumeClaim vinculado ao PV do MariaDB
- `values.yaml`: Arquivo de configuração com parâmetros customizados para a aplicação

## Etapas realizadas

### 1. Criar o namespace
```bash
kubectl create namespace wordpress
```

### 2. Criar os PersistentVolumes e PersistentVolumeClaims
```bash
kubectl apply -f pv-manual2.yaml
kubectl apply -f pv-mariadb.yaml
kubectl apply -f pvc-wordpress.yaml
kubectl apply -f pvc-mariadb.yaml
```

### 3. Adicionar o repositório Bitnami e atualizar os charts
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

### 4. Realizar o deploy da aplicação WordPress com o `values.yaml` customizado
```bash
helm install meu-wordpress bitnami/wordpress -f values.yaml -n wordpress
```

### 5. Verificar os pods em execução
```bash
kubectl get pods -n wordpress
```

### 6. Acessar o site WordPress
```bash
export NODE_PORT=$(kubectl get svc meu-wordpress -n wordpress -o jsonpath="{.spec.ports[0].nodePort}")
export NODE_IP=$(kubectl get nodes -o jsonpath="{.items[0].status.addresses[0].address}")
echo "URL de acesso: http://$NODE_IP:$NODE_PORT"
```

### 7. Obter as credenciais de acesso
```bash
echo "Usuário: user"
kubectl get secret --namespace wordpress meu-wordpress -o jsonpath="{.data.wordpress-password}" | base64 -d && echo
```

## Personalizações realizadas

- Título do blog alterado para **"Meu Blog Kubernetes ESR"**
- Tipo de serviço definido como `NodePort`
- Uso de volumes persistentes configurado via PV/PVC manuais

## Observações finais

- As pastas `/mnt/data1` e `/mnt/data2` devem existir na máquina host e possuir permissões apropriadas (`chown -R 1001:1001`).
- Os pods só funcionarão corretamente se os volumes puderem ser acessados com permissões de escrita.
- O parâmetro `global.security.allowInsecureImages` foi definido como `true` para contornar validações do Helm Chart com imagens alternativas da Bitnami.
