
import requests
import base64
import json
from datetime import datetime
from pprint import pp as pp
from Tokens import *
import pandas as pd

class IXC():

    def parameters_format(parameters):
        '''
        Formata os parâmetros no padrão utilizado
        '''
        cabecalho = ['TB','OP','P']
        param = []
        for p in parameters:
            param.append(dict(zip(cabecalho,p)))
        print(param)
        return param
        # -------------------- Fim --------------------


    def create_log(response,diretory='',modo='w+'):
        now = datetime.now().strftime("%d-%m-%Y %Hh%Mm%Ss")
        diretory = r'C:\Users\Financeiro\OneDrive\dev-bfp\GitHub\IXC_API\logs\log_IXC_' +now+ '.csv' if diretory == '' else diretory
        with open(diretory,str(modo)) as log:
            for x in response:
                log.write(str(x)+ '\n')
        # -------------------- Fim --------------------


    def swap(value_to_swap, source_table, table_column, value_return):
        data = IXC.get_info_IXC(source_table,table_column,'=',value_to_swap)['registros'][0]
        return data[value_return]
        # -------------------- Fim --------------------


    def update_date(date):
        '''
        Atualiza os campos de data para um formato aceito pelo IXC
        '''
        if date == '0000-00-00':
            return ''
        
        elif len(date) == 10:
            try:
                formated_date = datetime.strptime(date,'%Y-%m-%d')
                finaly_date = formated_date.strftime('%d/%m/%Y')
                return finaly_date
            except:
                return date
        
        elif len(date) == 19:
            try:
                formated_date = datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
                finaly_date = formated_date.strftime("%d/%m/%Y %H:%M:%S")
                return finaly_date
            except:
                return date
        # -------------------- Fim --------------------


    def type_verificator(payload):
        data = payload
        data_formated = {}
        for key,value in data.items():
            if len(value) == 10 or len(value) == 19:
                check = value.split('-')
                if len(check) == 3:
                    data_formated[key] = IXC.update_date(value)
                    # print(f'Formatado {key}: {value} para {data_formated[key]}')
                else:
                    pass

        data.update(data_formated)
        return data
        # -------------------- Fim --------------------


    def edit_data_IXC(table, id_list, payload):
        '''
        table = tabela do IXC que será alterada
        id_list = lista de ID's dos dados a serem alterados
        payload = lista em dict dos campos a serem alterados
        '''
        array_log = []
        index = 1
        for x in id_list:
            edited = IXC.edit_info_IXC(table,x,payload)
            print(f'ID: {x} == {edited['type']} - {edited['message']}')
            print()
            array_log.append(f'id: {x} - {edited}')
            index += 1

        IXC.create_log(array_log)
        # -------------------- Fim --------------------


    def return_list(response,return_list):
        array = []
        for dados in response['registros']:
            array2 = {}
            for key, value in dados.items():
                if key in return_list:
                    array2[key] = value
            array.append(array2)
        response['registros'] = array
        return response
        # -------------------- Fim --------------------        


    def file_upload_ixc(id_cliente, arquivo, tipo_arquivo, nome_arquivo):
        '''
            Adiciona arquivos no IXC
            id_cliente = id do cliente no IXC
            arquivo = request.get(link) ou caminho local
            tipo_arquivo = PDF, JPG, PNG, MP3, etc.
            nome_arquivo = nome do arquivo
        '''
        url = IXC_url + 'cliente_arquivos'
        encode = base64.b64encode(IXC_token.encode('utf-8')).decode('utf-8')
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


    def get_info_IXC(tab, col='id', op='>', value=0, return_list='', param='', pag="1", lin="10000000",
                     ord_camp='id', order='asc'):
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
        url = IXC_url + tab
        encode = base64.b64encode(IXC_token.encode('utf-8')).decode('utf-8')
        headers = {
            'ixcsoft': 'listar',
            'Authorization': "Basic " + encode,
            'Content-Type': 'application/json'
        }
        
        payload = {
                'qtype': col,
                'query': value,
                'oper': op,
                'page': pag,
                'rp': lin,
                'sortname': ord_camp,
                'sortorder': order,
            }
        if param != '':
            param = IXC.parameters_format(param)
            payload['grid_param'] = json.dumps(param)

        print(f'Tabela: "{tab}"\nParâmetros: {payload}')
        
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            # pp(response.json())
            try:
                data = response.json()
                if int(data['total']) > 0:
                    return_list = IXC.return_list(data,return_list) if return_list != '' else data
                    return return_list
                else:
                    print('Sem registros - Verifique os parametros inseridos***')
                    return False, '***Sem registros - Verifique os parametros inseridos***'
            except:
                msg = 'Erro na solicitação, verifique os parametros inseridos'
                print(msg)
                return False, msg
        else:
            # pp(response.text)
            return "Error" + response.json()
        
        # -------------------- Fim --------------------

    
    def edit_info_IXC(tab, id, payload):
        '''
        tab - Tabela do IXC
        id = id do da coluna para pesquisa
        payload = alterações a serem realizadas
        '''
        print(f'Atualizando ID: {id} da tabela {tab}')
        dados = dict(IXC.get_info_IXC(tab,col='id',op='=',value=id)['registros'][0])
        dados.update(payload)
        payload1 = IXC.type_verificator(dados)
        dados.update(payload1)
        
        #pp(dados)
        
        url = f"https://crm.redfibra.com.br/webservice/v1/{tab}/{id}"
        encode = base64.b64encode(IXC_token.encode('utf-8')).decode('utf-8')
        headers = {
            'ixcsoft': '',
            'Authorization': "Basic " + encode,
            'Content-Type': 'application/json'
        }

        response = requests.put(url, data=json.dumps(dados), headers=headers)
        if response.status_code == 200:
            #pp(response.json())
            retorno = response.json()
            return retorno
        else:
            pp(response.text)
            return "Error" + response.text
        # -------------------- Fim --------------------
        

    def close_OS(id_os, mensagem):
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        url = IXC_url + 'su_oss_chamado_fechar'
        encode = base64.b64encode(IXC_token.encode('utf-8')).decode('utf-8')
        headers = {
                    "ixcsoft": "",
                    "Authorization": "Basic " + encode,}
        
        payload = { 'id_chamado': id_os,
                    'mensagem' : mensagem,
                    'status' : 'F',
                    'id_atendente': '76',
                    'id_tecnico': '76',
                    'data_inicio': date,
                    'data_final': date,
                    }
        
        response = requests.post(url, headers=headers, data=payload)
        print(response.json())


if __name__ == "__main__":
    grid = [["id", "=", "226226"],["status", "=", "A"]]
    IXC.get_info_IXC("fn_areceber",param=grid)