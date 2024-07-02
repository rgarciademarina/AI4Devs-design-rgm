# Sistema ATS (Applicant Tracking System)

*Disclaimer: Se han utilizado para proponer una solución a la práctica de LTI los ejemplos mezclados de diferentes estudiantes del curso AI4Devs.*

## Índice

* [Descripción Breve](#descripción-breve)
* [Valor Añadido y Ventajas Competitivas](#valor-añadido-y-ventajas-competitivas)
* [Funciones Principales](#funciones-principales)
* [Diagrama Lean Canvas](#diagrama-lean-canvas)
* [Casos de uso principales](#casos-de-uso-principales)
  * [Caso de Uso 1: Publicación de Vacantes](#caso-de-uso-1-publicación-de-vacantes)
  * [Caso de Uso 2: Proceso de Selección de Candidatos](#caso-de-uso-2-proceso-de-selección-de-candidatos)
  * [Caso de Uso 3: Integración con Herramientas de RRHH](#caso-de-uso-3-integración-con-herramientas-de-rrhh)
* [Modelo de datos](#modelo-de-datos)
* [Diseño del sistema de alto nivel](#diseño-del-sistema-a-alto-nivel)
* [Diagramas C4](#diagramas-c4)
  * [Diagrama de contexto - nivel 1](#diagrama-de-contexto---nivel-1)
  * [Diagrama de contenedores - nivel 2](#diagrama-de-contenedores---nivel-2)
  * [Diagrama de componentes - nivel 3](#diagrama-de-componentes---nivel-3)
  * [Diagrama de código - nivel 4](#diagrama-de-código---nivel-4)
* [Conclusiones](#conclusiones)

## Descripción Breve
LTI es un ATS (Applicant Tracking System) innovador diseñado para revolucionar el proceso de reclutamiento y contratación de personal en las empresas. Aprovecha las últimas tecnologías de automatización e inteligencia artificial para optimizar y agilizar todas las etapas, desde la publicación de vacantes hasta la selección final de candidatos.

## Valor Añadido y Ventajas Competitivas

1. **Aumento de la eficiencia para los departamentos de Recursos Humanos**: Automatiza tareas rutinarias y agiliza el flujo de trabajo, liberando tiempo valioso para que los reclutadores se enfoquen en actividades de mayor valor.
2. **Colaboración en tiempo real entre reclutadores y managers**: Promueve una comunicación fluida y transparente, permitiendo una toma de decisiones más informada y ágil.
3. **Asistencia de Inteligencia Artificial**: Aprovecha la IA para tareas como clasificación de currículums, programación de entrevistas, redacción de descripciones de puestos y preguntas de entrevista, entre otras.
4. **Experiencia de usuario mejorada**: Interfaz intuitiva y atractiva tanto para reclutadores como para candidatos, mejorando su engagement y satisfacción.
5. **Integración con otras herramientas de RRHH**: Compatibilidad con diversas plataformas y sistemas de gestión de recursos humanos.
6. **Análisis de datos avanzados**: Capacidades de generación de informes personalizados y análisis en profundidad de métricas de reclutamiento.
7. **Personalización y configuración**: Opciones para adaptar el sistema a las necesidades específicas de cada empresa.
8. **Seguridad y cumplimiento normativo**: Garantiza la protección de datos y el cumplimiento de regulaciones de privacidad.
9. **Escalabilidad**: Capacidad para manejar grandes volúmenes de candidatos sin comprometer el rendimiento.
10. **Soporte multilingüe y adaptabilidad regional**: Accesible a empresas y candidatos de diferentes regiones y culturas.
11. **Funciones multimedia**: Video-entrevistas, evaluaciones en línea y capacidades de reclutamiento en redes sociales.
12. **Acceso móvil optimizado**: Interfaz adaptada para dispositivos móviles, brindando flexibilidad a reclutadores y candidatos.
13. **Gamificación y engagement de candidatos**: Elementos lúdicos y atractivos que mejoran la experiencia de los candidatos.
14. **Modelo de precios flexible**: Opciones de planes adaptados al tamaño y necesidades de cada empresa.

## Funciones Principales

1. **Gestión integral del proceso de reclutamiento**: Desde la publicación de vacantes hasta la contratación final, pasando por la recopilación y clasificación de candidatos, programación de entrevistas, evaluaciones, ofertas de trabajo y seguimiento.
2. **Inteligencia Artificial aplicada**: Utilización de IA para tareas como matching de currículums, programación inteligente de entrevistas, redacción asistida de descripciones de puestos y preguntas de entrevista, entre otras.
3. **Colaboración y comunicación en tiempo real**: Plataforma centralizada que facilita la comunicación entre reclutadores, managers y candidatos, promoviendo una toma de decisiones más informada y ágil.
4. **Automatización de tareas**: Capacidades de automatización de procesos repetitivos, como el filtrado inicial de candidatos, envío de comunicaciones estandarizadas, programación de entrevistas, etc.
5. **Análisis de datos y generación de informes**: Herramientas avanzadas de análisis de datos y generación de informes personalizados sobre métricas clave de reclutamiento, tendencias y áreas de mejora.
6. **Gestión de marca empleadora**: Funcionalidades para promocionar la marca empleadora de la empresa, atrayendo a los mejores talentos.
7. **Integración con otras plataformas**: Capacidad de integrarse sin problemas con otros sistemas de gestión de recursos humanos, plataformas de redes sociales y profesionales, herramientas de evaluación, etc.
8. **Configuración y personalización**: Opciones para personalizar el sistema según las necesidades y preferencias de cada empresa, adaptándose a sus flujos de trabajo y procesos únicos.
9. **Seguridad y cumplimiento normativo**: Medidas de seguridad robustas y cumplimiento de regulaciones de protección de datos y privacidad.
10. **Soporte multilingüe y adaptabilidad regional**: Capacidad de operar en múltiples idiomas y adaptarse a diferentes regiones y culturas.
11. **Acceso móvil optimizado**: Interfaz móvil intuitiva y funcional para reclutadores y candidatos, permitiendo una experiencia fluida en cualquier momento y lugar.
12. **Gamificación y engagement de candidatos**: Elementos de gamificación y estrategias de engagement para mantener a los candidatos motivados e interesados durante todo el proceso.
13. **Modelo de precios flexible**: Diferentes opciones de planes y precios adaptados al tamaño y necesidades de cada empresa, desde pequeñas empresas hasta grandes corporaciones.

## Diagrama Lean Canvas
A continuación se muestra un diagrama tipo **Lean Canvas** con los siguientes elementos:

1. Problema
2. Segmento de clientes
3. Solución
4. Métricas clave
5. Ventaja especial
6. Canales
7. Estructura de costos
8. Fuentes de ingresos
9. Alternativas existentes
10. Primeros adoptantes

![Lean Canvas](./res/ats-lean-canvas.jpg)

## Casos de uso principales
### Caso de Uso 1: Publicación de Vacantes
1. **Roles de Usuario**:

  * **Reclutador**: Publica nuevas ofertas de trabajo.
  * **Manager de Contratación**: Aprueba las vacantes antes de su publicación.

2. **Acciones**:
* El Reclutador crea una nueva oferta de trabajo en el sistema.
* El Manager de Contratación revisa y aprueba la oferta de trabajo.
* Una vez aprobada, la vacante se publica automáticamente en los canales seleccionados.

3. **Dependencias**:
* La aprobación de la vacante por parte del Manager de Contratación es necesaria antes de la publicación.
* El Reclutador debe estar autenticado en el sistema para crear y enviar la oferta de trabajo.

**Diagrama de uso**:

![Flujo publicación de vacante](./res/cu1-publicacion-vacantes.png)

### Caso de Uso 2: Proceso de Selección de Candidatos

1. **Roles de Usuario**:
* **Candidato**: Aplica a las ofertas de trabajo y completa las evaluaciones requeridas.
* **Reclutador**: Revisa las aplicaciones y selecciona candidatos para entrevistas.

2. **Acciones**:
* El Candidato se registra en el sistema, completa su perfil y aplica a las vacantes.
* El Reclutador utiliza la IA para filtrar y clasificar las aplicaciones.
* Los candidatos seleccionados son notificados y programados para entrevistas.

3. **Dependencias**:
* Los Candidatos deben registrarse y completar su perfil para aplicar a las vacantes.
* El Reclutador necesita autenticarse para acceder a las aplicaciones y gestionar el proceso de selección.

**Diagrama de uso**:

![Flujo seleccion de candidatos](./res/cu2-seleccion-candidatos.png)

### Caso de Uso 3: Integración con Herramientas de RRHH

1. **Roles de Usuario**:
* **Administrador de Sistemas**: Configura y mantiene la integración con otras herramientas de RRHH.
* **Reclutador**: Utiliza las herramientas integradas para mejorar el proceso de reclutamiento.

2. **Acciones**:
* El Administrador de Sistemas establece conexiones con plataformas de RRHH externas.
* El Reclutador accede a las herramientas integradas para realizar tareas como la evaluación de competencias o la verificación de antecedentes.

3. **Dependencias**:
* La configuración por parte del Administrador de Sistemas es necesaria para la integración funcional.
* El Reclutador debe tener permisos adecuados para utilizar las herramientas integradas.

**Diagrama de uso**:

![Flujo integración con Herramientas de RRHH](./res/cu3-integracion-otras-htas.png)

## Modelo de datos
El siguiente diagrama muestra las entidades principales y sus relaciones en el contexto del sistema ATS que se está diseñando:

![Modelo de datos](./res/modelo-datos.jpeg)

## Diseño del sistema a alto nivel

Para implementar un sistema de seguimiento de candidatos (ATS) que cubra los casos de uso de "Registro de Candidatos", "Filtrar Candidatos" y "Análisis y Reportes", es fundamental elegir un patrón de arquitectura que facilite la escalabilidad, la mantenibilidad y la eficiencia. Dados estos requerimientos y la naturaleza del sistema, se recomienda utilizar una arquitectura basada en **microservicios**. Este patrón es particularmente adecuado debido a su flexibilidad para adaptarse a cambios y escalar partes específicas del sistema de manera independiente.

A continuación se describe la arquitectura de alto nivel del sistema de ATS haciendo uso exclusivo de servicios en la nube de AWS:

![Diagrama de alto nivel](./res/ats-diagrama-alto-nivel.png)

### Frontend:
Utiliza las librerías React.js y Next.js
* **Amazon CloudFront**: Como CDN, distribuirá el contenido estático y dinámico del frontend, mejorando la velocidad de carga y reduciendo la latencia.
* **Amazon S3 Bucket**: Almacenará los archivos estáticos del frontend como HTML, CSS y JavaScript.

### Backend:
Cada funcionalidad principal del ATS se desarrollará como un microservicio separado, permitiendo que cada uno se despliegue, escale y actualice de manera independiente. Esto es ideal para un sistema como un ATS, donde diferentes funciones pueden tener diferentes requisitos de carga y cambios frecuentes. Por tanto, en el diagrama anterior, habrá diversas instancias EC2, cada una de ellas con su propia base de datos en RDS, optimizada para su carga de trabajo específica. Ésta es una práctica común en la arquitectura de microservicios para asegurar la independencia y la eficiencia. Se requiere un API Gateway que actúa como un punto de entrada único para todas las solicitudes, encaminándolas a los microservicios apropiados. Se utilizarán contenedores Docker para empaquetar las aplicaciones y facilitar su despliegue.

*-Microservicio de Gestión de Candidatos:* Maneja todo el registro y la información personal de los candidatos.
*-Microservicio de Aplicaciones:* Procesa las solicitudes de empleo y las asociaciones a diferentes puestos.
*-Microservicio de Entrevistas:* Administra la programación y los resultados de las entrevistas.
*-Microservicio de Reportes:* Genera análisis y reportes basados en datos recopilados de otros microservicios.


* **Elastic Load Balancing (ELB)**: Distribuirá el tráfico entrante entre las instancias EC2 para mejorar la disponibilidad y la tolerancia a fallos.
* **Auto Scaling Group**: Asegurará que el número de instancias EC2 se ajuste automáticamente según la demanda para manejar la carga y mantener la escalabilidad.
* **Amazon EC2**: Instancias para alojar la lógica de negocio del backend.
* **Amazon RDS / Aurora**: Base de datos relacional gestionada que almacenará el modelo de datos del ATS y proporcionará alta disponibilidad y escalabilidad.
* **Amazon ElastiCache**: Para caché en memoria, reducirá la carga en la base de datos y mejorará el rendimiento de las consultas frecuentes.

### Integración y Comunicación:
* **AWS Lambda**: Para ejecutar código en respuesta a eventos, como procesamiento de aplicaciones o tareas de automatización.
* **Amazon SNS y SQS**: Para la mensajería y la comunicación asíncrona entre servicios, asegurando la entrega de mensajes y el desacoplamiento de componentes.

### Seguridad:
* **AWS Identity and Access Management (IAM)**: Para controlar el acceso a los recursos de AWS de manera segura.
* **Amazon Cognito**: Para la gestión de usuarios y el control de acceso al frontend.
* **AWS WAF y Shield**: Para proteger la aplicación de ataques web comunes y DDoS.

### Almacenamiento y Procesamiento de Datos:
* **Amazon S3**: Para almacenar datos no estructurados como currículums y otros documentos de los candidatos.
* **AWS Glue**: Para transformación y carga de datos, permitiendo la integración con otras fuentes de datos.
* **Amazon Redshift**: Para análisis de datos y generación de informes, escalable y optimizado para consultas SQL.

### Escalabilidad y Disponibilidad:
* La combinación de Auto Scaling, ELB y múltiples instancias EC2 garantizará la escalabilidad horizontal y la alta disponibilidad.
* La replicación y la configuración de Aurora proporcionarán redundancia y recuperación ante fallos.

### Mantenibilidad:
* Utilización de servicios gestionados como RDS y Aurora reducirá la carga operativa en el mantenimiento de la base de datos.
* Implementación de infraestructura como código (IaC) con AWS CloudFormation para facilitar la gestión y actualización de recursos.



## Diagramas C4

### Diagrama de contexto - nivel 1:
Este diagrama muestra a los usuarios principales (**Candidato**, **Reclutador**, **Manager de Contratación**) y cómo interactúan con el sistema ATS. También muestra la integración del sistema ATS con sistemas externos como sistemas de RRHH, plataformas de empleo y servicios de email:

![Diagrama de contexto](./res/c4-diagrama-contexto.png)

### Diagrama de contenedores - nivel 2:
Este diagrama de contenedores muestra cómo los usuarios (**Candidato**, **Reclutador**, **Manager de Contratación**) interactúan con la Aplicación Web ATS y cómo esta se comunica con los servicios de backend, autenticación y la API de integración. También se ilustra la interacción del sistema ATS con sistemas externos:

![Diagrama de contenedores](./res/c4-diagrama-contenedores.png)

### Diagrama de componentes - nivel 3:
Este diagrama de componentes muestra los principales componentes dentro del servicio de backend ATS y cómo interactúan entre sí. Cada componente tiene una responsabilidad específica, como manejar solicitudes de usuario, gestionar vacantes, procesar aplicaciones de candidatos, autenticar usuarios, enviar notificaciones, y comunicarse con la base de datos y servicios de búsqueda:

![Diagrama de componentes](./res/c4-diagrama-componentes.png)

### Diagrama de código - nivel 4:
Este diagrama de código se centra en el **Controlador de Aplicaciones** y muestra las clases o módulos que lo componen, como el modelo de aplicación, el servicio de aplicación, el repositorio de aplicaciones y el validador de aplicaciones. También se ilustran las interacciones y dependencias entre estos componentes, proporcionando una visión detallada de cómo se implementa la gestión de aplicaciones en el sistema ATS:

![Diagrama de código](./res/c4-diagrama-codigo.png)

### Diagrama completo:
En este último diagrama se muestra el diagrama C4 combinado. Se añade para tener otro posible ejemplo, y por dar mayor detalle en el nivel 4 de código, donde se especifican las funciones clave.

![Diagrama C4 completo](./res/c4-diagrama-completo.png)

## Conclusiones
Hemos completado un recorrido exhaustivo por el diseño de un sistema de seguimiento de candidatos (ATS) utilizando el modelo C4 para visualizar su arquitectura. Comenzamos con el **diagrama de contexto**, que establece cómo el sistema ATS interactúa con usuarios y sistemas externos, proporcionando una visión general de alto nivel.

Luego, profundizamos en el **diagrama de contenedores**, detallando las aplicaciones y servicios que componen el sistema, sus tecnologías subyacentes y cómo se comunican entre sí. Este nivel nos ayudó a entender la estructura y la distribución de las funcionalidades del sistema ATS.

El siguiente paso fue el **diagrama de componentes**, donde desglosamos el servicio de backend ATS en sus componentes individuales, mostrando la responsabilidad de cada uno y cómo contribuyen al procesamiento de la lógica de negocio y la gestión de datos.

Finalmente, con el **diagrama de código**, nos centramos en el Controlador de Aplicaciones, ilustrando las clases y módulos específicos que lo componen y cómo se implementan las operaciones críticas del sistema.

A lo largo de este proceso, hemos asegurado que la arquitectura cumpla con los requisitos no funcionales de escalabilidad, seguridad, mantenibilidad y disponibilidad, utilizando servicios de AWS para una infraestructura robusta y confiable.

Este trabajo sienta las bases para una documentación completa y un entendimiento claro del sistema ATS, facilitando futuras iteraciones, mantenimiento y escalabilidad del sistema.