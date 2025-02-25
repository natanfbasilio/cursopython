import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "codigo_conta_twilio"
# Your Auth Token from twilio.com/console
auth_token = "token_twilio"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel. Lista sempre colocada em colchetes
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# Para cada arquivo:
# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+seunumero",
            from_="+numero_gerado_twilio",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)

# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor