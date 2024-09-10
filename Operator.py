from IXC_main import *
import wget

# # # Extrai dados no IXC e cria um xlsx
# data = datetime.now().strftime("%d-%m-%Y %Hh%Mm%Ss")
# tabela = 'cliente_contrato'
# # filtro = (['id_plano','=','7'],) 
# # ret = ['id','id_contrato','tipo','id_plano','id_produto']
# dados = IXC.get_info_IXC(tabela, )
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

# produtos = IXC.get_info_IXC('vd_contratos_produtos')
# ids = ['466',
# '1776',
# '3743',
# '4560',
# '5006',
# '5135',
# '5271',
# '5294',
# '5617',
# '6354',]
# pay = {'tipo': 'S',
#        'id_plano': '',}
# IXC.edit_data_IXC('vd_contratos_produtos',ids,pay)

# https://drive.usercontent.google.com/u/0/uc?id={}&export=download

link = 'https://drive.google.com/open?id=1MSfGG42MfOHgAOuPTEfIFjPjld6QY-ty'
arquivo_id = link.split('id=')
print(arquivo_id[1])
novo_link = f'https://drive.google.com/uc?export=download&id={arquivo_id[1]}'
print(novo_link)

wget.download(novo_link,'teste.jpeg')
# arquivo = requests.get(novo_link)
# if arquivo.status_code == 200:
#     temp_file = 'foto_temp.jpeg'
#     with open(temp_file, 'wb') as f:
#         f.write(arquivo.content)
# print(arquivo)
# image = Image.open
# IXC.file_upload_ixc('3817', temp_file,'jpeg', 'teste')
