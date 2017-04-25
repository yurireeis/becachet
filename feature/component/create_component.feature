# language: pt
@criar_componentes
Funcionalidade: Criar componente
  Como usuário com acesso ao painel de controle
  Para que ...
  Quero criar um componente

  Contexto: usuário acessa o painel de controle
    Dado que o usuário acessa o painel de controle

  @criar_componente_ativo_com_nome
  Cenário: Criar componente ativo com nome
    Dado que iniciou a adição de um componente
    E que informou um nome
    Mas sem uma descrição
    E o setou como ativo
    Quando concluir a criação do componente
    Então o componente deverá estar visível na lista de componentes
    Mas não deverá apresentar a descrição corresponente
    E deverá estar visível na página de status

  @criar_componente_ativo_com_nome_e_descricao
  Cenário: Criar componente ativo com nome e descrição
    Dado que iniciou a adição de um componente
    E que informou um nome
    E uma descrição
    E o setou como ativo
    Quando concluir a criação do componente
    Então o componente deverá estar visível na lista de componentes
    E deverá apresentar a descrição corresponente
    E deverá estar visível na página de status

  @criar_componente_inativo_com_nome_e_descricao
  Cenário: Criar componente inativo com nome e descrição
    Dado que iniciou a adição de um componente
    E que informou um nome
    E uma descrição
    Mas o setou como inativo
    Quando concluir a criação do componente
    Então o componente deverá estar visível na lista de componentes
    E deverá apresentar a descrição corresponente
    Mas não deverá estar visível na página de status
