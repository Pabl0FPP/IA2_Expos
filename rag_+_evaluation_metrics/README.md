# 🚀 RAG (Retrieval-Augmented Generation) con Métricas de Evaluación Avanzadas

Este proyecto implementa un sistema completo de **Retrieval-Augmented Generation (RAG)** utilizando **Google Gemini** y **ChromaDB**, junto con un framework comprensivo de evaluación que incluye múltiples métricas automáticas para comparar el rendimiento entre respuestas generadas con y sin RAG.

---

## 👥 **Autores**

- **Rafaela Sofía Ruiz Pizarro** - A00395368  
- **Pablo Fernando Pineda Patiño** - A00395831

---

## 🎯 **Objetivos del Proyecto**

1. **Implementar un sistema RAG funcional** que combine recuperación de información con generación de texto
2. **Desarrollar métricas de evaluación automática** para medir la calidad de respuestas generadas
3. **Comparar sistemáticamente** el rendimiento entre RAG y respuestas sin contexto externo
4. **Proporcionar análisis visual** y estadístico de los resultados obtenidos
5. **Crear una herramienta reutilizable** para futuras evaluaciones de sistemas de IA generativa

---

## 🏗️ **Arquitectura del Sistema**

### **Componentes Principales:**

```
📄 Documento de Entrada
    ↓
🔪 Chunking (División en fragmentos)
    ↓
🧠 Generación de Embeddings (SentenceTransformers)
    ↓
🗄️ Base de Datos Vectorial (ChromaDB)
    ↓
🔍 Sistema de Recuperación
    ↓
🤖 Generación de Respuestas (Google Gemini)
    ↓
📊 Evaluación con Múltiples Métricas
```

### **Métricas de Evaluación Implementadas:**

- **🎯 BLEU Score**: Precisión de n-gramas entre candidato y referencia
- **📝 ROUGE (ROUGE-1, ROUGE-L)**: Recall y F1-score para evaluación de resúmenes
- **🧠 BERTScore**: Similitud semántica usando embeddings contextuales
- **🔄 Similitud Semántica**: Similitud coseno entre embeddings de respuestas

---


## 🛠️ **Tecnologías Utilizadas**

### **Backend y RAG:**
- **Python 3.8+**
- **Google Gemini API** - Modelo de lenguaje para generación
- **ChromaDB** - Base de datos vectorial para almacenamiento de embeddings
- **SentenceTransformers** - Generación de embeddings semánticos
- **rank_bm25** - Algoritmo BM25 para recuperación basada en keywords

### **Métricas y Evaluación:**
- **NLTK** - Natural Language Toolkit para BLEU score
- **rouge-score** - Implementación de métricas ROUGE
- **bert-score** - BERTScore para similitud semántica
- **scikit-learn** - Métricas adicionales y utilidades

### **Visualización y Análisis:**
- **Matplotlib** - Gráficos y visualizaciones
- **Seaborn** - Visualizaciones estadísticas avanzadas
- **Pandas** - Manipulación y análisis de datos
- **NumPy** - Operaciones numéricas

---

## ⚙️ **Instalación y Configuración**


### **Configurar API Key de Google Gemini**

1. Ve a [Google AI Studio](https://aistudio.google.com/)
2. Crea una API Key
3. Reemplaza en el notebook la línea:
   ```python
   os.environ["GEMINI_API_KEY"] = "TU_API_KEY_AQUI"
   ```

---

## 🚀 **Uso del Sistema**

### **Ejecutar el Notebook Principal**

1. **Abre Jupyter Notebook:**
   ```bash
   jupyter notebook RAG_con_Metricas_Evaluacion.ipynb
   ```

2. **Ejecuta las celdas en orden:**
   - 📦 Instalación de librerías
   - 🔧 Configuración del entorno
   - 📄 Carga de documentos
   - 🧠 Creación del sistema RAG
   - 📊 Evaluación y comparación
   - 📈 Visualización de resultados

### **Personalizar el Sistema**

#### **Cambiar el Documento de Entrada:**
```python
# En la sección de carga de documentos
document_text = """
Tu texto personalizado aquí...
"""
```

#### **Ajustar Parámetros de Chunking:**
```python
chunks = chunk_text(document_text, chunk_size=150, overlap=30)
```

#### **Modificar Preguntas de Evaluación:**
```python
test_dataset = [
    {
        "question": "Tu pregunta personalizada",
        "reference": "Respuesta de referencia esperada"
    },
    # Añadir más preguntas...
]
```

---

## 📊 **Resultados y Métricas**

### **Métricas Implementadas:**

| Métrica | Descripción | Rango | Interpretación |
|---------|-------------|--------|----------------|
| **BLEU** | Precisión de n-gramas | 0-1 | Más alto = mejor coincidencia léxica |
| **ROUGE-1** | Unigram recall/precision/F1 | 0-1 | Más alto = mejor cobertura de contenido |
| **ROUGE-L** | Longest common subsequence | 0-1 | Más alto = mejor estructura secuencial |
| **BERTScore** | Similitud semántica contextual | 0-1 | Más alto = mejor similitud semántica |
| **Sim. Semántica** | Similitud coseno de embeddings | -1 a 1 | Más alto = mayor similitud semántica |

### **Ejemplo de Output:**

```
📊 RESUMEN DE RESULTADOS:
============================================================

📈 Promedios por enfoque:
           bleu  rouge1_f1  rougeL_f1  bertscore_f1  semantic_similarity
approach                                                                  
RAG       0.245      0.389      0.352         0.587                0.712
No-RAG    0.198      0.301      0.267         0.498                0.623

BLEU:
  RAG: 0.2453
  No-RAG: 0.1980
  Diferencia: +0.0473
  Mejora: +23.89%
```

---

## 🔬 **Metodología de Evaluación**

### **Proceso de Evaluación:**

1. **Generación de Respuestas:**
   - RAG: Usando contexto recuperado
   - No-RAG: Solo conocimiento del modelo

2. **Cálculo de Métricas:**
   - Comparación contra respuestas de referencia
   - Múltiples métricas automáticas

3. **Análisis Estadístico:**
   - Promedios, desviaciones estándar
   - Pruebas de significancia
   - Correlaciones entre métricas

4. **Visualización:**
   - Gráficos comparativos
   - Análisis de distribuciones

---

## 💡 **Conclusiones y Hallazgos**

### **Principales Observaciones:**

1. **🚀 RAG mejora significativamente** la precisión de respuestas específicas del dominio
2. **📊 BERTScore y Similitud Semántica** son las métricas más sensibles a mejoras cualitativas
3. **🎯 BLEU y ROUGE** capturan bien la precisión léxica pero pueden ser conservadores
4. **⚡ El overhead computacional** de RAG se justifica por la mejora en calidad

### **Recomendaciones:**

- **Para información específica**: RAG supera consistentemente al modelo base
- **Para conocimiento general**: La diferencia puede ser menor
- **Optimización recomendada**: Ajustar chunk size según el dominio
- **Evaluación múltiple**: Usar varias métricas para una visión completa