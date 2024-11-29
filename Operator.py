from IXC_main import *
import gspread
from google.oauth2.service_account import Credentials

scope = ["https://www.googleapis.com/auth/drive"]
#credentials_google = ServiceAccountCredentials.from_json_keyfile_name(caminho_local_credentials, scope)
credentials_google = ServiceAccountCredentials.from_json_keyfile_dict(credencial_google, scope)
client = gspread.authorize(credentials_google)


# # # Extrai dados no IXC e cria um xlsx
# data = datetime.now().strftime("%d-%m-%Y %Hh%Mm%Ss")
# tabela = 'cliente_contrato'
# # filtro = (['id_plano','=','7'],) 
# ret = ['id','id_contrato','tipo','id_plano','id_produto']
# dados = IXC.get_info_IXC(tabela, return_list=ret)
# ret = dados['registros'][0].keys()

# df = pd.DataFrame(dados['registros'],columns=ret)
# df.to_excel(f'C:/Users/brian/OneDrive/dev-bfp/GitHub/IXC_API/generated files/{tabela} - {data}.xlsx', index= False)


# dd = IXC.get_info_IXC('cliente_contrato','id','=','9000')
# vd = IXC.get_info_IXC('vd_contratos','id','=',str(dd['registros'][0]['id_vd_contrato']))
# vd_contrato = IXC.get_info_IXC('vd_contratos_produtos')#,col='id',op='=',value=dd['id_vd_contrato'])
# speed_plan = ''
# pp(vd_contrato)


# lista = []
# payload = {
#     'desconto_fidelidade': '600,00',
# }
# IXC.edit_data_IXC('cliente_contrato',lista,payload)


# def alterar_venda(id_venda):
  
#     dados = IXC.get_info_IXC('vd_saida','id','=',id_venda)['registros'][0]
#     url = IXC_url + 'vd_saida_alterar'
#     encode = base64.b64encode(IXC_token.encode('utf-8')).decode('utf-8')
#     headers = { "ixcsoft": "",
#                 "Authorization": "Basic " + encode,}

#     payload = {'id_saida': id_venda,
#         'status': 'A'}
    
    
#     response = requests.put(url, json=payload, headers=headers)
#     # response = requests.post(url, headers=headers, data=payload)
#     print(response.json())

# alterar_venda('271342')
# saida = IXC.get_info_IXC('vd_saida','id','=','172038')
# pp(saida)


# ------------------------------------------------------
# clientes = []

# payload = {
#     'filial_id': '2',
# }
# IXC.edit_data_IXC('cliente',clientes,payload)
# # ------------------------------------------------------


# # ------------------------------------------------------
# tabela = 'cliente_contrato'
# filtro = (['assinatura_digital','!=','P'],) 
# ret = ['id', 'id_cliente']
# dados = IXC.get_info_IXC(tabela, param=filtro, return_list=ret)
# contratos = []
# for valores in dados["registros"]:
#     id = valores['id']
#     # print(id)
#     contratos.append(id)

# payload = {
#     'assinatura_digital': 'P',
# }

# IXC.edit_data_IXC('cliente_contrato',contratos,payload)
# ------------------------------------------------------
# nmSheets = "Custo Operacional"
# sheet = client.open(nmSheets).worksheet("vd_saida")

# filtro = (['status','=','F'],['id','>','0'],['id_condicao_pagamento','=',"14"],)
# dados = IXC.get_info_IXC('vd_saida',param=filtro, order='DESC')

# formated_data = [list(dados['registros'][0].keys())]
# for dados in dados["registros"]:
#     formated_data.append(list(dados.values()))

# dados = sheet.update(formated_data,'A1')



# nmSheets = "Custo Operacional"
# sheet = client.open(nmSheets).worksheet("movimento_produtos")

# filtro = (['id_saida', '!=', '0'],['data', '>', '2024-01-01'],)
# dados = IXC.get_info_IXC('movimento_produtos', param=filtro, order='DESC')

# formated_data = [list(dados['registros'][0].keys())]
# for dados in dados["registros"]:
#     formated_data.append(list(dados.values()))

# dados = sheet.update(formated_data,'A1')


nmSheets = "Custo Operacional"
sheet = client.open(nmSheets).worksheet("contrato")

filtro = (['id', '>', '0'],['data_fechamento', '>', '2024-01-01'],)
dados = IXC.get_info_IXC('cliente_contrato',  order='DESC')
# print(dados)

formated_data = [list(dados['registros'][0].keys())]
for dados in dados["registros"]:
    formated_data.append(list(dados.values()))

dados = sheet.update(formated_data,'A1')
