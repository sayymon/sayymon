descreva de forma sucinta e simples o que é para que serve quando utilizar e os principais conceitos envolvidos



## Virtualização

**O que é?**

Virtualização é criar uma versão virtual (em software) de algo físico, como um servidor, um sistema operacional, um dispositivo de armazenamento ou recursos de rede.  Imagine como tirar uma foto de algo, em vez de ter o objeto real. Você tem uma representação, mas não o objeto em si.

**Para que serve?**

Serve para aproveitar melhor os recursos de hardware existentes.  Em vez de ter vários servidores físicos, cada um rodando um único sistema operacional e aplicação, com a virtualização você pode ter um único servidor físico rodando várias máquinas virtuais (VMs), cada uma com seu próprio sistema operacional e aplicações.

**Quando utilizar?**

* **Consolidação de servidores:** Reduzir o número de servidores físicos, economizando espaço, energia e custos de manutenção.
* **Testes e desenvolvimento:** Criar ambientes isolados para testar softwares e aplicações sem afetar sistemas em produção.
* **Disaster recovery:** Replicar sistemas e dados para garantir a continuidade dos negócios em caso de falhas.
* **Cloud computing:** A base da infraestrutura de nuvem, permitindo a criação e gerenciamento de VMs sob demanda.
* **Desktop virtualization:** Executar vários sistemas operacionais em um único computador.


**Principais conceitos envolvidos:**

* **Hipervisor:**  O software que gerencia as máquinas virtuais, alocando recursos de hardware para cada uma delas.  É a camada entre o hardware e as VMs. Exemplos: VMware vSphere, Hyper-V, KVM.
* **Máquina virtual (VM):**  Um ambiente de software que emula um computador físico, com seu próprio sistema operacional, aplicações e dados.
* **Sistema operacional convidado (Guest OS):** O sistema operacional instalado dentro da máquina virtual.
* **Sistema operacional hospedeiro (Host OS):** O sistema operacional instalado diretamente no hardware físico, onde o hipervisor é executado.
* **Imagem de disco virtual:** Um arquivo que representa o disco rígido de uma máquina virtual.
* **Alocação de recursos:**  O processo pelo qual o hipervisor distribui recursos de hardware (CPU, memória, armazenamento, rede) entre as VMs.
* **Snapshot:**  Um "retrato" do estado de uma VM em um determinado momento, permitindo reverter para um estado anterior