# Laboratorio Práctico: De Prompt Simple a Prompt Avanzado

Este archivo contiene una serie de ejercicios diseñados para demostrar empíricamente la diferencia entre un prompt simple (ingenuo) y un prompt estructurado (avanzado). La meta es que puedas ejecutar ambos, comparar los resultados y validar la teoría aprendida en la guía principal.

---

## Instrucciones

Para cada ejercicio:
1.  **Copia y pega el "Prompt Simple"** en tu LLM de preferencia (ChatGPT, Claude, Gemini, etc.).
2.  **Guarda la respuesta** generada.
3.  **Copia y pega el "Prompt Avanzado"** en el mismo LLM.
4.  **Guarda la respuesta** generada.
5.  **Compara ambas respuestas** usando los "Criterios de Evaluación" sugeridos. Anota tus observaciones.

---

### Ejercicio 1: Generación de una Función de Código

**Objetivo:** Crear una función en Python que valide si una contraseña cumple con ciertos criterios de seguridad.

#### 1.A: Prompt Simple

```
Haz una función en Python para validar una contraseña.
```
Resultado:

```
import re

def validar_contrasena(contrasena):
    """
    Valida una contraseña según los siguientes criterios:
      - Mínimo 8 caracteres
      - Al menos una letra mayúscula
      - Al menos una letra minúscula
      - Al menos un número
      - Al menos un carácter especial (!@#$%^&*(),.?":{}|<>)
    """

    if len(contrasena) < 8:
        return "La contraseña debe tener al menos 8 caracteres."

    if not re.search(r"[A-Z]", contrasena):
        return "Debe contener al menos una letra mayúscula."

    if not re.search(r"[a-z]", contrasena):
        return "Debe contener al menos una letra minúscula."

    if not re.search(r"\d", contrasena):
        return "Debe contener al menos un número."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contrasena):
        return "Debe contener al menos un carácter especial."

    return "Contraseña válida ✅"


# Ejemplo de uso
print(validar_contrasena("Hola123"))          # Muy débil
print(validar_contrasena("Hola123!"))         # Fuerte
print(validar_contrasena("holamundo123!"))    # Sin mayúscula

```

#### 1.B: Prompt Avanzado

```
**Rol:** Eres un desarrollador de software senior especializado en ciberseguridad.

**Tarea:** Genera una función en Python llamada `validar_contrasena`.

**Contexto:** La función recibirá una cadena de texto (la contraseña) y debe retornar `True` si cumple con TODAS las siguientes reglas, o `False` si falla al menos una.

**Reglas de Validación (Criterios):**
1.  Debe tener una longitud mínima de 12 caracteres.
2.  Debe contener al menos una letra mayúscula (A-Z).
3.  Debe contener al menos una letra minúscula (a-z).
4.  Debe contener al menos un número (0-9).
5.  Debe contener al menos un carácter especial (ej: @, #, $, %, &, !).

**Formato de Salida:**
-   El bloque de código de la función en Python.
-   Debe incluir docstrings que expliquen qué hace la función, sus parámetros y qué retorna.
-   Añade 3 ejemplos de uso: uno con una contraseña válida y dos con contraseñas inválidas que demuestren diferentes fallos.

**Restricciones:**
-   No uses librerías externas, solo el core de Python.
-   El código debe ser legible y seguir las convenciones de estilo de PEP 8.
```

Resultado:

