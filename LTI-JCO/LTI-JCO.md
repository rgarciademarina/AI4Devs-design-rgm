# LTI-JCO

- [Descripción breve del software LTI](#descripción-breve-del-software-lti)
- [Valor añadido y ventajas competitivas](#valor-añadido-y-ventajas-competitivas)
- [Funciones principales](#funciones-principales)
- [Diagrama Lean Canvas](#diagrama-lean-canvas)
- [Casos de Uso Principales del ATS de LTI](#casos-de-uso-principales-del-ats-de-lti)
  - [Caso de Uso 1: Automatización del Filtrado de Candidatos](#caso-de-uso-1-automatización-del-filtrado-de-candidatos)
  - [Caso de Uso 2: Programación Automática de Entrevistas](#caso-de-uso-2-programación-automática-de-entrevistas)
  - [Caso de Uso 3: Colaboración en Tiempo Real entre Reclutadores y Managers](#caso-de-uso-3-colaboración-en-tiempo-real-entre-reclutadores-y-managers)
- [Modelo de datos](#modelo-de-datos)
- [Diseño del Sistema a Alto Nivel](#diseño-del-sistema-a-alto-nivel)
  - [Componentes Principales](#componentes-principales)
- [Diagrama AWS](#diagrama-aws)
- [Diagrama C4](#diagrama-c4)

### Descripción breve del software LTI

LTI es un avanzado sistema de seguimiento de candidatos (ATS) diseñado para transformar y optimizar el proceso de contratación. Con un enfoque en la eficiencia, la colaboración en tiempo real y la automatización impulsada por inteligencia artificial, LTI permite a los departamentos de recursos humanos y a los reclutadores gestionar de manera efectiva el ciclo de vida completo de la contratación, desde la solicitud hasta la incorporación del nuevo empleado.

### Valor añadido y ventajas competitivas

- **Eficiencia mejorada:** LTI automatiza tareas repetitivas y administra grandes volúmenes de datos de candidatos, permitiendo a los equipos de recursos humanos centrarse en la toma de decisiones estratégicas.
- **Colaboración en tiempo real:** Integración fluida de comunicación y herramientas colaborativas para que los reclutadores y gerentes trabajen conjuntamente en tiempo real.
- **Asistencia de IA:** Utiliza inteligencia artificial para mejorar la preselección de candidatos, análisis de currículums, programación de entrevistas y generación de informes detallados.
- **Interfaz intuitiva:** Diseñada para ser fácil de usar, lo que reduce el tiempo de capacitación y mejora la adopción por parte del equipo.
- **Analíticas y reportes avanzados:** Ofrece insights y reportes detallados para ayudar a las empresas a mejorar continuamente sus procesos de contratación.

### Funciones principales

1. **Automatización del flujo de trabajo:** Automatización de tareas rutinarias como el envío de correos electrónicos, recordatorios de entrevistas y actualización de estados de los candidatos.
2. **Preselección y análisis de candidatos impulsados por IA:** Algoritmos de IA que filtran y analizan currículums, identificando los candidatos más adecuados basados en criterios personalizados.
3. **Portal de colaboración en tiempo real:** Herramientas integradas de chat y videoconferencia que permiten la colaboración sin interrupciones entre reclutadores y gerentes.
4. **Gestión centralizada de candidatos:** Base de datos unificada que almacena toda la información de los candidatos, incluyendo currículums, cartas de presentación, notas de entrevistas y más.
5. **Analíticas y reportes:** Dashboard interactivo con métricas clave y reportes personalizables para evaluar el rendimiento del proceso de contratación.
6. **Programación de entrevistas:** Herramientas de programación automatizadas que sincronizan calendarios y envían invitaciones a entrevistas.
7. **Integraciones con otras herramientas:** Integración con sistemas de gestión de recursos humanos (HRMS), plataformas de redes sociales y sitios de empleo para una gestión de candidatos sin fisuras.

### Diagrama Lean Canvas

![alt text](assets/lean-canvas.png)

### Casos de Uso Principales del ATS de LTI

#### Caso de Uso 1: Automatización del Filtrado de Candidatos

**Descripción**:
El ATS de LTI automatiza el proceso de filtrado inicial de candidatos, utilizando algoritmos de inteligencia artificial para evaluar currículums y perfiles, seleccionando los más adecuados según los requisitos del puesto.

**Diagrama Mermaid**:
```mermaid
graph TD
    A[Inicio] --> B[Recepción de Currículums]
    B --> C[Análisis con IA]
    C --> D{Cumple Requisitos}
    D --> |Sí| E[Enviar a Reclutador]
    D --> |No| F[Notificación de Rechazo]
    E --> G[Revisión por Reclutador]
    F --> H[Guardar en Base de Datos]
```

#### Caso de Uso 2: Programación Automática de Entrevistas

**Descripción**:
LTI permite la programación automática de entrevistas, sincronizando las agendas de los reclutadores y los candidatos, y enviando recordatorios para evitar ausencias y retrasos.

**Diagrama Mermaid**:
```mermaid
graph TD
    A[Inicio] --> B[Selección de Candidato]
    B --> C[Disponibilidad de Reclutador]
    C --> D[Disponibilidad de Candidato]
    D --> E[Programar Entrevista]
    E --> F[Enviar Invitaciones]
    F --> G[Confirmación de Candidato]
    G --> H[Recordatorio de Entrevista]
```

#### Caso de Uso 3: Colaboración en Tiempo Real entre Reclutadores y Managers

**Descripción**:
El sistema permite la colaboración en tiempo real entre los reclutadores y los managers a través de herramientas de comunicación integradas, facilitando la toma de decisiones rápidas y efectivas.

**Diagrama Mermaid**:
```mermaid
graph TD
    A[Inicio] --> B[Selección de Candidatos]
    B --> C[Herramienta de Comunicación]
    C --> D[Reclutadores y Managers Colaboran]
    D --> E[Comentarios y Feedback]
    E --> F[Decisión de Contratación]
    F --> G[Notificación al Candidato]
```

Estos casos de uso ilustran cómo LTI puede optimizar y facilitar los procesos de reclutamiento mediante la automatización, la programación eficiente y la colaboración en tiempo real.

### Modelo de datos

```mermaid
erDiagram
    CANDIDATE {
        int id PK
        string name
        string email
        string phone
        string resume_link
        string status
        date application_date
    }

    JOB {
        int id PK
        string title
        string description
        string location
        string department
        date posted_date
        string status
    }

    RECRUITER {
        int id PK
        string name
        string email
        string phone
        string department
    }

    INTERVIEW {
        int id PK
        date interview_date
        time interview_time
        string location
        int candidate_id FK
        int recruiter_id FK
    }

    FEEDBACK {
        int id PK
        int candidate_id FK
        int recruiter_id FK
        int job_id FK
        string comments
        date feedback_date
    }

    APPLICATION {
        int id PK
        int candidate_id FK
        int job_id FK
        string status
        date application_date
    }

    CANDIDATE ||--o{ APPLICATION : applies_to
    JOB ||--o{ APPLICATION : has
    RECRUITER ||--o{ INTERVIEW : conducts
    CANDIDATE ||--o{ INTERVIEW : attends
    CANDIDATE ||--o{ FEEDBACK : receives
    JOB ||--o{ FEEDBACK : about
    RECRUITER ||--o{ FEEDBACK : gives
```

**Relaciones**

- Un candidato puede tener múltiples aplicaciones (one-to-many).
- Un trabajo puede tener múltiples aplicaciones (one-to-many).
- Un reclutador puede conducir múltiples entrevistas (one-to-many).
- Un candidato puede asistir a múltiples entrevistas (one-to-many).
- Un candidato puede recibir múltiples comentarios de feedback (one-to-many).
- Un trabajo puede tener múltiples comentarios de feedback sobre candidatos (one-to-many).
- Un reclutador puede dar múltiples comentarios de feedback (one-to-many).

### Diseño del Sistema a Alto Nivel

El ATS de LTI será diseñado como una arquitectura basada en microservicios utilizando AWS (Amazon Web Services) para garantizar escalabilidad, alta disponibilidad y facilidad de mantenimiento. A continuación, se describen los componentes clave y el flujo general del sistema.

#### Componentes Principales

1. **Frontend**:
   - **React.js**: Aplicación web para la interfaz de usuario.
   - **AWS S3**: Almacenamiento de contenido estático (HTML, CSS, JS).

2. **Backend**:
   - **Microservicios**: Implementados en **Node.js** o **Python**, utilizando **AWS Lambda** para ejecutar código sin servidor.
   - **API Gateway**: **AWS API Gateway** para gestionar las solicitudes API y enrutarlas a los microservicios correspondientes.
   - **Autenticación**: **Amazon Cognito** para la gestión de usuarios y autenticación.

3. **Base de Datos**:
   - **Amazon RDS**: Base de datos relacional para almacenar datos estructurados.
   - **Amazon DynamoDB**: Base de datos NoSQL para datos no estructurados o semi-estructurados.

4. **Almacenamiento**:
   - **AWS S3**: Almacenamiento de currículums, documentos y otros archivos.

5. **Mensajería y Colas**:
   - **Amazon SQS**: Colas de mensajes para la gestión de tareas asíncronas.
   - **Amazon SNS**: Servicio de notificación para enviar mensajes y alertas.

6. **Analítica y Reporting**:
   - **AWS QuickSight**: Herramienta de análisis y visualización de datos.
   - **AWS Glue**: Servicio de preparación de datos para ETL (Extract, Transform, Load).

7. **Monitorización y Logging**:
   - **Amazon CloudWatch**: Monitorización del rendimiento y logging.
   - **AWS X-Ray**: Seguimiento de solicitudes para el análisis y depuración.

### Diagrama AWS

![alt text](assets/system-diagram.png)

### Diagrama C4
Vamos a enfocarnos en el componente de "API REST". Utilizaremos el modelo C4 para describir la arquitectura del sistema en cuatro niveles: contexto, contenedores, componentes y código.

![alt text](assets/C4-api-rest.png)

El diagrama generado proporciona una visión clara y estructurada de cómo se organiza y funciona el componente "API REST" dentro del sistema ATS de LTI.

1. **Usuarios**: Los usuarios (Reclutadores, Managers, Candidatos) interactúan con la **Aplicación Web** (representada como una función Lambda), que forma parte del frontend del sistema.

2. **API Gateway**: La aplicación web se comunica con el **API Gateway** que actúa como el punto de entrada para todas las solicitudes del frontend. El API Gateway enruta las solicitudes a los microservicios correspondientes.

3. **Autenticación**: El servicio de autenticación está gestionado por **Amazon Cognito**, que autentica a los usuarios antes de permitirles acceder a los demás servicios.

4. **Microservicios**:
   - **AuthController**: Gestiona la autenticación y autorización de usuarios.
   - **CandidateController**: Gestiona las operaciones relacionadas con los candidatos (creación, actualización, eliminación, etc.).
   - **JobController**: Gestiona las operaciones relacionadas con los trabajos (creación, actualización, eliminación, etc.).
   - **FilteringController**: Gestiona el proceso de filtrado de candidatos. Este servicio envía los currículums al **Servicio de IA** para su análisis y guarda los resultados en la base de datos.

5. **Base de Datos**: **Amazon RDS** se utiliza para almacenar datos estructurados relacionados con candidatos, trabajos y resultados de filtrado.

6. **Servicio de IA**: Implementado como una función Lambda, este servicio analiza los currículums de los candidatos y devuelve los resultados del filtrado al **FilteringController**.

7. **Almacenamiento**: **Amazon S3** se utiliza para almacenar currículums y otros documentos relacionados con los candidatos.

Este diagrama de alto nivel muestra cómo se comunican los diferentes componentes del sistema y cómo se gestionan las operaciones dentro del componente "API REST".