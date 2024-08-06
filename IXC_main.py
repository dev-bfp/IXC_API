import requests
import base64
import json
from pprint import pp as pp
from Tokens import *

class IXC():
    def parameters_format(parameters):
        '''
        Formata os parâmetros no padrão utilizado
        '''
        cabecalho = ['TB','OP','P']
        param = []
        for p in parameters:
            print(p)
            param.append(dict(zip(cabecalho,p)))
        print(param)
        return param
        # -------------------- Fim --------------------


    def get_info_IXC(tab, col='id', op='>', value=0, param='', pag="1", lin="10000000", ord_camp='id', ord='asc'):
        '''
        tab - Tabela do IXC
        param = Filtros adicionais array(['col','op','value'])
        col - Coluna IXC que vai ser consultada
        value - Campo da consulta
        op - Operador lógico para consulta = != > < >= <=
        pag - Qual pag vai retornar
        lin - Quantidade de registros por página
        ord_camp - Campo que vai ser usado para colocar em ordem
        ord - Ordenação ASC ou DESC
        '''
        param = IXC.parameters_format(param) if param != '' else ''
        url = ixc_url + tab
        encode = base64.b64encode(ixc_token.encode('utf-8')).decode('utf-8')
        headers = {
            'ixcsoft': 'listar',
            'Authorization': "Basic " + encode,
            'Content-Type': 'application/json'
        }
        payload = json.dumps({
                # 'qtype': col,
                # 'query': value,
                # 'oper': op,
                'page': pag,
                'rp': lin,
                'sortname': ord_camp,
                'sortorder': ord,
                'grid_param': json.dumps(param)
            })

        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 200:
            pp(response.json())
            return response.json()
        else:
            pp(response.text)
            return "Error" + response.text
        # -------------------- Fim --------------------
        
    def file_upload_ixc(id_cliente, arquivo, tipo_arquivo, nome_arquivo):
        '''
        Adiciona arquivos no IXC
        arquivo = request.get(link) ou caminho local
        tipo_arquivo = PDF, JPG, PNG, MP3, etc.
        nome_arquivo = nome do arquivo
        '''
        url = ixc_url + 'cliente_arquivos'
        encode = base64.b64encode(ixc_token.encode('utf-8')).decode('utf-8')
        headers = {
            "ixcsoft": "",
            "Authorization": "Basic " + encode,
        }
        files = {
            'local_arquivo': (nome_arquivo + '.' + tipo_arquivo, arquivo)
        }
        payload = {
            'id_cliente': id_cliente, 
            'nome_arquivo': nome_arquivo + '.' + tipo_arquivo,
            'descricao': nome_arquivo
        }

        response = requests.post(url, headers=headers, data=payload, files=files)
        if response.status_code == 200:
            pp(response.json())
            return response.json()
        else:
            pp(response.text)
            return "Error" + response.text
        # -------------------- Fim --------------------