```
import re

def validar_contrasena(contrasena: str) -> bool:
    """
    Valida la fortaleza de una contraseña según criterios de seguridad establecidos.

    Criterios:
        1. Longitud mínima de 12 caracteres.
        2. Contiene al menos una letra mayúscula (A-Z).
        3. Contiene al menos una letra minúscula (a-z).
        4. Contiene al menos un número (0-9).
        5. Contiene al menos un carácter especial (por ejemplo: @, #, $, %, &, !).

    Parámetros:
        contrasena (str): La contraseña a validar.

    Retorna:
        bool: True si la contraseña cumple con todos los criterios, False en caso contrario.
    """
    # Verificar longitud mínima
    if len(contrasena) < 12:
        return False

    # Verificar al menos una mayúscula
    if not re.search(r"[A-Z]", contrasena):
        return False

    # Verificar al menos una minúscula
    if not re.search(r"[a-z]", contrasena):
        return False

    # Verificar al menos un número
    if not re.search(r"\d", contrasena):
        return False

    # Verificar al menos un carácter especial
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contrasena):
        return False

    return True


# ==========================
# Ejemplos de uso
# ==========================

# ✅ Contraseña válida
print(validar_contrasena("SeguraFuerte2025!"))   # True

# ❌ Inválida: sin carácter especial
print(validar_contrasena("ClaveSegura2025"))     # False

# ❌ Inválida: muy corta y sin mayúsculas
print(validar_contrasena("segura2025!"))         # False

```
#### 1.C: Evaluación Comparativa

-   **Completitud:** ¿La función del prompt simple incluyó todas las reglas?
-   **Claridad:** ¿El código está bien documentado? ¿Es fácil de entender?
-   **Utilidad:** ¿El prompt avanzado proporcionó ejemplos de uso que facilitan la prueba y la integración?
-   **Robustez:** ¿La función maneja casos borde que el prompt simple podría haber ignorado?

Resultado:


**Completitud**

La función del **prompt simple** no incluyó todas las reglas.
Solo exigía:

- 8 caracteres mínimos,
una mayúscula,
una minúscula,
un número,
y un carácter especial.

El **prompt avanzado**, en cambio, amplió el criterio de longitud a 12 caracteres mínimos y dejó los demás claramente definidos, asegurando un control más estricto y completo sobre la seguridad de la contraseña.


**Claridad**

El **primer código** es comprensible, pero su documentación es limitada: explica las reglas dentro del código, pero sin detallar parámetros ni valores de retorno.
El **segundo código** (prompt avanzado) incluye:

docstrings bien formateados según PEP 257,
descripción clara de criterios, parámetros y retorno,
estructura limpia y legible.

**Utilidad**

El **prompt avanzado** agrega tres ejemplos de uso, mostrando casos de éxito y de fallo.
Esto facilita:

- la verificación inmediata del comportamiento,
la integración en pruebas automatizadas,
y el entendimiento de qué tipo de contraseñas fallan.

El **prompt simple** solo mostraba algunos print, sin representar todos los posibles errores.

**Robustez**

El **prompt simple** era funcional, pero no manejaba algunos casos borde, como:

contraseñas cortas menores a 12 caracteres (porque el umbral era más bajo),
posibles strings vacíos,
ni validación estricta de criterios con valores límite.

El **prompt avanzado**, aunque tampoco usa manejo de excepciones explícito (porque no es necesario aquí), sí mejora la robustez lógica, ya que:

aplica validaciones más estrictas,
usa expresiones regulares bien definidas,
y garantiza el retorno booleano exacto (True o False).

---

### Ejercicio 2: Extracción de Información a Formato JSON

**Objetivo:** Extraer datos específicos de un texto no estructurado y presentarlos en formato JSON.

#### 2.A: Prompt Simple

```
Saca los datos importantes de este texto en JSON:

"La reunión de lanzamiento del Proyecto Fénix será el 15 de octubre de 2024 a las 10:30 AM en la Sala Júpiter. Los asistentes confirmados son Ana García (Líder de Proyecto), Carlos Rodríguez (Desarrollador Principal) y Elena Fernández (Diseñadora UX). El presupuesto asignado es de $25,000 USD."
```

Resultado:
```
{
  "proyecto": "Proyecto Fénix",
  "evento": "Reunión de lanzamiento",
  "fecha": "2024-10-15",
  "hora": "10:30 AM",
  "lugar": "Sala Júpiter",
  "asistentes": [
    {
      "nombre": "Ana García",
      "rol": "Líder de Proyecto"
    },
    {
      "nombre": "Carlos Rodríguez",
      "rol": "Desarrollador Principal"
    },
    {
      "nombre": "Elena Fernández",
      "rol": "Diseñadora UX"
    }
  ],
  "presupuesto": {
    "monto": 25000,
    "moneda": "USD"
  }
}
```

