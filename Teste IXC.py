from IXC_main import *
import pandas as pd

                        

payload = {
            'pis_retem': 'S',
            'cofins_retem': 'S',
            'csll_retem': 'S',
            'irrf_retem': 'S',
            'desconto_irrf_valor_inferior': 'S',
            'cli_desconta_iss_retido_total': '',
            }


filtro = (['pis_retem', '=','S'],['id', '>', '8540'])
return_list = ['id','razao','pis_retem','cofins_retem','cofins_retem','irrf_retem','cli_desconta_iss_retido_total']
dados = IXC.get_info_IXC('cliente',param=filtro)


# array = []
# print(dados['total'])
# for x in dados['registros']:
#     array2 = []
#     # print(x['id'], x['pis_retem'])
#     array2 += x['id'], x['pis_retem']
#     array += array2

# with open(r'C:\Users\brian\OneDrive\dev-bfp\GitHub\Homologação\tributo.xls','w+') as tributo:
#     tributo.writelines(array)
# print(array)