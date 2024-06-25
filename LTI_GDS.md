# Prompt en GPT4o #
" Vamos a diseñar y documentar un sistema de software siguiendo las fases de investigación y análisis, casos de uso, modelado de datos, y diseño de alto nivel.
LTI es una startup que quiere desarrollar el ATS (Applicant-Tracking System) del futuro. (imagen adjunta del modelo y estructura a seguir)
Serás el product manager y tienes que definir esas funcionalidades clave que harán brillar a LTI por encima de los competidores,  aumentar la eficiencia para los departamentos de HR, mejorar la colaboración en tiempo real entre reclutadores y managers, automatizaciones, asistencia de IA en diversas tareas.
Tu misión es diseñar la primera versión del sistema, entregando los siguientes artefactos:
1- Descripción breve del software LTI, valor añadido y ventajas competitivas. 
2- Explicación de las funciones principales. 
3- Añadir un diagrama Lean Canvas para entender el modelo de negocio.
4- Descripción de los 3 casos de uso principales, con el diagrama asociado a cada uno.
5- Modelo de datos que cubra entidades, atributos (nombre y tipo) y relaciones.
6- Diseño del sistema a alto nivel, tanto explicado como diagrama adjunto.
7- Diagrama C4 que llegue en profundidad a uno de los componentes del sistema, el que prefieras.
Por ultimo y muy importante: Documenta todo en un único documento markdown (.md) con el nombre LTI_GDS "


# LTI Applicant-Tracking System (ATS)

## 1. Descripción breve del software LTI, valor añadido y ventajas competitivas
LTI Applicant-Tracking System (ATS) es una solución integral diseñada para modernizar y optimizar el proceso de reclutamiento. Este sistema permite a los departamentos de recursos humanos gestionar de manera eficiente todas las fases del ciclo de contratación, desde la creación de ofertas de empleo hasta la contratación de candidatos.

**Valor añadido y ventajas competitivas:**
- Automatización de tareas repetitivas como la programación de entrevistas y el filtrado de candidatos, lo que reduce el tiempo y esfuerzo manual.
- Utilización de inteligencia artificial para el análisis de currículums, evaluación de candidatos y recomendaciones basadas en datos.
- Herramientas colaborativas que permiten a reclutadores y managers trabajar juntos de manera eficiente y en tiempo real.
- Potentes capacidades analíticas que proporcionan insights sobre el proceso de contratación, permitiendo decisiones basadas en datos.
- Interfaz intuitiva y fácil de usar, diseñada pensando en mejorar la experiencia del usuario tanto para los reclutadores como para los candidatos.

## 2. Explicación de las funciones principales

1. **Gestión de ofertas de empleo:**
   - Creación y publicación de ofertas en múltiples plataformas (tableros de empleo, redes sociales, sitio web corporativo).
   - Plantillas personalizables para la creación rápida de nuevas ofertas.

2. **Recepción y análisis de solicitudes:**
   - Recepción de aplicaciones de candidatos desde múltiples fuentes.
   - Filtrado y categorización automática de aplicaciones utilizando IA.

3. **Evaluación y selección de candidatos:**
   - Herramientas para la evaluación de currículums y preselección de candidatos.
   - Pruebas en línea y evaluaciones personalizadas para cada oferta de trabajo.

4. **Programación y gestión de entrevistas:**
   - Programación automática de entrevistas basadas en la disponibilidad de los reclutadores y candidatos.
   - Recordatorios automáticos y seguimiento de las etapas del proceso de entrevista.

5. **Colaboración y comunicación:**
   - Plataformas colaborativas para la evaluación conjunta de candidatos.
   - Chats y videollamadas integradas para la comunicación en tiempo real.

6. **Análisis y reportes:**
   - Paneles de control y reportes detallados sobre el rendimiento del proceso de contratación.
   - Métricas clave como tiempo de contratación, tasa de aceptación de ofertas, y más.

## 3. Lean Canvas

## Lean Canvas
| Problem                                | Solution                              |
|----------------------------------------|---------------------------------------|
| 1. Tareas manuales repetitivas         | 1. Automatización del flujo de trabajo|
| 2. Falta de colaboración en tiempo real| 2. Herramientas colaborativas en tiempo real|
| 3. Análisis de datos ineficiente       | 3. Análisis y reportes avanzados con IA|

| Key Metrics                            | Unique Value Proposition              |
|----------------------------------------|---------------------------------------|
| 1. Tiempo de contratación reducido     | 1. Integración de IA y automatización |
| 2. Tasa de aceptación de ofertas       | 2. Herramientas colaborativas y comunicación en tiempo real|
| 3. Satisfacción del usuario            | 3. Experiencia de usuario optimizada  |

