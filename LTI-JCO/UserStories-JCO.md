# LTI-JCO
### Historias de Usuario para el MVP de LTI-JCO

#### 1. Clasificación Automática de Candidatos
**Título:** Clasificación Automática de Candidatos
Como reclutador, quiero que el sistema clasifique automáticamente los currículums, para que pueda identificar rápidamente a los candidatos más adecuados.

**Descripción:** El sistema utilizará IA para analizar y clasificar los currículums cargados, destacando los perfiles más alineados con los requisitos del puesto.

**Criterios de Aceptación:**
- Dado que he cargado varios currículums, cuando el sistema los procese, entonces debería ver una lista clasificada de candidatos.
- Dado que defino criterios personalizados, cuando los aplico, entonces el sistema debe filtrar los candidatos según esos criterios.
- Dado que el sistema clasifica un currículum, cuando reviso la clasificación, entonces debería poder ver las razones de la clasificación.

**Notas Adicionales:**
- Considerar variaciones en formatos de currículum y lenguajes.

**Historias de Usuario Relacionadas:**
- Programación Automática de Entrevistas (bloqueada por esta historia)

#### 2. Programación Automática de Entrevistas
**Título:** Programación Automática de Entrevistas
Como reclutador, quiero que el sistema programe entrevistas automáticamente, para ahorrar tiempo y reducir la posibilidad de conflictos de agenda.

**Descripción:** El sistema sincroniza los calendarios de entrevistadores y candidatos, programando automáticamente las entrevistas y enviando recordatorios.

**Criterios de Aceptación:**
- Dado que he seleccionado candidatos para entrevistas, cuando el sistema programa las entrevistas, entonces debería verlas en mi calendario sincronizado.
- Dado que el sistema programa una entrevista, cuando se acerca la fecha, entonces debe enviar recordatorios automáticos a todos los participantes.
- Dado que el sistema detecta conflictos de agenda, cuando intenta programar una entrevista, entonces debe sugerir nuevas fechas disponibles.

**Notas Adicionales:**
- Integración con principales calendarios como Google Calendar y Outlook.

**Historias de Usuario Relacionadas:**
- Clasificación Automática de Candidatos (bloquea esta historia)
- Colaboración en Tiempo Real (bloqueada por esta historia)

#### 3. Colaboración en Tiempo Real
**Título:** Colaboración en Tiempo Real
Como manager, quiero colaborar en tiempo real con los reclutadores durante el proceso de entrevistas, para tomar decisiones informadas de manera rápida y eficiente.

**Descripción:** La plataforma permite dejar comentarios y evaluaciones en tiempo real sobre los candidatos, y ofrece un tablero centralizado para tomar decisiones.

**Criterios de Aceptación:**
- Dado que estoy en una entrevista, cuando dejo un comentario, entonces el reclutador debe verlo en tiempo real.
- Dado que varios evaluadores han dejado sus comentarios, cuando reviso el tablero centralizado, entonces debería ver un resumen consolidado de todas las evaluaciones.
- Dado que el equipo necesita tomar una decisión, cuando usamos las herramientas de votación, entonces el sistema debe mostrar el resultado en tiempo real.

**Notas Adicionales:**
- Notificaciones en tiempo real para nuevos comentarios o decisiones.

**Historias de Usuario Relacionadas:**
- Programación Automática de Entrevistas (bloquea esta historia)

#### 4. Portal de Candidatos
**Título:** Portal de Candidatos
Como candidato, quiero un portal fácil de usar para aplicar a trabajos y seguir el estado de mis solicitudes, para tener una experiencia de aplicación transparente y eficiente.

**Descripción:** El portal permite a los candidatos aplicar fácilmente a los puestos y hacer seguimiento del estado de sus aplicaciones en tiempo real.

**Criterios de Aceptación:**
- Dado que estoy aplicando a un puesto, cuando completo mi aplicación, entonces debería recibir una confirmación de que mi aplicación fue enviada.
- Dado que quiero verificar el estado de mi aplicación, cuando inicio sesión en el portal, entonces debería ver el estado actualizado de todas mis aplicaciones.
- Dado que mi aplicación cambia de estado, cuando esto ocurre, entonces debería recibir una notificación al respecto.

**Notas Adicionales:**
- Interfaz amigable y accesible desde dispositivos móviles.

**Historias de Usuario Relacionadas:**
- Clasificación Automática de Candidatos (bloqueada por esta historia)

### Backlog Prioritizado para LTI-JCO

#### Must Have:
1. **Clasificación Automática de Candidatos**
   - **Título:** Clasificación Automática de Candidatos
   - **Descripción:** El sistema analiza y clasifica currículums cargados, destacando perfiles alineados con los requisitos del puesto.
   - **Criterios de Aceptación:**
     - Clasificación automática de currículums.
     - Filtrado basado en criterios personalizados.
     - Visualización de razones de clasificación.

2. **Portal de Candidatos**
   - **Título:** Portal de Candidatos
   - **Descripción:** El portal permite a los candidatos aplicar a trabajos y seguir el estado de sus solicitudes en tiempo real.
   - **Criterios de Aceptación:**
     - Confirmación de aplicación enviada.
     - Visualización del estado actualizado de aplicaciones.
     - Notificaciones de cambios en el estado de la aplicación.

#### Should Have:
3. **Programación Automática de Entrevistas**
   - **Título:** Programación Automática de Entrevistas
   - **Descripción:** El sistema sincroniza calendarios para programar entrevistas automáticamente y envía recordatorios.
   - **Criterios de Aceptación:**
     - Programación de entrevistas en calendario sincronizado.
     - Recordatorios automáticos de entrevistas.
     - Sugerencias de nuevas fechas ante conflictos de agenda.

