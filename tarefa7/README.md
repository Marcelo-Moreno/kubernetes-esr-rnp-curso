# Tarefa 7 - Curso Kubernetes (ESR/RNP)

## Objetivo

Esta tarefa faz parte da Sessão 7 do curso de Kubernetes da ESR/RNP e tem como objetivo explorar os recursos de armazenamento do Kubernetes. São abordados os conceitos e práticas relacionadas a:

- Volumes persistentes (PV)
- Requisições de volumes (PVC)
- StorageClasses
- Provisionamento manual e dinâmico de volumes
- Montagem de volumes em pods
- Utilização de subPath com Downward API

---

## Estrutura dos arquivos

| Arquivo | Descrição |
|--------|-----------|
| `author.yaml` | `Deployment` com 2 réplicas, que montam dois PVCs: `novel` e `events`. Utiliza `subPathExpr` com variável de ambiente `POD_NAME` para isolar diretórios. Aplica `podAntiAffinity`. |
| `writer.yaml` | Pod simples que monta o PVC `dynamic-pvc-data` e simula escrita em `/data`. |
| `pv-data.yaml` | Define um `PersistentVolume` com `hostPath` local e modo `ReadWriteMany`. |
| `pvc-data.yaml` | Cria um `PersistentVolumeClaim` associado ao `pv-data.yaml`. |
| `sc-data.yaml` | Define uma `StorageClass` manual (`no-provisioner`) com binding no `first consumer`. |
| `sc-pv-data.yaml` | PV com `local path` e `nodeAffinity` forçando agendamento no nó `s2-node-1`. Usa a `StorageClass` `sc-data`. |
| `sc-pvc-data.yaml` | PVC que usa a `StorageClass` `sc-data`. Requisição de 250Mi com `ReadWriteOnce`. |
| `dynamic-pvc-data.yaml` | PVC com provisionamento dinâmico via `nfs-client`, modo `ReadWriteMany`, usado no `writer.yaml`. |
| `novel.yaml` | PVC com `nfs-client`, 200Mi, também montado no `author.yaml`. |

---

## Ambiente utilizado

- Control Plane: `s2-master-1`
- Worker Node: `s2-node-1`
- Provisionamento local e dinâmico com suporte ao plugin `nfs-client`
- CNI com plugins instalados manualmente em `/opt/cni/bin` (loopback, etc)

---

## Aplicando os arquivos

```bash
# Exemplo de aplicação dos manifests
kubectl apply -f pv-data.yaml
kubectl apply -f pvc-data.yaml
kubectl apply -f sc-data.yaml
kubectl apply -f sc-pv-data.yaml
kubectl apply -f sc-pvc-data.yaml
kubectl apply -f dynamic-pvc-data.yaml
kubectl apply -f novel.yaml
kubectl apply -f writer.yaml
kubectl apply -f author.yaml
