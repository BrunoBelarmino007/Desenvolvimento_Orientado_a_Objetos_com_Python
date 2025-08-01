# 🐍 Python - POO  

Este repositório contém um sistema bancário básico desenvolvido durante o curso **"Desenvolvimento Orientado a Objeto Utilizando a Linguagem Python"** oferecido pela **Fundação Bradesco**.

> **Nota:** Este projeto faz parte da trilha de conhecimento da Linguagem de Programação Python da Fundação Bradesco e é complementar ao repositório de [Python - Básico](https://github.com/BrunoBelarmino007/Python), representando a evolução do aprendizado para conceitos de Programação Orientada a Objetos.

## 📚 Sobre o Curso

O curso aborda os conceitos fundamentais da Programação Orientada a Objetos (POO) aplicados à linguagem Python, proporcionando uma compreensão prática de como estruturar e organizar código de forma mais eficiente e reutilizável.

## 🎯 Conceitos de POO Aplicados

### 1. **Classes e Objetos**
- **Classe Cliente**: Representa um cliente do banco
- **Classe Conta**: Representa uma conta bancária
- **Classe Main**: Classe principal para execução do sistema

### 2. **Encapsulamento**
- Atributos privados (\_nome, \_telefone, \_saldo)
- Métodos getter e setter para controle de acesso
- Uso de properties para validação de dados

### 3. **Abstração**
- Modelagem de entidades do mundo real (Cliente, Conta)
- Separação de responsabilidades entre classes
- Interface clara para interação com objetos

### 4. **Métodos e Atributos**
- Construtor `__init__` para inicialização de objetos
- Métodos de instância para operações específicas
- Properties para controle de acesso aos atributos

## 🏗️ Estrutura do Projeto

```
PythoncomPOO/
├── app/
│   ├── __pycache__/          # Cache do Python (gerado automaticamente)
│   ├── Cliente.py            # Classe Cliente
│   ├── Conta.py              # Classe Conta Bancária
│   └── Main.py               # Arquivo principal de execução
├── venv/                     # Ambiente virtual Python
├── .gitignore               # Arquivos ignorados pelo Git
└── README.md                # Este arquivo
```

## 📋 Descrição das Classes

### 🧑‍💼 Classe Cliente (`Cliente.py`)
Representa um cliente do sistema bancário.

**Atributos:**
- `_nome`: Nome do cliente (privado)
- `_telefone`: Telefone do cliente (privado)

**Métodos:**
- `__init__(n, fone)`: Construtor da classe
- `get_nome()`: Retorna o nome do cliente
- `set_nome(nome)`: Define o nome do cliente

### 💰 Classe Conta (`Conta.py`)
Representa uma conta bancária com operações básicas.

**Atributos:**
- `titular`: Cliente titular da conta
- `numero`: Número da conta
- `_saldo`: Saldo da conta (privado, controlado por property)

**Métodos:**
- `__init__(titular, numero, saldo)`: Construtor da classe
- `saldo` (property): Getter/setter para o saldo com validação
- `saque(valor)`: Realiza saque da conta
- `deposita(valor)`: Realiza depósito na conta
- `extrato()`: Exibe informações da conta

### 🚀 Classe Main (`Main.py`)
Classe principal que demonstra o uso do sistema.

## 🔧 Funcionalidades Implementadas

- ✅ **Criação de Cliente**: Instanciação de objetos Cliente
- ✅ **Criação de Conta**: Associação de conta a um cliente
- ✅ **Depósito**: Adição de valores ao saldo
- ✅ **Saque**: Retirada de valores com validação de saldo
- ✅ **Extrato**: Visualização de informações da conta
- ✅ **Validação de Saldo**: Impedimento de saldo negativo
- ✅ **Encapsulamento**: Controle de acesso aos atributos

## 🚀 Como Executar

### Pré-requisitos
- Python 3.x instalado
- Ambiente virtual configurado (opcional, mas recomendado)

### Passos para Execução

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/BrunoBelarmino007/PythoncomPOO.git
   cd PythoncomPOO
   ```

2. **Ative o ambiente virtual (opcional):**
   ```bash
   # Windows
   venv\\Scripts\\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Execute o programa principal:**
   ```bash
   cd app
   python Main.py
   ```

### Exemplo de Saída
```
Testando o arquivo main.py
Saldo Realizado com sucesso
Cliente:  Bruno Saldo:  500
```

## 🎓 Conceitos de POO Demonstrados

| Conceito | Implementação | Arquivo |
|----------|---------------|---------|
| **Encapsulamento** | Atributos privados com \_ | `Cliente.py`, `Conta.py` |
| **Abstração** | Classes representando entidades reais | Todas as classes |
| **Métodos Getter/Setter** | Controle de acesso aos atributos | `Cliente.py` |
| **Properties** | Validação automática de dados | `Conta.py` |
| **Construtor** | Inicialização de objetos | `__init__` em todas as classes |
| **Validação** | Regras de negócio (saldo não negativo) | `Conta.py` |

## 🏆 Aprendizados Consolidados

Durante este curso, foram consolidados os seguintes conceitos de POO:

- ✅ **Classes e Objetos**: Criação e instanciação
- ✅ **Encapsulamento**: Proteção de dados com atributos privados
- ✅ **Abstração**: Modelagem de entidades do mundo real
- ✅ **Métodos**: Comportamentos específicos das classes
- ✅ **Properties**: Controle avançado de acesso aos atributos
- ✅ **Validação**: Implementação de regras de negócio
- ✅ **Organização**: Estruturação de código em módulos

## 🤝 Contribuições

Este repositório é para fins educacionais. Sugestões de melhorias e extensões do projeto são bem-vindas!

---

**Parte da Trilha Python:** Curso 3 de 5 | [Ver curso anterior: Python Básico](https://github.com/BrunoBelarmino007/Python)

---

Que tudo o que somos e temos seja para a glorificação do nome DELE - Romanos 11:33-36.

---