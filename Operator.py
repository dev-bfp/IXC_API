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

# contratos = ['14',
# '27',
# '130',
# '243',
# '386',
# '1258',
# '1709',
# '2048',
# '2103',
# '2161',
# '2167',
# '2195',
# '2215',
# '2225',
# '2234',
# '2236',
# '2252',
# '2264',
# '2290',
# '2318',
# '2345',
# '2370',
# '2446',
# '2512',
# '2530',
# '2598',
# '3157',
# '3312',
# '3461',
# '3602',
# '3888',
# '4124',
# '4262',
# '4325',
# '4413',
# '4497',
# '5027',
# '5533',
# '5635',
# '5887',
# '5934',
# '5956',
# '6012',
# '6013',
# '6017',
# '6019',
# '6027',
# '6032',
# '6034',
# '6037',
# '6038',
# '6041',
# '6042',
# '6056',
# '6062',
# '6063',
# '6066',
# '6068',
# '6069',
# '6089',
# '6090',
# '6093',
# '6095',
# '6096',
# '6098',
# '6102',
# '6107',
# '6110',
# '6111',
# '6114',
# '6115',
# '6116',
# '6125',
# '6131',
# '6132',
# '6137',
# '6141',
# '6144',
# '6145',
# '6151',
# '6154',
# '6155',
# '6157',
# '6166',
# '6167',
# '6170',
# '6172',
# '6174',
# '6177',
# '6178',
# '6181',
# '6182',
# '6184',
# '6185',
# '6186',
# '6190',
# '6191',
# '6195',
# '6198',
# '6202',
# '6207',
# '6209',
# '6210',
# '6214',
# '6215',
# '6219',
# '6225',
# '6240',
# '6243',
# '6281',
# '6398',
# '6422',
# '6474',
# '6780',
# '8155',
# '8157',
# '8161',
# '8162',
# '8165',
# '8166',
# '8168',
# '8172',
# '8175',
# '8176',
# '8177',
# '8180',
# '8181',
# '8182',
# '8189',
# '8190',
# '8191',
# '8192',
# '8196',
# '8197',
# '8199',
# '8200',
# '8201',
# '8205',
# '8206',
# '8207',
# '8209',
# '8210',
# '8211',
# '8213',
# '8215',
# '8219',
# '8220',
# '8221',
# '8223',
# '8229',
# '8231',
# '8232',
# '8233',
# '8234',
# '8240',
# '8242',
# '8244',
# '8245',
# '8251',
# '8255',
# '8256',
# '8259',
# '8260',
# '8261',
# '8262',
# '8264',
# '8265',
# '8268',
# '8272',
# '8273',
# '8285',
# '8287',
# '8288',
# '8292',
# '8293',
# '8294',
# '8296',
# '8297',
# '8299',
# '8300',
# '8301',
# '8302',
# '8303',
# '8305',
# '8306',
# '8308',
# '8313',
# '8314',
# '8323',
# '9796',
# '9942',
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




lista = {('303353', '150,00', '25/03/2025', '43994'),
('299902', '100,00', '25/03/2025', '40075'),
('300498', '100,00', '25/03/2025', '40782'),
('300780', '75,00', '25/03/2025', '41105'),
('300430', '75,00', '25/03/2025', '40662'),
('300510', '100,00', '25/03/2025', '40806'),
('297359', '120,00', '24/03/2025', '37068'),
('301284', '120,00', '24/03/2025', '41719'),
('297873', '100,00', '24/03/2025', '37649'),
('302102', '75,00', '24/03/2025', '42619'),
('296274', '100,00', '24/03/2025', '35689'),
('300989', '100,00', '23/03/2025', '41333'),
('313303', '75,00', '07/03/2025', '38928'),}

log = []
for x in lista: 
    payload = {
        "filial_id": "2",  # filial do recebimento
        "id_receber": x[0],  # id do título
        "conta_": "12",  # conta que está fazendo o recebimento
        "id_conta": "1",  # planejamento analítico da conta que está fazendo o recebimento
        "tipo_recebimento": "D",  # tipo recebimento em dinheiro
        "data": x[2],  # data do recebimento
        "valor_parcela": x[1],  # valor da parcela
        "credito": x[1],  # crédito e débito devem se anular na baixa
        "debito": x[1],
        "valor_total_recebido": x[1],  # valor total
        "historico": "BAIXA NETFIBRALINE - ID SGP: " + x[3] + " - IXC: " + x[0],  # descrição registrada
        "previsao": "N",  # Previsão = S significa isentar de um período, previsão = N significa que foi cobrado
        "tipo_lanc": "R",  # tipo de lançamento recebimento
    }

    dados = IXC.send_to_IXC('fn_areceber_recebimentos_baixas_novo',payload)
    pp(dados)
    log.append(dados)

IXC.create_log(log)
