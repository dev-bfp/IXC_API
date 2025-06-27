📦 Integração com API IXC - Automação e Utilitários
Este repositório contém uma biblioteca Python desenvolvida para automatizar e facilitar integrações com o sistema IXC Provedor via API REST. Ele oferece uma série de métodos reutilizáveis para:

✅ Funcionalidades principais
🔄 Envio e edição de dados em qualquer tabela do IXC

🔍 Consultas customizadas com filtros avançados e paginação

🔃 Formatação automática de datas e tratamento de payloads

🧠 Conversão e substituição de valores manualmente com replace_manual

📂 Upload de arquivos em cadastros de clientes

🧾 Geração de logs CSV das operações executadas

🛠️ Fechamento automático de OS, liberação temporária e desbloqueios de confiança

📁 Estrutura
O arquivo principal é IXC_main.py, que centraliza todas as funções. As credenciais e configurações como IXC_url e IXC_token devem estar em um módulo separado chamado Tokens.py.

⚠️ Requisitos
Python 3.7+

Bibliotecas: requests, pandas, base64, datetime, csv

🚀 Exemplo de uso
python

from IXC_main import IXC

# Buscar dados de clientes
dados = IXC.get_info_IXC("cliente", param=[["id", ">", "5000"]])

# Editar dados de um cliente específico
IXC.edit_data_IXC("cliente", [1234], {"nome": "Novo Nome"})

# Enviar novo registro para IXC
IXC.send_to_IXC("cliente", {"nome": "Teste", "cpf": "00000000000"})
