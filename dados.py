import pandas as pd

questions = [
    ["O que pode ser patenteado?", "1) Uma Marca", "2) Uma Invenção", "3) Um Desenho Industrial", "4) Um Modelo de Utilidade", "", 2],
    ["A busca de patente nos bancos de dados é um procedimento obrigatório para dar entrada no pedido?", "1) Sim", "2) Não", "3) Pode variar de acordo com as circunstâncias", "", "", 2],
    ["Qual a abrangência da proteção da patente após ser concedida?", "1) Nacional", "2) Mundial", "3) Estadual", "4) Municipal", "5) Continental", 1],
    ["Qual a vigência de uma Patente de Invenção?", "1) 10 anos", "2) 5 anos", "3) 25 anos", "4) 15 anos", "5) 20 anos", 5],
    ["Quais os Requisitos Necessários para uma Patente de Invenção?", "1) Ato Inventivo", "2) Novidade", "3) Atividade Inventiva", "4) Melhoria Funcional", "5) Aplicação Industrial", 2],
    ["Dentre as alternativas abaixo, o que deve ser observado no momento da Redação do Pedido de Patente?", "1) Lei de Propriedade Industrial – LPI (Lei nº 9279/1996)","2) Lei do Direito Autoral – (Lei nº 9610/1998)", "3) IN 30/2013 do INPI (estabelecimento de normas gerais de procedimentos para explicitar e cumprir dispositivos da Lei de Propriedade Industrial - Lei nº 9279, de 14 de maio de 1996, no que se refere às especificações dos pedidos de patente);", "4) IN 31/2013 do INPI (estabelecer normas gerais de procedimentos para explicitar e cumprir dispositivos da Lei de Propriedade Industrial - Lei nº 9279, de 14 de maio de 1996, no que se refere às especificações formais dos pedidos de patente);", "5) Lei do Software – (Lei nº 9609/1998)", 3],
    ["Quais documentos devem, obrigatoriamente, ser protocolados no Pedido de Patente?", "1) Requerimento", "2) Desenhos", "3) Anterioridades", "4) Reivindicações", "5) Comprovante de pagamento", 4],
    ["São Bases de Pesquisa de Patente:", "1) Ecad", "2) INPI", "3) Biblioteca Nacional", "4) Espacenet", "5) Patentscope", 2],
    ["No que diz respeito ao Exame do Pedido, é correto afirmar:", "1) O exame do pedido é realizado a critério do INPI, independente de requerimento", "2) Na ocasião do exame é elaborado parecer pelo INPI", "3) O pedido é mantido em sigilo por 18 meses a contar da data do depósito", "4) Na falta de requerimento no prazo estipulado a patente é arquivada e não há mais possibilidade de desarquivamento", "", 3],
    ["A divulgação prévia pelo próprio inventor prejudica o requisito da novidade da patente?", "1) Sim", "2) Não", "3) Apenas se ultrapassar o 12 meses que antecedem o pedido", "", "", 3],
]

df = pd.DataFrame(questions, columns=['perguntas', 'opcao 1', 'opcao 2', 'opcao 3', 'opcao 4', 'opcao 5', 'resposta'])

df.to_excel("question.xlsx", index=False)

print('Perguntas inseridas com sucesso!')