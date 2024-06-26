### Descripción breve del software LTI, valor añadido y ventajas competitivas. Explicación de las funciones principales. Añadir un diagrama Lean Canvas para entender el modelo de negocio.

Descripción del Software LTI
El Software LTI es una solución avanzada de gestión de candidatos que optimiza el proceso de contratación para empresas de todos los tamaños. Su valor añadido reside en su capacidad para automatizar y simplificar las tareas de reclutamiento, permitiendo a las empresas enfocarse en seleccionar los mejores talentos. Las ventajas competitivas incluyen una interfaz intuitiva, herramientas avanzadas de análisis y reporting, y una integración perfecta con diversas plataformas de empleo y redes sociales.

Funciones Principales
Gestión de Candidatos

Permite a los reclutadores almacenar y gestionar perfiles de candidatos de manera eficiente.
Funciones de búsqueda avanzada para encontrar rápidamente candidatos según criterios específicos.
Publicación de Ofertas

Posibilidad de crear y publicar ofertas de trabajo en múltiples plataformas desde una única interfaz.
Herramientas para personalizar y optimizar las descripciones de las ofertas.
Seguimiento de Solicitudes

Sistema para rastrear el estado de cada solicitud y recibir notificaciones sobre actualizaciones importantes.
Funcionalidades de comunicación integradas para facilitar la interacción con los candidatos.
Programación de Entrevistas

Herramientas para organizar y gestionar entrevistas, incluyendo la coordinación de horarios con los candidatos y los entrevistadores.
Integración con calendarios externos para simplificar la programación.
Análisis y Reportes

Generación de informes detallados sobre el proceso de reclutamiento, incluyendo métricas clave como tiempo de contratación y fuentes de candidatos.
Análisis de datos para identificar áreas de mejora y optimizar las estrategias de reclutamiento.
Integración con Redes Sociales

Conexión con LinkedIn y otras redes sociales para importar perfiles y contactar con candidatos potenciales.
Funcionalidades para compartir ofertas de trabajo en redes sociales y atraer a un mayor número de candidatos.

