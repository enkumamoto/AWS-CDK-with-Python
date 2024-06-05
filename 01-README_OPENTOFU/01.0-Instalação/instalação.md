### O que é Terraform?
Terraform é uma ferramenta de Infrastructure as Code (IaC) que permite definir e provisionar infraestrutura através de arquivos de configuração. Ele é utilizado para criar, gerenciar e atualizar recursos em vários provedores de serviços de nuvem, incluindo AWS.

### Principais Comandos do Terraform
- `terraform init`: Inicializa um diretório contendo arquivos de configuração do Terraform. Este comando baixa os plugins necessários para interagir com os provedores de nuvem especificados.
- `terraform plan`: Gera um plano de execução, mostrando quais ações o Terraform tomará para atingir o estado desejado da infraestrutura descrita nos arquivos de configuração.
- `terraform apply`: Aplica as mudanças necessárias para alcançar o estado desejado da infraestrutura, conforme definido nos arquivos de configuração.
- `terraform destroy`: Remove todos os recursos provisionados gerenciados pelo Terraform.

### TF_LOG=DEBUG
Essa variável de ambiente é usada para habilitar o modo de depuração (debug) do Terraform. Ao definir `TF_LOG=DEBUG`, você obterá informações detalhadas sobre o que o Terraform está fazendo, o que pode ser útil para diagnosticar problemas.

---

# Instalação

Como instalar o OpenTofu no Ubuntu:

```markdown
# Instalação do OpenTofu no Ubuntu

Este guia explica como instalar o OpenTofu no Ubuntu.

## Passo a Passo

### 1. Atualize o sistema
Antes de instalar qualquer novo software, é uma boa prática garantir que o sistema esteja atualizado.

```bash
sudo apt update
sudo apt upgrade -y
```

### 2. Instale dependências necessárias
O OpenTofu pode ter algumas dependências que precisam ser instaladas. Vamos instalar algumas ferramentas básicas e o `curl` para baixar os arquivos.

```bash
sudo apt install -y curl unzip
```

### 3. Baixe o OpenTofu
Baixe o pacote mais recente do OpenTofu. Visite a [página de lançamentos do OpenTofu](https://github.com/opentofu/opentofu/releases) para verificar a versão mais recente. Aqui, substituiremos `VERSION` pela versão atual do OpenTofu.

```bash
curl -LO https://github.com/opentofu/opentofu/releases/download/VERSION/opentofu_VERSION_linux_amd64.zip
```

### 4. Extraia o arquivo baixado
Extraia o arquivo baixado para um diretório em seu PATH. Normalmente, `/usr/local/bin` é um bom local para isso.

```bash
unzip opentofu_VERSION_linux_amd64.zip
sudo mv opentofu /usr/local/bin/
```

### 5. Verifique a instalação
Para verificar se o OpenTofu foi instalado corretamente, execute o seguinte comando:

```bash
opentofu version
```

Você deve ver a versão do OpenTofu instalada.

### 6. Configuração do Ambiente (Opcional)
Se você deseja que o OpenTofu esteja disponível em qualquer sessão do terminal, adicione `/usr/local/bin` ao seu PATH no arquivo de configuração do shell (ex.: `~/.bashrc`, `~/.zshrc`).

Abra o arquivo de configuração do shell com um editor de texto, como `nano`:

```bash
nano ~/.bashrc
```

Adicione a seguinte linha no final do arquivo:

```bash
export PATH=$PATH:/usr/local/bin
```

Carregue o novo PATH na sessão atual do terminal:

```bash
source ~/.bashrc
```

### 7. Instalação Concluída
Agora, você deve ter o OpenTofu instalado e configurado corretamente no seu sistema Ubuntu. Você pode começar a usar o OpenTofu para gerenciar sua infraestrutura como código.

## Referências

- [OpenTofu GitHub](https://github.com/opentofu/opentofu)
- [Documentação Oficial do OpenTofu](https://docs.opentofu.org)

```

Este `README.md` fornece instruções claras e concisas para instalar o OpenTofu no Ubuntu, garantindo que qualquer usuário possa seguir os passos sem dificuldades.