#### 2.B: Prompt Avanzado

```
**Rol:** Eres un asistente de procesamiento de datos altamente preciso.

**Tarea:** Extrae la información clave del siguiente texto y formatéala estrictamente como un objeto JSON.

**Texto de Entrada:**
```
La reunión de lanzamiento del Proyecto Fénix será el 15 de octubre de 2024 a las 10:30 AM en la Sala Júpiter. Los asistentes confirmados son Ana García (Líder de Proyecto), Carlos Rodríguez (Desarrollador Principal) y Elena Fernández (Diseñadora UX). El presupuesto asignado es de $25,000 USD.
```

**Esquema JSON de Salida (Schema):**
Debes seguir esta estructura exacta. Si un campo no se encuentra en el texto, déjalo como `null`.

```json
{
  "proyecto": {
    "nombre": "string",
    "presupuesto": {
      "monto": "number",
      "moneda": "string"
    }
  },
  "reunion": {
    "fecha": "string (formato YYYY-MM-DD)",
    "hora": "string (formato HH:MM)",
    "ubicacion": "string"
  },
  "asistentes": [
    {
      "nombre": "string",
      "rol": "string"
    }
  ]
}
```

**Restricciones:**
-   El `monto` del presupuesto debe ser un número, no un string.
-   La `fecha` y `hora` deben ser normalizadas a los formatos especificados.
-   No incluyas campos que no estén en el esquema.


Resultado:
```
{
  "proyecto": {
    "nombre": "Proyecto Fénix",
    "presupuesto": {
      "monto": 25000,
      "moneda": "USD"
    }
  },
  "reunion": {
    "fecha": "2024-10-15",
    "hora": "10:30",
    "ubicacion": "Sala Júpiter"
  },
  "asistentes": [
    {
      "nombre": "Ana García",
      "rol": "Líder de Proyecto"
    },
    {
      "nombre": "Carlos Rodríguez",
      "rol": "Desarrollador Principal"
    },
    {
      "nombre": "Elena Fernández",
      "rol": "Diseñadora UX"
    }
  ]
}

```


#### 2.C: Evaluación Comparativa

-   **Estructura:** ¿El JSON del prompt simple tiene una estructura lógica y predecible?
-   **Precisión:** ¿Los tipos de datos son correctos (números vs. strings)?
-   **Parseabilidad:** ¿El JSON generado por el prompt avanzado es directamente utilizable por una aplicación sin necesidad de limpieza o conversión?
-   **Manejo de Nulos:** ¿Cómo manejaría cada uno un texto donde, por ejemplo, el presupuesto no se menciona?


Resultado:

1. Estructura

**Prompt simple:**
Sí, el JSON del prompt simple tiene una estructura lógica y predecible. Usa claves coherentes (proyecto, evento, fecha, hora, lugar, asistentes, presupuesto) y anidación razonable.
Sin embargo, no estaba guiado por un esquema explícito, por lo que diferentes textos podrían generar ligeras variaciones (por ejemplo, usar lugar vs ubicacion o incluir/excluir evento).

**Prompt complejo:**
Tiene una estructura estrictamente definida gracias al esquema proporcionado. Esto garantiza consistencia entre distintas ejecuciones y facilita la automatización del parsing.

2. Precisión

**Prompt simple:**
Los tipos de datos son correctos en este caso (monto como número, moneda como string), pero como no se definieron reglas explícitas, podría variar si el texto fuera ambiguo o si se usaran formatos distintos (por ejemplo, “25 mil dólares” podría causar un error de tipo).

**Prompt complejo:**
La precisión es mayor, porque las reglas del esquema especifican los tipos (monto numérico, fecha en formato YYYY-MM-DD, etc.). Esto reduce el riesgo de inconsistencias.

3. Parseabilidad

**Prompt simple:**
Es parseable por JSON, pero puede requerir ajustes manuales si los nombres de campos cambian o si los formatos no son consistentes (por ejemplo, hora en formato “10:30 AM” en lugar de “10:30”).

**Prompt complejo:**
Es totalmente parseable y listo para usar por una aplicación. Cumple el formato JSON estándar y usa valores normalizados, lo que permite integrarlo directamente en bases de datos o APIs.

4. Manejo de Nulos

**Prompt simple:**
No define cómo manejar la ausencia de datos. Si un campo no aparece (por ejemplo, presupuesto), simplemente no se incluiría en el JSON, lo que podría causar errores en sistemas que esperan ese campo.

**Prompt complejo:**
Define explícitamente que los campos faltantes deben colocarse como null, lo que garantiza robustez y compatibilidad con validadores JSON Schema o bases de datos estructuradas.

---

### Ejercicio 3: Escritura Creativa con Tono y Estilo

**Objetivo:** Escribir un párrafo corto sobre un tema complejo, adaptado a una audiencia específica.

#### 3.A: Prompt Simple

```
Escribe sobre los agujeros negros.
```

Resultado:
```
Los **agujeros negros** son uno de los fenómenos más fascinantes y misteriosos del universo. Se trata de regiones del espacio donde la **gravedad es tan intensa** que nada puede escapar de su atracción, ni siquiera la luz. Por eso se llaman “negros”: porque no emiten ninguna radiación visible y resultan invisibles directamente.

