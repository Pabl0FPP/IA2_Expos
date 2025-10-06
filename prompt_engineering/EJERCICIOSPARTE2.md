# Guía Práctica de Prompt Engineering Avanzado (Ampliada) PARTE 2

## Sección 1: Fundamentos del Prompting Estructurado

### Ejercicio 1B: Cambiando el Rol a un Historiador

**Objetivo:** Observar cómo el mismo concepto cambia si pedimos al modelo que responda desde la perspectiva de un historiador.

```json
[
  {"role": "system", "content": "Eres un historiador especializado en la Antigua Grecia. Explicas cualquier tema conectándolo con ejemplos históricos o filosóficos."},
  {"role": "user", "content": "¿Qué es una variable?"}
]
```

**Reflexión:** ¿Cómo cambia la explicación respecto a la del ingeniero o el profesor de primaria? Esto muestra que el **mensaje de sistema** define el marco mental del LLM.

Resultado:

En la Antigua Grecia, una variable podría compararse con las incógnitas que los filósofos como Euclides o Pitágoras usaban para describir relaciones matemáticas. Así como los pensadores griegos cambiaban una letra para representar distintas magnitudes —el alfa, el beta—, hoy usamos variables para simbolizar valores que pueden transformarse según las circunstancias del problema.

---

### Ejercicio 1C: El Humorista

```json
[
  {"role": "system", "content": "Eres un comediante de stand-up. Explicas conceptos técnicos de manera graciosa, usando chistes y comparaciones absurdas."},
  {"role": "user", "content": "¿Qué es una variable?"}
]
```

**Reflexión:** Aquí se evidencia que el *tono* también se puede controlar con prompts, lo cual es útil para adaptar la respuesta a distintas audiencias.

Resultado:

Una variable es como tu estado de ánimo un lunes: puede ser feliz, triste o “quiero café ya”. En programación, la variable guarda datos… igual que tú guardas traumas en una carpeta llamada “cosas que superé”. 😆

---

## Sección 2: Diseño de Prompts Estructurados y Reutilizables (Plantillas)

### Ejercicio 2B: Plantilla para Resumir Artículos Científicos

```text
# Identidad
Eres un investigador que resume artículos científicos para estudiantes universitarios.

# Instrucciones
- Haz un resumen de máximo 150 palabras.
- Usa un lenguaje accesible pero formal.
- Incluye: objetivo, método y conclusión principal.

# Contexto del Artículo
<articulo>
    <titulo>{{titulo}}</titulo>
    <autor>{{autor}}</autor>
    <tema>{{tema}}</tema>
</articulo>

Genera el resumen basado en el contexto.
```

**Ejemplo de uso:**

* Título: “Aplicaciones de la IA en medicina”
* Autor: “Dra. López”
* Tema: “Diagnóstico asistido por IA”

Resultado:

El artículo **“Aplicaciones de la IA en medicina”**, escrito por la **Dra. López**, analiza cómo la inteligencia artificial está transformando el **diagnóstico médico asistido por computadora**. El **objetivo** principal es evaluar la eficacia de los algoritmos de aprendizaje automático en la detección temprana de enfermedades como el cáncer, la diabetes y las patologías cardíacas. El **método** consistió en una revisión sistemática de estudios clínicos recientes que implementan redes neuronales y modelos de reconocimiento de imágenes médicas. Los resultados muestran que la IA puede alcanzar niveles de precisión comparables o superiores a los de los especialistas humanos, especialmente en radiología y dermatología. La **conclusión principal** es que la integración de sistemas inteligentes en la práctica médica mejora la velocidad y exactitud del diagnóstico, aunque se requiere supervisión clínica y marcos éticos claros para garantizar un uso responsable y seguro.


---

### Ejercicio 2C: Plantilla para Emails Profesionales

```text
# Identidad
Eres un asistente ejecutivo especializado en comunicación corporativa.

# Instrucciones
- Redacta un email breve, claro y profesional.
- Usa tono cordial pero directo.
- Incluye saludo, cuerpo y cierre con firma.

# Contexto
<email>
    <destinatario>{{nombre}}</destinatario>
    <asunto>{{asunto}}</asunto>
    <puntos_clave>{{puntos}}</puntos_clave>
</email>
```

Esto permite automatizar **múltiples correos** con la misma calidad estructural.

- destinatario: profesor miller

- asunto: correción de notas

- puntos clave: entrega de la tarea 1, entrega de la tarea 2

Resultado:

**Asunto:** Solicitud de revisión de notas – Tareas 1 y 2

Estimado Profesor Miller,

Espero se encuentre muy bien. Le escribo para solicitar amablemente la revisión de las calificaciones correspondientes a la **Tarea 1** y la **Tarea 2**, ya que ambas fueron entregadas dentro del plazo establecido y me gustaría confirmar que se hayan tenido en cuenta correctamente.