| Channels                               | Cost Structure                        |
|----------------------------------------|---------------------------------------|
| 1. Ventas directas                     | 1. Desarrollo de software             |
| 2. Marketing digital                   | 2. Infraestructura y soporte técnico  |
| 3. Asociaciones estratégicas           | 3. Marketing y ventas                 |

| Customer Segments                      | Revenue Streams                       |
|----------------------------------------|---------------------------------------|
| 1. Grandes empresas                    | 1. Suscripción mensual/anual          |
| 2. PYMES                               | 2. Pago por uso                       |
| 3. Agencias de reclutamiento           | 3. Servicios premium                  |

## 4. Casos de uso principales

### Caso de uso 1: Publicación de ofertas de empleo

**Descripción:**
Un reclutador crea y publica una oferta de empleo en múltiples plataformas desde el sistema.

**Diagrama de Caso de Uso:**
![image](https://github.com/LIDR-academy/AI4Devs-design/assets/45273946/5123149a-2597-4fb5-990c-80ac0102b0c4)

### Caso de uso 2: Evaluación de candidatos

**Descripción:**
El sistema evalúa automáticamente los currículums recibidos y preselecciona a los mejores candidatos.

**Diagrama de Caso de Uso:**
![image](https://github.com/LIDR-academy/AI4Devs-design/assets/45273946/da103918-8aae-4d00-87d1-332403b423c6)

### Caso de uso 3: Programación de entrevistas

**Descripción:**
El sistema programa entrevistas basadas en la disponibilidad de los candidatos y reclutadores.

**Diagrama de Caso de Uso:**

![image](https://github.com/LIDR-academy/AI4Devs-design/assets/45273946/26271b1a-35fc-4b0a-b576-dc34a78d7f0b)


## 5. Modelo de datos

### Entidades y Atributos

#### 1. Candidato
- ID (int, primary key)
- Nombre (varchar)
- Email (varchar)
- Teléfono (varchar)
- Currículum (blob)
- Estado (varchar)

#### 2. Oferta de Empleo
- ID (int, primary key)
- Título (varchar)
- Descripción (text)
- Fecha de creación (datetime)
- Estado (varchar)

#### 3. Aplicación
- ID (int, primary key)
- CandidatoID (int, foreign key)
- OfertaID (int, foreign key)
- Fecha de aplicación (datetime)
- Estado (varchar)

#### 4. Entrevista
- ID (int, primary key)
- CandidatoID (int, foreign key)
- ReclutadorID (int, foreign key)
- Fecha y Hora (datetime)
- Estado (varchar)

#### 5. Reclutador
- ID (int, primary key)
- Nombre (varchar)
- Email (varchar)
- Teléfono (varchar)

## 6. Diseño del sistema a alto nivel

**Descripción:**
El sistema ATS de LTI se compone de varios módulos clave que interactúan entre sí para gestionar todo el ciclo de vida de la contratación. Estos módulos incluyen:

1. **Módulo de Gestión de Ofertas:**
   - Permite crear y publicar ofertas de empleo.
   - Integra con plataformas externas para la publicación.

2. **Módulo de Recepción y Evaluación de Candidatos:**
   - Gestiona la recepción de aplicaciones.
   - Utiliza IA para el filtrado y evaluación de currículums.

3. **Módulo de Programación de Entrevistas:**
   - Automatiza la programación de entrevistas.
   - Envía recordatorios y gestiona la disponibilidad.

4. **Módulo de Análisis y Reportes:**
   - Genera reportes y análisis sobre el proceso de contratación.

**Diagrama de arquitectura de alto nivel:**

![image](https://github.com/LIDR-academy/AI4Devs-design/assets/45273946/f30c3e6a-9f5f-429e-9b77-2c876742b1b5)


## 7. Diagrama C4 para el Módulo de Recepción y Evaluación de Candidatos

**Contexto:**

![image](https://github.com/LIDR-academy/AI4Devs-design/assets/45273946/e47f6b0d-d4de-4db7-9f92-0d585474d212)

**Contenedor:**

![image](https://github.com/LIDR-academy/AI4Devs-design/assets/45273946/57b780a1-877a-4d4e-aaf9-1e8fd3914d11)


**Componente:**

![image](https://github.com/LIDR-academy/AI4Devs-design/assets/45273946/61174ffc-a901-4ea4-9bcd-98c0c5be0fd1)

He generado el documento markdown con el nombre LTI_GDS.md. Puedes descargarlo aquí. ​