---

### **Formación**

La mayoría de los agujeros negros se forman cuando una **estrella masiva** (al menos tres veces más grande que el Sol) agota su combustible nuclear. En ese punto, la presión interna que mantenía la estrella estable ya no puede contrarrestar la gravedad, y el núcleo colapsa sobre sí mismo. Este colapso comprime toda la masa en un punto infinitamente denso llamado **singularidad**, rodeado por una frontera invisible llamada **horizonte de sucesos**: el límite más allá del cual nada puede volver.

---

### **Tipos de agujeros negros**

Existen varios tipos según su masa y origen:

1. **Agujeros negros estelares:**
   Se forman a partir del colapso de estrellas masivas. Suelen tener entre 3 y 100 veces la masa del Sol.

2. **Agujeros negros supermasivos:**
   Se encuentran en el centro de la mayoría de las galaxias, incluida la Vía Láctea. Tienen millones o miles de millones de masas solares. Su origen aún no se comprende del todo, aunque se cree que crecieron absorbiendo materia y fusionándose con otros agujeros negros.

3. **Agujeros negros intermedios:**
   Representan una categoría intermedia, con masas entre cientos y miles de soles. Son difíciles de detectar, pero se han identificado algunos candidatos.

4. **Agujeros negros primordiales:**
   Hipotéticos agujeros negros formados poco después del Big Bang, debido a densidades extremas en el universo temprano.

---

### **Efectos y observaciones**

Aunque los agujeros negros no pueden observarse directamente, los astrónomos pueden **detectar su presencia** observando cómo afectan a su entorno. Por ejemplo:

* Las **estrellas que orbitan** alrededor de un punto invisible.
* La **radiación X** emitida por la materia que cae hacia el agujero negro (acreción).
* Las **ondas gravitacionales**, generadas por la fusión de agujeros negros, detectadas por observatorios como LIGO y Virgo.

En 2019, el **Telescopio del Horizonte de Sucesos (EHT)** logró la **primera imagen directa** de la sombra de un agujero negro en la galaxia M87, marcando un hito histórico en la astrofísica.

---

### **Efectos físicos y teóricos**

Cerca del horizonte de sucesos, el espacio y el tiempo se deforman drásticamente. La **relatividad general de Einstein** describe estos efectos con precisión, prediciendo fenómenos como la **dilatación del tiempo** (el tiempo pasa más lento cerca del agujero negro) y la **curvatura extrema del espacio**.

A nivel cuántico, los agujeros negros también son un enigma. Stephen Hawking propuso que emiten una débil radiación llamada **radiación de Hawking**, lo que sugiere que podrían **evaporarse lentamente** con el tiempo, desafiando nuestra comprensión de la física fundamental.