Agradezco de antemano su tiempo y atención. Quedo atento a cualquier comentario o indicación adicional.

Cordialmente,

**[Tu Nombre]**

[Tu número de estudiante, si aplica]

[Tu programa o asignatura]


---

## Sección 3: Técnicas Avanzadas

### 3.1 Chain-of-Thought (CoT)

#### Ejercicio 3B: Problema Matemático

* **Prompt Directo:**

  ```
  ¿Cuál es la raíz cuadrada de 1764?
  ```

  Resultado:

  Calculemos paso a paso la raíz cuadrada de (1764):

1. Sabemos que $40^2 = 1600$ y $45^2 = 2025$, así que está entre 40 y 45.
2. Probemos $(42^2)$:
3. 
   $
   42 \times 42 = 1764
   $

✅ Por lo tanto,

$\sqrt{1764} = 42$


* **Prompt con CoT:**

  ```
  Calcula la raíz cuadrada de 1764. Piensa paso a paso, muestra tu razonamiento y luego la respuesta final.
  ```

Esto obliga al modelo a hacer la división en pasos (1764 ÷ 42 = 42), reduciendo errores.


  Resultado:

  Vamos a calcular la raíz cuadrada de \( 1764 \) paso a paso.

**1. Descomponer en factores primos**

Primero factorizamos $1764$:

- $1764$ es par:  $1764 \div 2 = 882$
- $882$ es par: $882 \div 2 = 441$
- $441$ no es par, probamos con $3: 4+4+1=9$ (múltiplo de 3) → $441 \div 3 = 147$
- $147$ es divisible por $3: 1+4+7=12$ → $147 \div 3 = 49$
- $49 = 7 \times 7$

Entonces:
$
1764 = 2 \times 2 \times 3 \times 3 \times 7 \times 7
$
$
1764 = 2^2 \times 3^2 \times 7^2
$


**2. Aplicar raíz cuadrada**

$
\sqrt{1764} = \sqrt{2^2 \times 3^2 \times 7^2}
$
$
\sqrt{1764} = 2 \times 3 \times 7
$
$
\sqrt{1764} = 42
$


**3. Verificación**


$42 \times 42 = (40+2)^2 = 1600 + 2 \times 40 \times 2 + 4 = 1600 + 160 + 4 = 1764$

Correcto.


**Respuesta final:**
$
\boxed{42}
$

---

#### Ejercicio 3C: Pregunta de Razonamiento

* **Directo:**

  ```
  María tiene el doble de edad que Juan. Juan tiene 12 años. ¿Qué edad tiene María?
  ```

  Resultado:

  Vamos paso a paso:

1. Sabemos que **Juan tiene 12 años**.
2. El problema dice: **María tiene el doble de edad que Juan**.
3. El doble de la edad de Juan es:  
$
2 \times 12 = 24
$
1. Por lo tanto, **María tiene 24 años**.

**Respuesta:** María tiene **24 años**.
* **Con CoT:**

  ```
  María tiene el doble de edad que Juan. Juan tiene 12 años. Razona paso a paso para calcular la edad de María y luego da la respuesta final.
  ```

  Resultado;

  Vamos a razonar paso a paso:

1. **Entender la relación de edades**:  
   El problema dice: *"María tiene el doble de edad que Juan"*.  
   Esto significa:  
   $
   \text{Edad de María} = 2 \times \text{Edad de Juan}
   $

2. **Identificar la edad de Juan**:  
   El problema dice: *"Juan tiene 12 años"*.  
   Es decir:  
   $
   \text{Edad de Juan} = 12
   $

3. **Sustituir en la relación**:  
   $
   \text{Edad de María} = 2 \times 12
   $

4. **Calcular**:  
   $
   \text{Edad de María} = 24
   $

**Respuesta final**: María tiene **24 años**.

---

### 3.2 ReAct

#### Ejercicio 4B: Simulación de búsqueda encadenada

**Pregunta:** “¿Cuál es la capital de Australia y en qué continente está?”

Prompt con ReAct:

```text
Thought: Necesito identificar la capital de Australia.  
Action: Search("capital de Australia")  
Observation: Canberra es la capital.  

Thought: Ahora debo identificar en qué continente está.  
Action: Search("Australia continente")  
Observation: Australia está en Oceanía.  

Final Answer: La capital de Australia es Canberra y el país se encuentra en Oceanía.
```

Resultado:

✅ Correcto.
La **capital de Australia es Canberra** y **se ubica en el continente de Oceanía**.


---

### 3.3 Self-Consistency

#### Ejercicio 5B: Pregunta Trampa de Probabilidad

“Si lanzas una moneda dos veces, ¿cuál es la probabilidad de obtener dos caras seguidas?”

