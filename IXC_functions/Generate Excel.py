from Monalisa import *
from datetime import *
import pandas as pd

def Tab_FN_ARECEBER_Brian(page, registros, celula):
    colunas = [
        ['id', 'nd'],
        ['status', 'subt', {"A": "A Receber", "C": "Cancelado", "R": "Recebido", "P": "Parcial"}],
        ['id_cliente', 'nd'],
        ['valor', 'nd'],
        ['valor_recebido', 'nd'],
        ['valor_aberto', 'nd'],
        ['data_emissao', 'date'],
        ['data_vencimento', 'date'],
        ['pagamento_valor', 'num'],
        ['pagamento_data', 'date'],
        ['documento', 'txt'],
        ['id_saida', 'nd'],
        ['id_contrato_principal', 'nd'],
        ['id_contrato_avulso', 'nd'],
        ['id_contrato', 'nd'],
        ['id_renegociacao', 'nd'],
        ['nn_boleto', 'nd'],
        ['obs', 'txt'],
        ['liberado', 'txt'],
        ['id_carteira_cobranca','subt', {"1": "Santander", "2": "Gerencianet", "3": "BIN", "4": "Cartão de crédito", "5": "Gerencianet com desconto", "6": "Santander com desconto"}]
    ]

    filtro = [
    ]
    return dump2sh_Brian(colunas, filtro, 'Data_base_fn_areceber', 'FN_ARECEBER_ABERTO', 'fn_areceber', celula,'all',page,registros)



dados = getdtall('fn_areceber')
print(dados['total'])
pages = dados['total']
registros = 120000
qtd_pages = math.ceil(int(pages) / registros)
print(qtd_pages)
linha = 2
dados = []
for x in range(1,qtd_pages+1): # qtd_pages+1
    celula = 'A'+ str(linha)
    print(f'página {x} que inicia em {celula}')
    data_ixc = Tab_FN_ARECEBER_Brian(x,registros,celula)
    linha += registros
    dados += data_ixc
print(len(dados))
cabecalho = {
        'Id': int,
        'Status': str,
        'Id Cliente': int,
        'Valor': float,
        'Valor Recebido': float,
        'Valor Aberto': float,
        'Data Emissão': object,
        'Data Vencimento': object,
        'Pagamento Valor': object,
        'Pagamento Data': object,
        'Documento': str,
        'Id Saída': str,
        'Id Contrato Principal': str,
        'Id Contrato Avulso': str,
        'Id Contrato': str,
        'Id Renegociacao': str,
        'Nosso número boleto': str,
        'Observação': str,
        'Liberado': str,
        'Carteira Cobrança': str
        }

df = pd.DataFrame(dados,columns=list(cabecalho.keys()))
df = df.astype(cabecalho)
agora = datetime.now().strftime("%d-%m-%Y %H_%M_%S")
df.to_excel(f"C:/Users/brian/OneDrive/dev-bfp/GitHub/IXC_API/generated files/{} " + agora + ".xlsx", index= False)

