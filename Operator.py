from IXC_main import *


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

filtro = (['estoque','=','S'],['id','=','626155']) 
saida = IXC.get_info_IXC('vd_saidas',param=filtro)
pp(saida)