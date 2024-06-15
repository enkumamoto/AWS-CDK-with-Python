import json
import boto3 # Importa o cliente da AWS para DynamoDB
import os
import uuid # Importa o módulo uuid para gerar IDs únicas

# Obtém o nome da tabela do DynamoDB a partir de uma variável de ambiente
table_name = os.environ.get("TABLE_NAME")

# Cria um recurso do DynamoDB usando o nome da tabela
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(table_name)

def handler(event, context):
    # Determina o método HTTP da requisição
    method = event["httpMethod"]

    # Se o método for POST, processa a criação de um novo item
    if method == "POST":
        # Carrega o corpo da requisição como um dicionário Python
        item = json.loads(event["body"])
        # Gera um ID único para o novo item
        item["id"] = str(uuid.uuid4())
        # Insere o novo item na tabela do DynamoDB
        table.put_item(Item=item)
        # Retorna uma resposta com sucesso e o ID do novo item
        return {
            "statusCode": 200,
            "body": json.dumps({"id": item["id"]}),
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "*",
            }
        }

    # Se o método for GET, processa a recuperação de um item existente
    if method == "GET":
        # Extrai o ID do parâmetro de consulta da requisição
        empl_id = event["queryStringParameters"]["id"]
        # Tenta recuperar o item do DynamoDB pelo ID
        response = table.get_item(Key={"id": empl_id})
        # Verifica se o item foi encontrado
        if "Item" in response:
            # Retorna uma resposta com sucesso e os detalhes do item
            return {
                "statusCode": 200,
                "body": json.dumps(response["Item"]),
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "*",
                }
            }
        else:
            # Retorna uma resposta indicando que o item não foi encontrado
            return {
                "statusCode": 404,
                "body": json.dumps("Not found"),
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "*",
                }
            }