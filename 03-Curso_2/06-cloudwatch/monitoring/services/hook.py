import urllib3  # Importa a biblioteca urllib3 para fazer requisições HTTP
import json    # Importa a biblioteca json para manipulação de dados JSON

http = urllib3.PoolManager()  # Cria um PoolManager para realizar requisições HTTP

def handler(event, context):  # Define a função lambda_handler que será chamada por eventos
    print("Calling Slack!!!")  # Imprime uma mensagem indicando que a chamada ao Slack está sendo feita
    
    url = ""  # Variável vazia para armazenar a URL da API do Slack
    msg = {  # Dicionário contendo a mensagem a ser enviada ao Slack
        "channel" : "#aws-events",  # Canal no Slack onde a mensagem será enviada
        "text" : event["Records"][0]["Sns"]["Message"],  # Texto da mensagem, obtido do evento SNS
    }

    encode_msg = json.dumps(msg).encode('utf-8')  # Converte o dicionário msg para JSON
    resp = http.request('POST', url, body=encode_msg)  # Faz uma requisição POST à URL especificada com a mensagem
    print({  # Imprime informações sobre a resposta recebida
        "message": event["Records"][0]["Sns"]["Message"],  # Mensagem original do evento SNS
        "status_code": resp.status,  # Código de status da resposta
        "response": resp.data  # Dados da resposta
    })