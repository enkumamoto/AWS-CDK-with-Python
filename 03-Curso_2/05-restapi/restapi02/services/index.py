import json 
import boto3  # Importação da biblioteca boto3 para interação com serviços AWS
import os
import uuid  # Importação da biblioteca uuid para geração de IDs únicos

table_name = os.environ.get("TABLE_NAME")  # Recuperação do nome da tabela do DynamoDB a partir de uma variável de ambiente
dynamodb = boto3.resource("dynamodb")  # Inicialização do cliente DynamoDB
table = dynamodb.Table(table_name)  # Referência à tabela específica pelo nome obtido acima

def handler(event, context):  # Define o ponto de entrada da função Lambda
    method = event["httpMethod"]  # Determina o método HTTP da requisição

    if method == "POST":  # Se o método for POST
        item = json.loads(event["body"])  # Carrega o corpo da requisição como um objeto Python
        item["id"] = str(uuid.uuid4())  # Gera um novo ID único para o item
        table.put_item(Item=item)  # Insere o item na tabela DynamoDB
        return {  # Retorna uma resposta HTTP
            "statusCode": 200,
            "body": json.dumps({"id": item["id"]}),  # Corpo da resposta contendo o ID gerado
        }

    if method == "GET":  # Se o método for GET
        empl_id = event["queryStringParameters"]["id"]  # Extrai o parâmetro de consulta 'id'
        response = table.get_item(Key={"id": empl_id})  # Busca o item na tabela usando o ID
        if "Item" in response:  # Verifica se o item foi encontrado
            return {  # Retorna uma resposta HTTP com o item encontrado
                "statusCode": 200,
                "body": json.dumps(response["Item"]),  # Corpo da resposta contendo os dados do item
            }
        else:
            return {  # Retorna uma resposta HTTP indicando que o item não foi encontrado
                "statusCode": 404,
                "body": json.dumps("Not found"),  # Corpo da resposta indicando falha na busca
            }