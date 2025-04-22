import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from IXC_main import *



contratos = ['235', 
'3778',  
]

payload_contratos = {
    'id_filial': '2',
    'id_carteira_cobranca': '8'
}

IXC.edit_data_IXC('cliente_contrato', contratos, payload_contratos)

clientes = []
for x in contratos:
    dados = IXC.get_info_IXC('cliente_contrato', 'id', '=', x)
    id_cliente = dados['registros'][0]['id_cliente']
    clientes.append(id_cliente)

print(clientes)    
payload_cliente = {
    'filial_id': '2',
}

IXC.edit_data_IXC('cliente',clientes,payload_cliente)