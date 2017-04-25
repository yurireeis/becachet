# language: pt
@remover_componentes
Funcionalidade: Remover componente
  Como usuário com acesso ao painel de controle
  Para que ...
  Quero remover um componente

  Contexto: usuário acessa o painel de controle
    Dado que o usuário acessa o painel de controle

  @remover_componente
  Cenário: Remover componente ativo
    Dado que iniciou a remoção de um componente
    E que recebeu um questionamento se deseja de fato concluir a ação
    Quando afirmar que deseja concluir a ação
    Então deverá receber uma confirmação de que o componente foi removido com sucesso
    E o componente não deverá estar visível na lista de componentes
    E não deverá estar visível na página de status

  @remover_componente_e_cancelar
  Cenário: Cancelar a ação de remover componente ativo
    Dado que iniciou a remoção de um componente
    E que recebeu um questionamento se deseja de fato concluir a ação
    Quando negar que deseja concluir a ação
    Então o componente deverá estar visível na lista de componentes
    E deverá estar visível na página de status

  @remover_componente_e_cancelar
  Cenário: Cancelar a ação de remover componente inativo
    Dado que iniciou a remoção de um componente
    E que recebeu um questionamento se deseja de fato concluir a ação
    Quando negar que deseja concluir a ação
    Então deverá receber uma confirmação de que o componente foi removido com sucesso
    E o componente deverá estar visível na lista de componentes
    Mas não deverá estar visível na página de status
