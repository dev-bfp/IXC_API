import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from IXC_main import *

contratos = []

payload_contratos = {'nao_bloquear_ate': '31/05/2025'}

changes = IXC.edit_data_IXC("cliente_contrato",contratos,payload_contratos)
print(changes) 