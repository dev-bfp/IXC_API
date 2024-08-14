from IXC_main import *
              

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
        array_log.append(f'{index} - {edited} {'\n'}')
        index += 1

    IXC.create_log(array_log)

edit_data_IXC('cliente', ['3817','5982'],{'razao': 'Ola word'})