import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from IXC_main import *
from config_google import *

nameSheets = "Análise Pontual"
worksheet = 'filial_contrato'
sheet = client.open(nameSheets).worksheet(worksheet)

#filtro = (['status','=','F'],['id','>','0'],['id_condicao_pagamento','=',"14"],)
return_list = ['id', 'status', 'id_filial']
manual_replace = {'status': [['A','Ativo'],['I','Inativo'],['P','Pre-Contrato'],['D','Desistiu']]}
dados = IXC.get_info_IXC('cliente_contrato',return_list=return_list,manual_replace=manual_replace)
# print(dados)

formated_data = [list(dados['registros'][0].keys())]
for dados in dados["registros"]:
    formated_data.append(list(dados.values()))

dados = sheet.update(formated_data,'A1')