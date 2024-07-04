ChatGPT 4o

# Prompts
## PROMPT 1
Actúa como un Product Manager y Business Analyst.

Usando este documento (https://github.com/cubelos/AI4Devs-design/blob/main/LTI-JCO/LTI-JCO.md) como PRD, crea las historias de usuario de usuario principales para tener un MVP teniendo en cuenta los distintos roles y necesidades.

Usa la siguiente plantilla para las historias de usuario:

"""
Título:
Como [rol del usuario], quiero [acción que desea realizar el usuario], para que [beneficio que espera obtener el usuario].

Descripción:
[Una descripción concisa y en lenguaje natural de la funcionalidad que el usuario desea]

Criterios de Aceptación:
[Condiciones específicas que deben cumplirse para considerar la User Story como "terminada", éstos deberian de seguir un formato similar a “Dado que” [contexto inicial], "cuando” [acción realizada], “entonces” [resultado esperado].
- [Detalle específico de funcionalidad]
- [Detalle específico de funcionalidad]
- [Detalle específico de funcionalidad]
]

Notas Adicionales:
- [Cualquier consideración adicional que pueda ayudar a desarrollar la historia]

Historias de Usuario Relacionadas:
- [Relaciones con otras historias de usuario indicando cual bloquea a cual]
"""

## PROMPT 2
Identifica qué método de priorización sería el óptimo para las historias de usuario

### Respuesta
### Método de Prioritización Óptimo para LTI-JCO

Basado en la información del PRD y las necesidades del proyecto, el método **MoSCoW (Must have, Should have, Could have, Won't have)** es óptimo para priorizar las historias de usuario. Este método permite clasificar funcionalidades críticas y opcionales, asegurando un enfoque claro para el desarrollo del MVP.

### Aplicación del Método MoSCoW:

1. **Must Have:**
   - Clasificación Automática de Candidatos
   - Portal de Candidatos

2. **Should Have:**
   - Programación Automática de Entrevistas

3. **Could Have:**
   - Colaboración en Tiempo Real

4. **Won't Have:**
   - Funcionalidades adicionales no críticas para el MVP

### Razones para elegir MoSCoW:
- **Claridad:** Facilita la comunicación y la comprensión entre el equipo y los stakeholders.
- **Enfoque:** Permite centrarse en entregar valor inmediato con las funcionalidades más críticas.
- **Flexibilidad:** Acomoda cambios y ajustes durante el desarrollo sin comprometer los elementos esenciales del proyecto.

## PROMPT 3
Aplícala en las historias de usuario para priorizarlas creando un backlog.

## PROMPT 4
Estima por cada item en el backlog (genera una tabla markdown):
- Impacto en el usuario y valor del negocio.
- Urgencia basada en tendencias del mercado y feedback de usuarios.
- Complejidad y esfuerzo estimado de implementación.
- Riesgos y dependencias entre tareas.
Rellena sólo con los siguientes valores: alta, media, baja.

## PROMPT 5
Actúa ahora como un líder técnico. Crea los tickets de trabajo para la historia de usuario más prioritaria. Añade a cada ticket
- tipo: feature, tarea técnica, bug...
- título
- descripción
- criterios de aceptación:  lista detallada de condiciones que deben cumplirse para que el trabajo en el ticket se considere completado.
- estrategia de implementación: descripción de cómo implementarlo técnicamente, incluyendo las tecnologías a usar
- estimación: estimación del esfuerzo en puntos de historia con fibonacci
- prioridad: clasificación de la importancia y la urgencia de la tarea
- testing plan: pasos o pruebas específicas que se deben realizar para verificar que la tarea se ha completado correctamente
- bloqueos: bloqueos a o con otras tareas