---

### **Conclusión**

Los agujeros negros son laboratorios naturales donde la física clásica y la cuántica se enfrentan. A pesar de su nombre sombrío, son esenciales para entender cómo funciona el universo: influyen en la formación de galaxias, en la dinámica cósmica y en los límites del conocimiento humano.

---

```

#### 3.B: Prompt Avanzado

```
**Rol:** Eres un divulgador científico como Carl Sagan, capaz de explicar conceptos complejos con asombro y claridad.

**Tarea:** Escribe un párrafo corto (aproximadamente 100 palabras) sobre los agujeros negros.

**Audiencia:** Niños de 10 a 12 años.

**Tono y Estilo:**
-   Usa un lenguaje sencillo y evocador.
-   Evita la jerga técnica y las fórmulas matemáticas.
-   Utiliza analogías o metáforas fáciles de entender (ej: "un aspirador cósmico del que ni la luz puede escapar").
-   El tono debe ser de misterio y fascinación, no de miedo.

**Formato de Salida:**
-   Un único párrafo de texto.

**Restricción:**
-   No menciones la "singularidad" o la "relatividad general" directamente. Enfócate en el fenómeno observable.
```

Resultado:

Los agujeros negros son como puertas secretas en el universo, lugares donde la gravedad es tan fuerte que nada puede escapar, ¡ni siquiera la luz! Imagina un aspirador cósmico escondido en la oscuridad, tragándose todo lo que se acerque demasiado: polvo de estrellas, planetas e incluso la luz misma. Aunque no podemos verlos directamente, los astrónomos los descubren observando cómo bailan las estrellas a su alrededor o cómo brilla el gas cuando cae en su interior. Son los grandes misterios del cosmos, silenciosos y poderosos, recordándonos que el universo aún guarda muchos secretos por descubrir.


#### 3.C: Evaluación Comparativa

-   **Adecuación a la Audiencia:** ¿Qué respuesta es más apropiada y comprensible para un niño?
-   **Tono:** ¿Logró el prompt simple capturar el tono de asombro solicitado?
-   **Creatividad:** ¿Qué respuesta es más original y memorable?
-   **Cumplimiento de Restricciones:** ¿El prompt avanzado logró evitar la jerga técnica como se le pidió?


Resultado:

**1. Adecuación a la Audiencia**

La **respuesta del prompt avanzado** es claramente más apropiada para un niño de 10 a 12 años.
Usa un lenguaje sencillo, imágenes visuales (“aspirador cósmico”, “puertas secretas en el universo”) y evita términos difíciles. El texto transmite curiosidad sin abrumar con tecnicismos.


**2. Tono**

El **prompt simple**, aunque correcto, probablemente ofrecía una descripción más neutra o informativa.
En cambio, el **prompt avanzado** logra un tono de **asombro y fascinación**, evocando el misterio del cosmos con frases poéticas (“silenciosos y poderosos”, “secretos por descubrir”).


**3. Creatividad**

La respuesta del **prompt avanzado** destaca por su creatividad. Las metáforas visuales y el estilo narrativo invitan a imaginar el fenómeno, algo esencial en la divulgación para niños.
El texto no solo informa, sino que también **despierta curiosidad** y emoción.


**4. Cumplimiento de Restricciones**

El **prompt avanzado** cumple perfectamente con las restricciones:

* No usa jerga técnica (no menciona “singularidad” ni “relatividad general”).
* Se enfoca en lo observable y en la experiencia visual del fenómeno.


---

### Conclusión de los Ejercicios

Al realizar estos laboratorios, deberías notar que los prompts avanzados no solo dan respuestas "mejores", sino que producen resultados:
-   **Más predecibles y consistentes.**
-   **Más fáciles de integrar en flujos de trabajo automatizados.**
-   **Alineados con objetivos de negocio o de producto muy específicos.**
-   **Que requieren menos post-procesamiento manual.**

¡La ingeniería de prompts es el arte de la especificación precisa para obtener resultados de alta calidad!
