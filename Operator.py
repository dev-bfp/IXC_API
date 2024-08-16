from IXC_main import *


filtro = (['status','=','A'],['desconto_fidelidade','=',''])
ret = ['id','razao','desconto_fidelidade','taxa_instalacao','id_produto_ativ']
dados = IXC.get_info_IXC('cliente_contrato', return_list=ret, param=filtro)
print(dados)

df = pd.DataFrame(dados['registros'],columns=ret)
df.to_excel('C:/Users/brian/OneDrive/dev-bfp/GitHub/IXC_API/generated files/contrato_taxafidelidade1.xlsx', index= False)


# lista = []
# payload = {
#     'desconto_fidelidade': '600,00',
# }
# IXC.edit_data_IXC('cliente_contrato',lista,payload)

