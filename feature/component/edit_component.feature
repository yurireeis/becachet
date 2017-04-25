# language: pt
@atualizar_componentes
Funcionalidade: Atualizar componente
  Como usuário com acesso ao painel de controle
  Para que ...
  Quero atualizar um componente

  Contexto: usuário acessa o painel de controle
    Dado que o usuário acessa o painel de controle

  @atualizar_componente_ativo_alterando_nome
  Cenário: Atualizar componente ativo alterando nome
    Dado que iniciou a atualização de um componente
    E que informou um novo nome
    Quando concluir a atualização do componente
    Então o componente com o novo nome deverá estar visível na lista de componentes
    E deverá estar visível na página de status com o novo nome