#### Could Have:
4. **Colaboración en Tiempo Real**
   - **Título:** Colaboración en Tiempo Real
   - **Descripción:** Permite dejar comentarios y evaluaciones en tiempo real sobre los candidatos, con un tablero centralizado para decisiones.
   - **Criterios de Aceptación:**
     - Comentarios visibles en tiempo real.
     - Resumen consolidado de evaluaciones.
     - Resultados de votaciones en tiempo real.

### Estimación del Backlog

| Historia de Usuario                    | Impacto en el Usuario y Valor del Negocio | Urgencia basada en Tendencias del Mercado y Feedback de Usuarios | Complejidad y Esfuerzo Estimado de Implementación | Riesgos y Dependencias Entre Tareas |
|----------------------------------------|-------------------------------------------|-------------------------------------------------------------------|---------------------------------------------------|-------------------------------------|
| Clasificación Automática de Candidatos | Alta                                      | Alta                                                              | Alta                                              | Media (bloquea Programación Automática de Entrevistas) |
| Portal de Candidatos                   | Alta                                      | Alta                                                              | Media                                             | Baja  |
| Programación Automática de Entrevistas | Media                                     | Media                                                             | Media                                             | Alta (bloqueada por Clasificación Automática de Candidatos) |
| Colaboración en Tiempo Real            | Media                                     | Baja                                                              | Alta                                              | Alta (bloqueada por Programación Automática de Entrevistas) |

### Clasificación Automática de Candidatos: Tickets de Trabajo

#### Ticket 1: Implementación del Algoritmo de Clasificación
- **Tipo:** Feature
- **Título:** Implementación del Algoritmo de Clasificación
- **Descripción:** Desarrollar y entrenar un algoritmo de IA para analizar y clasificar currículums según los criterios definidos.
- **Criterios de Aceptación:**
  - El algoritmo debe clasificar los currículums con una precisión mínima del 80%.
  - Los resultados deben ser visualizables en la interfaz del reclutador.
  - Los criterios de clasificación deben ser personalizables.
- **Estrategia de Implementación:**
  - Utilizar Python y bibliotecas como Scikit-Learn o TensorFlow.
  - Entrenar el algoritmo con un conjunto de datos representativo de currículums.
  - Integrar el modelo entrenado con la base de datos y la interfaz de usuario.
- **Estimación:** 8 puntos
- **Prioridad:** Alta
- **Testing Plan:**
  - Validar el modelo con un conjunto de datos de prueba.
  - Realizar pruebas de integración para asegurar la correcta visualización de resultados.
  - Obtener feedback de usuarios de prueba.
- **Bloqueos:** Ninguno

#### Ticket 2: Interfaz de Usuario para la Visualización de Clasificación
- **Tipo:** Feature
- **Título:** Interfaz de Usuario para la Visualización de Clasificación
- **Descripción:** Crear la interfaz donde los reclutadores puedan ver la lista clasificada de candidatos y los detalles de la clasificación.
- **Criterios de Aceptación:**
  - La interfaz debe mostrar la lista de candidatos clasificados.
  - Debe permitir a los usuarios ver las razones detrás de cada clasificación.
  - Debe ser posible filtrar y ordenar la lista según diferentes criterios.
- **Estrategia de Implementación:**
  - Utilizar tecnologías frontend como React o Angular.
  - Conectar la interfaz con el backend para obtener los datos del algoritmo de clasificación.
  - Diseñar una interfaz amigable y fácil de usar.
- **Estimación:** 5 puntos
- **Prioridad:** Alta
- **Testing Plan:**
  - Realizar pruebas de usabilidad con usuarios finales.
  - Verificar la correcta visualización y funcionamiento de filtros y ordenamientos.
  - Asegurar la sincronización con el backend.
- **Bloqueos:** Ninguno

#### Ticket 3: Integración de Criterios Personalizables
- **Tipo:** Feature
- **Título:** Integración de Criterios Personalizables
- **Descripción:** Permitir a los reclutadores definir y ajustar los criterios de clasificación según las necesidades del puesto.
- **Criterios de Aceptación:**
  - Los usuarios deben poder definir criterios personalizados desde la interfaz.
  - El sistema debe aplicar estos criterios en la clasificación.
  - Los cambios en los criterios deben reflejarse en tiempo real.
- **Estrategia de Implementación:**
  - Añadir opciones en la interfaz de usuario para definir criterios.
  - Ajustar el algoritmo de clasificación para aceptar criterios personalizados.
  - Asegurar la persistencia de estos criterios en la base de datos.
- **Estimación:** 3 puntos
- **Prioridad:** Media
- **Testing Plan:**
  - Verificar la correcta definición y almacenamiento de criterios personalizados.
  - Asegurar que los cambios se reflejen en las clasificaciones.
  - Realizar pruebas de rendimiento para evaluar el impacto.
- **Bloqueos:** Depende de la Interfaz de Usuario para la Visualización de Clasificación

#### Ticket 4: Documentación y Capacitación
- **Tipo:** Tarea Técnica
- **Título:** Documentación y Capacitación
- **Descripción:** Crear documentación detallada del sistema de clasificación y capacitar a los usuarios finales en su uso.
- **Criterios de Aceptación:**
  - La documentación debe ser clara y accesible.
  - Los usuarios deben recibir capacitación sobre cómo usar las nuevas funcionalidades.
- **Estrategia de Implementación:**
  - Redactar documentación técnica y de usuario.
  - Organizar sesiones de capacitación y crear tutoriales.
  - Obtener feedback de los usuarios y ajustar la documentación según sea necesario.
- **Estimación:** 2 puntos
- **Prioridad:** Media
- **Testing Plan:**
  - Revisar la documentación con un grupo de usuarios.
  - Evaluar la efectividad de la capacitación a través de encuestas.
- **Bloqueos:** Ninguno