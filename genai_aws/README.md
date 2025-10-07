# 📘 Guía Práctica: AWS Bedrock con RAG

Este directorio contiene la **guía práctica completa** para implementar **Retrieval-Augmented Generation (RAG)** usando **Amazon Bedrock**, incluyendo configuración paso a paso, código de demostración y documentos de prueba.

## 👥 **Autores**

- **Rafaela Sofía Ruiz Pizarro** - A00395368  
- **Pablo Fernando Pineda Patiño** - A00395831


## 📁 Archivos Incluidos

- **`Pratical guide_ AWS Bedrock with RAG.pdf`** - 📖 Guía completa paso a paso
- **`demo_bedrock.py`** - 🐍 Código funcional de demostración
- **`BATMAN.pdf`** - 📄 Documento de ejemplo para testing

## 🚀 Inicio Rápido

### Paso 1: Revisar la Guía
Consulta la guía práctica en PDF para entender:
- Los conceptos fundamentales de RAG
- La arquitectura de la solución
- Los requisitos de configuración

### Paso 2: Configurar AWS
Siguiendo la guía, configura:
- Tu cuenta de AWS Bedrock
- Una Knowledge Base funcional
- Los permisos y credenciales necesarios

### Paso 3: Ejecutar el Demo
```bash
# Instalar dependencias
pip install boto3

# Configurar variables en demo_bedrock.py
KNOWLEDGE_BASE_ID = "tu-kb-id"
AWS_ACCESS_KEY = "tu-access-key"
AWS_SECRET_KEY = "tu-secret-key"
AWS_REGION = "us-west-2"

# Ejecutar demo
python demo_bedrock.py
```

## � Requisitos Técnicos

### AWS Services:
- **Amazon Bedrock** - Modelos fundacionales
- **Amazon S3** - Almacenamiento de documentos
- **Amazon OpenSearch** - Vector database
- **IAM** - Gestión de permisos

### Herramientas de Desarrollo:
- **Python 3.8+** 
- **boto3** SDK
- **AWS CLI** (opcional)
- **IDE** de tu preferencia