* **Prompt:**

  ```
  Resuelve este problema paso a paso: Si lanzas una moneda dos veces, ¿cuál es la probabilidad de obtener dos caras seguidas?
  ```

Pide 3 cadenas de razonamiento independientes y compara:

* Algunos modelos dirán 1/2, otros 1/4.
* Con autoconsistencia, la mayoría coincidirá en 1/4 (correcto).

Resultado:

**Método 1 — Enumeración del espacio muestral**

Resultados posibles al lanzar la moneda dos veces (igualmente probables):

* Cara, Cara (CC)
* Cara, Sello (CS)
* Sello, Cara (SC)
* Sello, Sello (SS)
  Solo **CC** cumple “dos caras seguidas”. Favorables = 1, totales = 4 → probabilidad = $1/4 = 0{,}25 = 25\% $.

**Método 2 — Regla del producto (independencia)**

Las dos tiradas son independientes.
$P(\text{cara en 1ª})=\tfrac{1}{2}.
P(\text{cara en 2ª})=\tfrac{1}{2}.$
Entonces $P(\text{CC}=\tfrac{1}{2}\times\tfrac{1}{2}=\tfrac{1}{4}=25\%).$

**Método 3 — Conteo combinatorio / complemento**

Número total de secuencias de 2 lanzamientos = $2^2=4$. Número de secuencias con exactamente 2 caras = $\binom{2}{2}=1$. Probabilidad = $1/4$.
(Otra vista: la probabilidad de **no** obtener CC es $3/4$; por complemento $1-3/4=1/4$.)

**Comparación y por qué algunos dicen 1/2 (error común)**

La respuesta $1/2$ aparece cuando se interpreta **condicionalmente**: si **ya sabes** que la primera tirada fue cara, entonces la probabilidad de que la segunda también sea cara es $1/2$. Eso es $P(\text{2ª cara}\mid\text{1ª cara})=1/2$. Pero la pregunta original es **no condicionada** (antes de lanzar ambas), por lo que la probabilidad conjunta es $1/4$.

**Respuesta final:** $\boxed{\tfrac{1}{4}=25\%}$.


---

### 3.4 Tree-of-Thought (ToT)

#### Ejercicio 6B: Planificación de Viaje

Prompt ToT:

```
Quiero que explores 3 posibles planes de viaje a Europa con presupuesto limitado.  

Paso 1: Genera 3 opciones (países distintos).  
Paso 2: Evalúa cada opción en costo, cultura y accesibilidad.  
Paso 3: Elige la mejor y explica por qué.  
```

Esto obliga al modelo a **comparar alternativas** y no dar una única respuesta superficial.

Resultado:

¡Excelente! Vamos a crear tres planes de viaje a Europa que sean económicos pero increíbles. Aquí tienes el análisis paso a paso.

**Paso 1: Genera 3 opciones (países distintos)**

1.  **Opción A: La Ruta Balcánica (Serbia, Bosnia y Herzegovina, Montenegro)**
2.  **Opción B: El Este Clásico (Polonia y República Checa)**
3.  **Opción C: El Sur Ibérico (Portugal y Sur de España)**

**Paso 2: Evalúa cada opción en costo, cultura y accesibilidad**

**Opción A: La Ruta Balcánica**
*   **Costo (5/5 - Excelente):** Es la opción más barata. Puedes encontrar alojamiento en hostales por 10-15€ la noche, comidas completas por 5-8€ y el transporte entre ciudades (en autobús) es muy económico. Una cerveza rara vez supera los 2€.
*   **Cultura (5/5 - Excelente):** Ofrece una experiencia cultural intensa y auténtica. Verás la mezcla de imperios (Otomano y Austrohúngaro) en la arquitectura, probarás una gastronomía única y llena de sabores (ćevapi, burek) y conocerás historias recientes y antiguas que son profundamente conmovedoras. Es menos turística, lo que se agradece.
*   **Accesibilidad (3/5 - Regular):** El principal punto de entrada es Belgrado (Serbia) o Dubrovnik (Croacia, que es más cara). Los vuelos desde América pueden ser un poco más caros y con escalas. Una vez allí, el transporte entre países es eficiente pero en autobús, y los idiomas utilizan alfabetos diferentes (cirílico/latino), lo que puede ser una pequeña barrera.

**Resumen:** Ideal para el viajero aventurero que prioriza el bajo costo y una experiencia cultural profunda por encima de la comodidad logística.

