from IXC_main import *
import gspread
from google.oauth2.service_account import Credentials

scope = ["https://www.googleapis.com/auth/drive"]
#credentials_google = ServiceAccountCredentials.from_json_keyfile_name(caminho_local_credentials, scope)
credentials_google = ServiceAccountCredentials.from_json_keyfile_dict(credencial_google, scope)
client = gspread.authorize(credentials_google)



contratos = []

payload = {
    'id_filial': '2',
    'id_carteira_cobranca': '9'
}
IXC.edit_data_IXC('cliente_contrato', contratos, payload)

clientes = []
for x in contratos:
    dados = IXC.get_info_IXC('cliente_contrato', 'id', '=', x)
    id_cliente = dados['registros'][0]['id_cliente']
    clientes.append(id_cliente)

print(clientes)    
payload = {
    'filial_id': '2',
}

IXC.edit_data_IXC('cliente',clientes,payload)