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


# nmSheets = "Custo Operacional"
# sheet = client.open(nmSheets).worksheet("contrato")

# filtro = (['id', '>', '0'],['data_fechamento', '>', '2024-01-01'],)
# dados = IXC.get_info_IXC('cliente_contrato',  order='DESC')
# # print(dados)

# formated_data = [list(dados['registros'][0].keys())]
# for dados in dados["registros"]:
#     formated_data.append(list(dados.values()))

# dados = sheet.update(formated_data,'A1')


# dados = IXC.get_info_IXC('crm_campanha', 'id','=','2')['registros'][0]['campanha']
# pp(dados)




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


# contratos = []
# payload = {
#     'id_filial': '2',
#     'id_carteira_cobranca': '9'
# }
# IXC.edit_data_IXC('cliente_contrato',contratos,payload)
# # ------------------------------------------------------

# dados = IXC.get_info_IXC('cliente')
# print(dados)


# url = IXC_url + 'produtos'
# encode = base64.b64encode(IXC_token.encode('utf-8')).decode('utf-8')
# # print(encode)
# headers = {
# 'ixcsoft': 'listar',
# 'Authorization': "Basic " + encode,
# 'Content-Type': 'application/json'
# }

# payload = {
#     'qtype': 'id',
#     'query': '11',
#     'oper': '=',
#     # 'page': '1',
#     # 'rp': lin,
#     # 'sortname': ord_camp,
#     # 'sortorder': order,
# }

# response = requests.post(url, data=json.dumps(payload), headers=headers)
# pp(response.json())

# contratos = [
# ]

# payload = {
#     'id_filial': '2',
#     'id_carteira_cobranca': '9'
# }
# IXC.edit_data_IXC('cliente_contrato', contratos, payload)

# clientes = []
# for x in contratos:
#     dados = IXC.get_info_IXC('cliente_contrato', 'id', '=', x)
#     id_cliente = dados['registros'][0]['id_cliente']
#     clientes.append(id_cliente)

# print(clientes)    
# payload = {
#     'filial_id': '2',
# }

# IXC.edit_data_IXC('cliente',clientes,payload)


# payload = {'id_chamado' : '50383',
#       'mensagem' : 'teste',
#       'id_tecnico' : '38',
#       'status': 'AG',
#       'id_evento': '5',
#       'data_agendamento' : '2025-3-29 09:00:00',
#       'data_agendamento_final' :'2025-3-29 10:00:00',}

# data = IXC.send_to_IXC('su_oss_chamado_reagendar', payload)
# print(data)

# dados_os = {
#     "id_chamado": "50383",
#     "id_setor": "2",
#     "id_tecnico": "38",
#     "id_assunto": "1",
#     "mensagem": "testeee",
#     "status": "AG"
# }
# data = IXC.send_to_IXC('su_oss_chamado_alterar_setor',dados_os)
# print(data)


contratos = ['11119',
'11120',
'11131',
'11135',
'11136',
'11137',
'11138',
'11143',
'11144',
'11145',
'11146',
'11154',
'11156',
'11160',
'11162',
'11163',
'11164',
'11165',
'11167',
'11172',
'11174',
'11181',
'11182',
'11183',
'11187',
'11191',
'11192',
'11198',
'11208',
'11214',
'11223',
'11224',
'11233',
'11238',
'11239',
'11240',
'11242',
'11244',
'11246',
'11247',
'11248',
'11249',
'11250',
'11254',
'11255',
'11262',
'11267',
'11271',
'11272',
'11274',
'11277',
'11278',
'11279',
'11280',
'11283',
'11285',
'11287',
'11288',
'11291',
'11293',
'11297',
'11298',
'11299',
'11301',
'11304',
'11307',
'11313',
'11315',
'11316',
'11323',
'11326',
'11330',
'11331',
'11333',
'11334',
'11339',
'11340',
'11344',
'11345',
'11354',
'11357',
'11360',
'11364',
'11376',
'11389',
'11408',
'11413',]


log = []
for x in contratos:
    dados = IXC.desbloqueio_confianca(x)
    if dados:
        dados['id_origem'] = x
        log.append(dados)
    else: 
        dados = IXC.liberar_temp(x)
        dados['id_origem'] = x
        log.append(dados)
        print(dados)

print(log)
IXC.create_log(log)

