# jc-challenge

## Desafio

Criar uma aplicação CRM em django versão 1.8, Python 2.7, reutilizável, com as seguintes funcionalidades:

1. Autenticação de usuários sendo o username o email.
2. Cadastrar empresas: id 32 caracteres, nome único, quem criou e quando.
3. Cada empresa pode ter várias pessoas de contato, sendo a tabela: id 32 char, quem criou, quando, nome, email, telefone.
4. Status de realização de contatos com a empresa/pessoas: id 32 char, por quem, quando, detalhes, próximo contato null true, tipo: fazer follow up, não aprovado, sucesso.
5. Cada status pode conter uma proposta, sendo a proposta comercial relacionada a varios produtos e preços. 
6. Todos os POST devem ser via AJAX e as informações devem ser carregadas na tela automaticamente após o POST.

## Instalação

* Instale o [pip][0].

Primeira opção

```
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python get-pip.py
```

Segunda opção

```
$ sudo apt-get install -y python-pip
```

* Instale o [VirtualEnv][1].

```
$ sudo pip install virtualenv
$ # ou
$ sudo apt-get install -y virtualenv
```

### Criando o ambiente

Vamos criar um ambiente usando o **Python 2.7.12**.

```
virtualenv -p python2.7 .venv
```

Ativando o ambiente

```
source .venv/bin/activate
```

Instale o [django 1.8.17][2].

```
pip install django==1.8.17
```

Então nós temos:

```
virtualenv-15.1.0
Python 2.7.12
django==1.8.17
```

## Clonando e rodando o projeto

```bash
git clone https://github.com/rg3915/jc-challenge.git
cd jc-challenge
virtualenv -p python2.7 .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/secret_gen.py
python manage.py migrate
make createuser
make createcompanies
make createpersons
python manage.py test
python manage.py runserver
```

### Script

```
git clone https://github.com/rg3915/jc-challenge.git
cd jc-challenge
source setup.sh
```

[0]: http://pip.readthedocs.org/en/latest/
[1]: https://virtualenv.pypa.io/en/latest/
[2]: https://www.djangoproject.com/download/
