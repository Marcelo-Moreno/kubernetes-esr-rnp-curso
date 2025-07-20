Tarefa 9 — Resolução de Problemas e Monitoramento no Kubernetes

Curso: **Orquestração de Containers com Kubernetes — ESR/RNP**  
Sessão: **09 - Monitoramento e Observabilidade**  

---

## 🎯 Objetivo da Tarefa

Implementar soluções de monitoramento e observabilidade em um cluster Kubernetes por meio das ferramentas:

- [Kubebox](https://github.com/astefanutti/kubebox)
    
- [cAdvisor](https://github.com/google/cadvisor)
    
- [Grafana](https://grafana.com/)
    
- [Prometheus](https://prometheus.io/)
    
- Loki
    
- [Helm](https://helm.sh/)
    

---

## 📌 Etapas Realizadas

### 🟢 Parte 1 — Instalação do Kubebox + cAdvisor

- Instalação do Kubebox via binário no host `s2-master-1`
    
- Execução local do `kubebox` (modo CLI)
    
- Percebeu-se que as métricas não estavam disponíveis
    
- Instalação do cAdvisor como DaemonSet para coletar métricas de pods
    
- Validação do funcionamento das métricas no Kubebox
    
- Testes dos atalhos `e`, `r`, `Shift+e`, `Ctrl+e`
    
- Remoção do namespace `cadvisor` após uso
    

### 🟢 Parte 2 — Instalação do Helm e Loki Stack

- Instalação do Helm v3 no `s2-master-1`
    
- Criação do namespace `grafana`
    
- Adição do repositório oficial do Grafana no Helm
    
- Instalação do `loki-stack` via Helm (incluindo Prometheus, Loki, Grafana e Promtail)
    
- Verificação dos pods do stack no namespace `grafana`
    

### 🟢 Parte 3 — Exposição da Interface Web do Grafana

- Criação do serviço `loki-grafana-nodeport` com `NodePort` 30081
    
- Exposição do Grafana na URL: `http://192.168.68.21:30081/` (IP do worker node)
    
- Recuperação da senha do usuário `admin` via `kubectl get secret`
    
- Acesso bem-sucedido à interface web do Grafana
    

### 🟢 Parte 4 — Correção dos Data Sources do Grafana (Importante!)

- Erro ao testar o data source Prometheus:  
    `dial tcp: lookup loki-prometheus-server.grafana.svc: i/o timeout`
    
- Foi identificado que o pod do Grafana não conseguia resolver o DNS interno do serviço Prometheus
    
- Solução aplicada:
    
    - Identificação do IP do serviço Prometheus (`10.104.122.173`)
        
    - Atualização do arquivo `custom-values.yaml` para usar o IP diretamente na URL do data source
        
    - Reaplicação do Helm com:
        
        ```
        helm upgrade loki grafana/loki-stack -n grafana -f custom-values.yaml
        ```
        
- Após a correção, o teste do data source foi bem-sucedido (`Data source is working`)
    

### 🟢 Parte 5 — Importação Manual de Dashboards

- Erro ao tentar importar via URL direta (timeout)
    
- Diagnóstico confirmou que o pod do Grafana não tinha acesso à internet
    
- Solução adotada:
    
    - Download manual dos dashboards `.json` via `curl` no host
        
    - Upload manual dos arquivos via interface web do Grafana
        
- Dashboards importados:
    
    - Dashboard 3119: _Kubernetes cluster monitoring_
        
    - Dashboard 9135: _Kubernetes via Prometheus_
        
- Atribuição do data source Prometheus para renderizar os dashboards
    

### 🟢 Parte 6 — Correção de erro no `kubectl` em nó worker

- Erro ao executar `kubectl` no `s2-node-1`:  
    `The connection to the server localhost:8080 was refused - did you specify the right host or port?`
    
- Diagnóstico: o nó `s2-node-1` é um **worker**, e não possui configuração do `kubectl` para o cluster
    
- Solução:
    
    - Copiado o arquivo `/etc/kubernetes/admin.conf` do `s2-master-1` para o `s2-node-1`
        
    - Configurado como `~/.kube/config` no `s2-node-1`:
        
        ```
        scp /etc/kubernetes/admin.conf vagrant@s2-node-1:/tmp/admin.conf
        sudo cp /tmp/admin.conf ~/.kube/config
        sudo chown vagrant:vagrant ~/.kube/config
        chmod 600 ~/.kube/config
        ```
        
- Após isso, o comando `kubectl` funcionou corretamente no worker
    

---


## 📂 Arquivos presentes neste diretório

- `custom-values.yaml` — Arquivo usado para corrigir os data sources do Grafana (com IP direto do Prometheus)    
- `loki-grafana-nodeport.yaml` — Serviço `NodePort` para expor o Grafana na porta 30081    
- `Pasta JSON_dashboards` — Pasta contendo os arquivos de dashboard utilizados nesta tarefa (baixados manualmente)    
- `README.md` — Este documento
    

---

## ✅ Conclusão

A tarefa demonstrou habilidades essenciais de troubleshooting em Kubernetes, além de:

- Uso de ferramentas de monitoramento locais e remotas    
- Configuração de stack observability via Helm    
- Diagnóstico de problemas de DNS e conectividade em pods    
- Correção de data sources provisionados (via IP direto)    
- Importação de dashboards mesmo sem acesso à internet no pod    
- Correção de problemas com o `kubectl` em nós workers
    
Essa experiência é altamente aplicável a clusters reais e ambientes corporativos.

---

## 🔗 Links úteis

- [Helm](https://helm.sh/)    
- [Grafana](https://grafana.com/)    
- Loki Stack    
- [Prometheus](https://prometheus.io/)    
- [Kubebox](https://github.com/astefanutti/kubebox)