**Opción B: El Este Clásico (Polonia y República Checa)**
*   **Costo (4/5 - Muy Bueno):** Polonia es excepcionalmente asequible, especialmente ciudades como Cracovia. La República Checa es un poco más cara (sobre todo Praga), pero sigue siendo muy razonable comparada con Europa Occidental. Los hostales son baratos, la comida de pub es económica y la cerveza es más barata que el agua en muchos lugares.
*   **Cultura (4/5 - Muy Buena):** Tienes una dosis enorme de historia europea. Desde los castillos de cuento de Praga y la impresionante Cracovia, hasta la sobrecogedora historia de Auschwitz y el barrio judío. La cultura del café y la cerveza es vibrante. Es un equilibrio perfecto entre lo turístico y lo auténtico.
*   **Accesibilidad (5/5 - Excelente):** Tanto Varsovia como Cracovia en Polonia, y Praga en República Checa, tienen aeropuertos internacionales con muchas conexiones de bajo coste (ej. Ryanair, Wizz Air). El transporte entre ciudades es excelente (trenes y autobuses modernos). El inglés está muy extendido entre la gente joven.

**Resumen:** La opción más equilibrada. Ofrece una gran dosis de historia, belleza y cultura a un precio excelente, con una logística muy sencilla.

**Opción C: El Sur Ibérico (Portugal y Sur de España)**
*   **Costo (3/5 - Bueno):** Es la opción más cara de las tres, pero sigue siendo asequible si se compara con destinos como París o Londres. Lisboa y Sevilla han subido de precio, pero con planificación se pueden encontrar gangas. El truco está en aprovechar los "menús del día" y el transporte público. El Algarve portugués o Cádiz en España pueden ser más baratos.
*   **Cultura (5/5 - Excelente):** Es difícil superar la riqueza cultural de esta región. El flamenco, el fado, la arquitectura morisca, los tapetes y azulejos, y una de las gastronomías más celebradas del mundo (tapas, pescado fresco, vinos). La vida en la calle y el ambiente son vibrantes.
*   **Accesibilidad (5/5 - Excelente):** Lisboa, Oporto, Sevilla y Málaga tienen aeropuertos con numerosos vuelos baratos desde toda Europa. La conexión en tren o autobús entre Portugal y España es directa y frecuente. No hay barrera idiomática para hispanohablantes en España, y en Portugal es muy manejable.

**Resumen:** Perfecto para quienes buscan sol, una cultura vibrante y una gastronomía de primer nivel, con una logística impecable, estando dispuestos a gastar un poco más.


**Paso 3: Elige la mejor y explica por qué**

**La Mejor Opción: Opción B - El Este Clásico (Polonia y República Checa)**

**Explicación:**

Si el objetivo es maximizar la relación **calidad-precio-accesibilidad** con un presupuesto limitado, la ruta de Polonia y República Checa es la ganadora indiscutible.

1.  **Costo Imbatible para lo que Ofrece:** Si bien los Balcanes son más baratos, la diferencia de precio con Polonia y República Checa no es abismal, y a cambio obtienes una infraestructura turística y de transporte mucho más desarrollada. Te permite vivir una experiencia de "Europa de postal" (castillos, plazas medievales) sin el precio de Europa Occidental.

2.  **Accesibilidad y Facilidad:** Es la opción más fácil de ejecutar. Los vuelos son directos y baratos desde muchas capitales, el transporte terrestre es excelente y no existen las barreras lingüísticas significativas para un viajero. Esto reduce el estrés y el tiempo de planificación, algo valioso en un viaje corto.

3.  **Equilibrio Cultural Perfecto:** Ofrece una profundidad histórica y cultural tremenda (desde la Segunda Guerra Mundial y el Holocausto hasta la era comunista) combinada con una escena moderna y juvenil vibrante. Puedes pasar la mañana en un campo de concentración y la noche en un bar subterráneo escuchando jazz. Satisface tanto al viajero que busca historia como al que busca diversión y vida social.

**En conclusión,** mientras que los Balcanes son para una aventura más "fuera de lo común" y la Península Ibérica para un viaje más "clásico" y gastronómico, **la ruta de Polonia y República Checa es el punto óptimo.** Ofrece la esencia de un viaje europeo memorable (historia, arquitectura, cultura) con la mejor relación costo-beneficio y la menor complicación logística, haciendo que cada euro y cada día del viaje rindan al máximo.

---

### 3.5 JSON Enforced Output & Guardrails

#### Ejercicio 7B: Extracción de Contactos

Texto de entrada:
“Juan Pérez vive en Bogotá, Colombia. Su correo es [juanperez@mail.com](mailto:juanperez@mail.com) y su teléfono es +57 300 123 4567.”

Prompt:

```
Extrae la información y responde solo con un JSON válido en esta estructura:  

{
  "nombre": "string",
  "ciudad": "string",
  "pais": "string",
  "email": "string",
  "telefono": "string"
}
```

Esto asegura que la salida sea **estructurada y usable por un sistema**.

Resultado:

```json
{
  "nombre": "Juan Pérez",
  "ciudad": "Bogotá",
  "pais": "Colombia",
  "email": "juanperez@mail.com",
  "telefono": "+57 300 123 4567"
}
```

---



