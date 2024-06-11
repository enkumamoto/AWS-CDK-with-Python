from hook import lambda_handler  # Importa a função lambda_handler do módulo 'hook'

event = {  # Define um dicionário simbolizando um evento
    'Records' : [{  # O evento é estruturado como uma lista de registros
        'Sns' : {  # Dentro de cada registro, há um componente SNS (Simple Notification Service)
            'Message' : 'Test Message',  # A mensagem dentro do componente SNS é definida como 'test message'
        }
    }]
}

lambda_handler(event, {})  # Chama a função lambda_handler passando o evento simulado e um contexto vazio