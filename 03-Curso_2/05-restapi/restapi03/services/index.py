import json
import boto3
import os
import uuid

# Obtém o nome da tabela do DynamoDB a partir das variáveis de ambiente
table_name = os.environ.get('TABLE_NAME')

# Cria um cliente do DynamoDB
dynamodb = boto3.resource('dynamodb')

# Seleciona a tabela especificada pelo nome obtido das variáveis de ambiente
table = dynamodb.Table(table_name)

def handler(event, context):
    
    # Extrai o método HTTP da requisição
    method = event["httpMethod"]

    # Processamento para o método POST
    if method == "POST":
        # Decodifica o corpo da requisição para um dicionário Python
        item = json.loads(event["body"])
        
        # Gera um ID único para o item
        item["id"] = str(uuid.uuid4())
        
        # Insere o item na tabela do DynamoDB
        table.put_item(Item=item)
        
        # Retorna uma resposta HTTP com status 200 e o ID do item criado
        return {
            "statusCode": 200,
            "body": json.dumps({"id": item["id"]}),
        }

    # Processamento para o método GET
    if method == "GET":
        # Extrai o ID do empregado dos parâmetros da URL
        empl_id = event['queryStringParameters']['id']
        
        # Busca o item na tabela do DynamoDB usando o ID
        response = table.get_item(
            Key={
                "id": empl_id
            }
        )
        
        # Verifica se o item foi encontrado
        if "Item" in response:
            # Retorna uma resposta HTTP com status 200 e os dados do empregado encontrados
            return {
                "statusCode": 200,
                "body": json.dumps(response['Item']),
            }
        else:
            # Retorna uma resposta HTTP com status 404 indicando que o empregado não foi encontrado
            return {
                "statusCode": 404,
                "body": json.dumps("Not found"),
            }