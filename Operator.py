from IXC_main import *


# filtro = (['cofins_retem','=','S'],)
# ret = ['id','razao']
# dados = IXC.get_info_IXC('cliente', return_list=ret, param=filtro)
# print(dados)
# if dados != 'Sem registros':
#     IXC.create_log(dados['registros'],'C:/Users/brian/OneDrive/dev-bfp/GitHub/IXC_API/generated files/clientes_tributo.csv', modo='a')

# df = pd.DataFrame(dados['registros'],columns=('id','razao'))
# df.to_excel('C:/Users/brian/OneDrive/dev-bfp/GitHub/IXC_API/generated files/clientes_tributo.xlsx', index= False)


# lista = []
# payload = {
#     'pis_retem': '',
#     'cofins_retem': '',
#     'csll_retem': '',
#     'irrf_retem': '',
#     'desconto_irrf_valor_inferior': 'S',
#     'cli_desconta_iss_retido_total': '',
# }
# IXC.edit_data_IXC('cliente',lista,payload)