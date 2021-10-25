# Exemplo django + graphql

`(*)` incompleto, falta autenticação, tenants, fazer as queries...

## Sobre o django

O Django é uma framework muuuito antiga, quando nem existia node.js o Django já era vovô. Ele tem o foco de ser um pacotão com tudo pronto, destaque para o ORM que pode ser complexo de mexer mas lida muito bem com migrações. Como é antigo tem bastante coisa com cara de web clássica (cuspir HTML/MVC), e um suporte enorme de comunidade, muitos plugins mesmo.

Desvantagens: como consequência de ser um pacotão, quando você quer um caso muito específico pode entrar em coisas difíceis de configurar. E é claro, velocidade: está longe de ser o forte do python.

## Instalando

Esta é uma parte chata do python, as versões do python e os "ambientes". No python "cru" não existe o equivalente a uma pasta `node_modules`, existem então ferramentas como o `virtualenv` e o `pipenv` que tratam disso.

  - Verifique como instalar o `pipenv`;
  - Execute `pipenv install`;
  - Pode ser que dê algum erro se você não tiver um python 3.9 instalado;
  - Para entrar no ambiente do projeto, digite `pipenv shell`;
  - No VSCode, para que as completions funcionem direito, no canto inferior direito, onde estiver escrito "Python", clique, e na lista de pythons, selecione o que tem pipenv.

## Executando

  - `cp .env.sample .env`
    - Nota: O Django não tem o suporte a env embutido, isto é uma lib externa, a `django-environ`;
  - Suba o postgres: `docker-compose up`
  - Rode a migração. Depois de ativar `pipenv shell`, entre `python manage.py migrate`
  - Suba o servidor de dev: `python manage.py runserver`

## Estrutura de projeto

A estrutura do django é um tanto incomum, temos uma pasta com a raiz de configuração do projeto (aqui a chamei de proj), e depois podemos ter N pastas que são "aplicações plugáveis" (acho a chamei de app).

**Arquivos notáveis**

  - `proj/settings.py`: Configurações da framework e módulos;
    - NOTA: Note que o python não tem o conceito de "export variable" como no JS, toda variável de um arquivo é pública e exposta;
  - `proj/urls.py`: As rotas.
  - `app/models.py`: A definição de tabelas do banco. Aqui é um arquivo mas pode ser uma pasta, e o django carrega automaticamente a pasta toda;
  - `app/schemas.py`: Coisas do graphQL. Mesmo esquema pode ser uma pasta;
  - `app/views.py`: Controllers...

## Diferenciais

A framework é muito completa para criar CRUDs com pouco código.

  - No django você cria apenas os modelos (via classes) e ele cria as migrações pra você. Poucos ORMs fazem isso;
    - `python manage.py makemigrations` e `python manage.py migrate`
  - A framework vem com uma interface de admin com CRUDs prontos, acessar via `/admin`
    - Precisa criar um usuário root `python manage.py createsuperuser`
  - As seguintes tarefas são feitas com 1 ou 2 linhas:
    - filtrar listas de acordo com o usuário logado
    - upload de arquivos
    - adicionar autenticação com o Oauth2 ou JWT
  - Testes preconfigurados com rollback a cada caso;
  - Libs que integram com a base do framework, criando uma experiência de configuração limpa sem repetição:
    - `graphene-django` para o graphQL, cria os schemas a partir dos models;
    - `django-filter` pra filtros de busca, seja pro graphQL ou REST
    - `django-tenants` tem uma proposta de tenants qque parece interessante (apenas postgres)