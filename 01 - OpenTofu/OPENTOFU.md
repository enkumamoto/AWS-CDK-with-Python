# OpenTofu
OpenTofu é um fork de Terraform que oferece uma experiência semelhante. Aqui está um tutorial passo a passo para instalar o OpenTofu no Ubuntu 22.04 Jammy.

### Passo 1: Atualizar o Sistema
Primeiro, atualize os pacotes do sistema:
```bash
sudo apt update
sudo apt upgrade -y
```

### Passo 2: Instalar Dependências
Certifique-se de que você tenha `curl`, `gnupg`, e `software-properties-common` instalados:
```bash
sudo apt install -y curl gnupg software-properties-common
```

### Passo 3: Adicionar o Repositório OpenTofu
Adicione o repositório do OpenTofu à lista de fontes de pacotes:
```bash
curl -fsSL https://apt.opentofu.io/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://apt.opentofu.io $(lsb_release -cs) main"
```

### Passo 4: Instalar o OpenTofu
Atualize a lista de pacotes novamente e instale o OpenTofu:
```bash
sudo apt update
sudo apt install opentofu
```

### Passo 5: Verificar a Instalação
Verifique se o OpenTofu foi instalado corretamente:
```bash
opentofu --version
```
Você deve ver a versão do OpenTofu instalada.

### Passo 6: Configuração Inicial (Opcional)
Se você já tem projetos com Terraform, pode precisar ajustar arquivos de configuração e estado para compatibilidade com OpenTofu. Consulte a documentação oficial do OpenTofu para detalhes sobre a migração.

### Passo 7: Usar OpenTofu
Agora você pode usar o OpenTofu da mesma forma que usaria o Terraform, criando arquivos de configuração (`.tf`) e utilizando comandos como `opentofu init`, `opentofu plan` e `opentofu apply`.

```bash
mkdir my-opentofu-project
cd my-opentofu-project

# Criar um arquivo de configuração .tf, por exemplo, main.tf
# Exemplo simples:
echo '
provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
' > main.tf

# Inicializar o projeto
opentofu init

# Planejar a infraestrutura
opentofu plan

# Aplicar as mudanças
opentofu apply
```

### Conclusão
Seguindo esses passos, você terá o OpenTofu instalado e poderá começar a gerenciar sua infraestrutura como código. Se precisar de mais informações, consulte a [documentação oficial do OpenTofu](https://opentofu.io).

