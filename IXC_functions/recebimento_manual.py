import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from IXC_main import *

lista = (('304433', '100,00', '21/03/2025', '45114'),
)

log = []
for x in lista: 
    payload = {
        "filial_id": "2",  # filial do recebimento
        "id_receber": x[0],  # id do título
        "conta_": "12",  # conta que está fazendo o recebimento
        "id_conta": "1",  # planejamento analítico da conta que está fazendo o recebimento
        "tipo_recebimento": "D",  # tipo recebimento em dinheiro
        "data": x[2],  # data do recebimento
        "valor_parcela": x[1],  # valor da parcela
        "credito": x[1],  # crédito e débito devem se anular na baixa
        "debito": x[1],
        "valor_total_recebido": x[1],  # valor total
        "historico": "BAIXA NETFIBRALINE - ID SGP: " + x[3] + " - IXC: " + x[0],  # descrição registrada
        "previsao": "N",  # Previsão = S significa isentar de um período, previsão = N significa que foi cobrado
        "tipo_lanc": "R",  # tipo de lançamento recebimento
    }

    dados = IXC.send_to_IXC('fn_areceber_recebimentos_baixas_novo',payload)
    pp(dados)
    log.append(dados)

IXC.create_log(log)