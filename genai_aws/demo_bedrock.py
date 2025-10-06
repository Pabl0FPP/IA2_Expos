import boto3
import json

# 🔧 CONFIGURACIÓN - CAMBIA ESTOS VALORES
KNOWLEDGE_BASE_ID = "TU_KNOWLEDGE_BASE_ID_AQUI"
AWS_ACCESS_KEY = "TU_AWS_ACCESS_KEY_AQUI"
AWS_SECRET_KEY = "TU_AWS_SECRET_KEY_AQUI"
AWS_REGION = "us-west-2"  # ← Tu región

MODEL_ARN = "us.amazon.nova-micro-v1:0"

def hacer_pregunta(pregunta):
    bedrock = boto3.client(
        'bedrock-agent-runtime',
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )
    
    try:
        respuesta = bedrock.retrieve_and_generate(
            input={'text': pregunta},
            retrieveAndGenerateConfiguration={
                'type': 'KNOWLEDGE_BASE',
                'knowledgeBaseConfiguration': {
                    'knowledgeBaseId': KNOWLEDGE_BASE_ID,
                    'modelArn': MODEL_ARN
                }
            }
        )
        return respuesta['output']['text']
    except Exception as e:
        return f"Error: {str(e)}"

# USO
print("🤖 Pregunta lo que quieras sobre tus documentos:")
while True:
    user_input = input("\nTú: ")
    if user_input.lower() == 'salir':
        break
    respuesta = hacer_pregunta(user_input)
    print(f"Bot: {respuesta}")