[Lean Canvas del Software LTI](https://LTI-CAAM\mermaid-diagram-FlowChard-CAAM.png)
[Lean Canvas del Software LTI](https://LTI-CAAM\Diagrama lean canvas.md)

Descripción del Lean Canvas
- Problema: Contratación ineficiente, procesos manuales, falta de visibilidad.
- Solución: Gestión automatizada y centralizada de candidatos.
- Propuesta de Valor: Ahorro de tiempo y recursos, mejora en la calidad de contratación.
- Ventaja Competitiva: Integración con múltiples plataformas y análisis avanzado.
- Segmentos de Clientes: Empresas de todos los tamaños que necesitan optimizar su proceso de contratación.
- Estructura de Costos: Desarrollo y mantenimiento del software, marketing, soporte técnico.
- Flujo de Ingresos: Suscripciones mensuales/anuales, tarifas por uso.
- Canales: Marketing digital, redes sociales, partnerships con plataformas de empleo.
- Relación con Clientes: Soporte técnico, atención personalizada, actualización constante.
- Actividades Clave: Desarrollo de software, marketing, soporte al cliente.
- Recursos Clave: Equipo de desarrollo, equipo de marketing, infraestructura tecnológica.
- Socios Clave: Plataformas de empleo, redes sociales, proveedores de tecnología.

### Descripción de los 3 casos de uso principales, con el diagrama asociado a cada uno

1. Publicación de Ofertas de Trabajo
Descripción: Permitir a los reclutadores crear, editar y publicar ofertas de trabajo en múltiples plataformas (sitio web de la empresa, portales de empleo, redes sociales).
Funcionalidades:
Formulario para crear y editar ofertas de trabajo.
Opción para publicar en múltiples canales.
Visualización de las ofertas publicadas.

2. Recepción y Gestión de Solicitudes
Descripción: Automatizar la recepción de solicitudes de empleo y organizarlas en una base de datos centralizada.
Funcionalidades:
Formulario de solicitud para candidatos.
Almacenamiento automático de solicitudes en la base de datos.
Clasificación y etiquetado de solicitudes.

3. Base de Datos de Candidatos
Descripción: Mantener una base de datos de todos los candidatos con capacidad de búsqueda y filtrado.
Funcionalidades:
Creación y actualización de perfiles de candidatos.
Búsqueda y filtrado de candidatos por criterios específicos (habilidades, experiencia, ubicación).
Exportación de datos de candidatos.

....

[CasosDeUso.md](https://LTI-CAAM\CasosDeUso.md)
[imageCasosDeUso](https://LTI-CAAM\CasosdeusoCAAM.jpg)

### Modelo de datos que cubra entidades, atributos (nombre y tipo) y relaciones

Para un sistema de gestión de candidatos online, además de las entidades 'Candidato', 'Oferta de Trabajo' y 'Solicitud', podrías considerar las siguientes entidades adicionales:

- Empresa
- Entrevista
- Reclutador
- Habilidad
- Educación
- Experiencia Laboral

Aquí están los detalles de cada una, incluyendo sus campos más importantes y las relaciones entre ellas:

[ModeloDeDatos.md](https://LTI-CAAM\ModeloDeDatos.md)

![image modelodedatosCAAM](https://LTI-CAAM\modelodedatosCAAM.jpg)

Descripción de las entidades:
Empresa

id: int
nombre: string
ubicacion: string
industria: string
descripcion: string
website: string
Entrevista

id: int
id_solicitud: int
fecha_entrevista: date
estado: string
comentarios: text
Reclutador

id: int
nombre: string
email: string
telefono: string
posicion: string
Habilidad

id: int
nombre: string
Educación

id: int
id_candidato: int
titulo: string
institucion: string
fecha_inicio: date
fecha_fin: date
descripcion: string
Experiencia Laboral

id: int
id_candidato: int
empresa: string
titulo: string
fecha_inicio: date
fecha_fin: date
descripcion: string

### Diseño del sistema a alto nivel, tanto explicado como diagrama adjunto

Diseño del Sistema de Alto Nivel
El diseño del sistema de gestión de candidatos online se basará en la arquitectura hexagonal (Arquitectura de Puertos y Adaptadores), que promueve la separación de las preocupaciones y facilita el mantenimiento y la escalabilidad.

Arquitectura Hexagonal
La arquitectura hexagonal divide el sistema en capas o módulos con responsabilidades claras, lo que permite una fácil integración de nuevas funcionalidades y una mejor prueba de componentes. Las capas principales son:

Dominio: Contiene la lógica de negocio y las reglas del dominio.
Aplicación: Orquesta la lógica de negocio, coordinando las operaciones del dominio.
Adaptadores: Conectan la aplicación con el mundo exterior, incluyendo bases de datos, interfaces de usuario, APIs externas, etc.
Componentes del Sistema
Core (Dominio)

Entidades: Candidato, Oferta de Trabajo, Solicitud, Empresa, Entrevista, Reclutador, Habilidad, Educación, Experiencia.
Servicios del Dominio: Gestionan la lógica de negocio específica.
Repositorios: Interfaz para acceder a los datos del dominio.
Aplicación

Casos de Uso/Servicios de Aplicación: Coordinan la ejecución de la lógica del dominio según las acciones del usuario.
Adaptadores

Adaptadores de Entrada: APIs REST, interfaces de usuario web.
Adaptadores de Salida: Conectores a bases de datos, servicios externos (e.g., LinkedIn API).

[Diagrama de Arquitectura Hexagonal](https://LTI-CAAM\diagrams\architectureCaamCode.md)
[imagen](https://LTI-CAAM\img\architectureCAAM.png)


Explicación de la Arquitectura Hexagonal
Dominio: Es el núcleo del sistema donde reside toda la lógica de negocio. Las entidades representan los objetos de negocio (e.g., Candidato, Oferta). Los servicios del dominio contienen la lógica que manipula estas entidades.
Aplicación: Actúa como un intermediario entre el dominio y los adaptadores, ejecutando casos de uso específicos basados en las acciones del usuario.
Adaptadores: Los adaptadores de entrada manejan las interacciones del usuario (a través de APIs REST o UI web) y los adaptadores de salida se conectan a la infraestructura necesaria (bases de datos, servicios externos).
Este diseño asegura que la lógica de negocio no dependa de los detalles de infraestructura, facilitando el mantenimiento y permitiendo que el sistema evolucione sin comprometer su integridad.

### Diagrama C4 que llegue en profundidad a uno de los componentes del sistema, el que prefieras

El diagrama C4 (Context, Container, Component, and Code) ofrece una vista detallada de la arquitectura del sistema en diferentes niveles de abstracción. Aquí está un ejemplo simplificado de los primeros tres niveles:

[Contexto.md](https://LTI-CAAM\diagrams\ContextoC4.md)
[Contexto.png](https://LTI-CAAM\img\C4Contexto.png)

[Contenedores.md](https://LTI-CAAM\diagrams\ContenedoresC4.md)
[Contenedores.png](https://LTI-CAAM\img\C4Contenedores.png)

[Componentes.md](https://LTI-CAAM\diagrams\ComponentesC4.md)
[Componentes.png](https://LTI-CAAM\img\C4Componentes.png)

Explicación del Diagrama C4

- Contexto: Describe los actores principales que interactúan con el sistema y cómo se relacionan.

- Contenedores: Desglosa el sistema en contenedores (aplicación web, API REST, base de datos, servicios externos) y muestra cómo interactúan entre sí.

- Componentes: Desglosa uno de los contenedores (la API REST en este caso) en componentes más pequeños para mostrar las relaciones internas y cómo se manejan las peticiones.

