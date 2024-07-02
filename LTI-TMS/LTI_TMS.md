# 🚀 LTI: El ATS del Futuro

## 1 🌟 Descripción Breve

LTI (Talent Intelligence) es una startup revolucionaria que está desarrollando el **ATS (Applicant-Tracking System) del futuro**. Nuestro sistema utiliza inteligencia artificial de vanguardia y aprendizaje automático para transformar el proceso de reclutamiento y selección de personal.

## 💎 Valor Añadido y Ventajas Competitivas

1. 🧠 IA predictiva para evaluación de candidatos
2. 📊 Análisis de datos en tiempo real
3. 🔗 Integración perfecta con redes sociales y profesionales
4. 🎨 UX intuitiva para reclutadores y candidatos
5. 🤖 Automatización avanzada de tareas repetitivas
6. 🛡️ Cumplimiento de normativas de privacidad y no discriminación

## 🔑 Funciones Principales

1. 📢 Publicación automatizada de ofertas multi-plataforma
2. 🔍 Screening inteligente de CV y perfiles
3. 🗓️ Gestión de entrevistas con asistente virtual
4. 📝 Pruebas online adaptativas
5. 📈 Seguimiento del proceso en tiempo real
6. 📊 Informes y análisis predictivos
7. 🚪 Onboarding digital integrado

## 📘 Lean Canvas de LTI

# Lean Canvas de LTI

Problema:

- Procesos de selección lentos
- Dificultad para encontrar talento
- Sesgos en la contratación

Solución:

- ATS con IA
- Automatización inteligente
- Análisis predictivo

Propuesta de Valor:

- Reducción del tiempo de contratación
- Mejora en la calidad de las contrataciones
- Proceso más justo y transparente

Métricas Clave:

- Tiempo de contratación
- Calidad de contrataciones
- Satisfacción de usuarios

Ventaja Competitiva:

- IA avanzada
- UX superior
- Integración completa

Canales:

- Venta directa B2B
- Marketing digital
- Partnerships con consultoras de RRHH

Estructura de Costes:

- Desarrollo de software
- Infraestructura cloud
- Marketing y ventas
- Soporte al cliente

Fuentes de Ingresos:

- Suscripción mensual/anual
- Servicios de consultoría
- Integraciones personalizadas

# 2 🎯 Casos de Uso Principales de LTI

## 🟢 Caso de Uso 1: Publicación y Gestión de Ofertas de Trabajo

**Actores:** 👩‍💼 Reclutador, 🖥️ Sistema LTI

### Flujo Principal:

1. 🔐 Reclutador inicia sesión
2. ➕ Selecciona "Crear nueva oferta"
3. ✍️ Completa detalles de la oferta
4. 🧠 IA sugiere mejoras
5. 👀 Reclutador revisa y acepta sugerencias
6. 🌐 Selecciona plataformas de publicación
7. 🚀 Sistema publica automáticamente
8. ✅ Confirma publicación exitosa

### Flujos Alternativos:

- 💾 Guardar como borrador
- ⚠️ Alerta de ofertas similares

## 🔵 Caso de Uso 2: Screening Inicial de Candidatos

**Actores:** 🖥️ Sistema LTI, 👤 Candidato

### Flujo Principal:

1. 📝 Candidato aplica a oferta
2. 📊 Sistema extrae información del CV
3. 🤖 IA evalúa idoneidad
4. 🔍 Compara habilidades y experiencia
5. 🏅 Asigna puntuación inicial
6. 🏷️ Categoriza al candidato
7. 📝 Envía test de evaluación si aplica
8. 🔄 Actualiza perfil del candidato
9. 📣 Notifica al reclutador

### Flujos Alternativos:

- ❓ Solicita información faltante
- 🗣️ Programa entrevista automatizada

## 🟣 Caso de Uso 3: Seguimiento y Análisis del Proceso

**Actores:** 👩‍💼 Reclutador, 👨‍💼 Gerente RRHH, 🖥️ Sistema LTI

### Flujo Principal:

1. 📊 Acceso al dashboard
2. 🎯 Selección de oferta activa
3. 📈 Muestra métricas en tiempo real
4. 🔍 Filtrado de datos
5. 📊 Generación de gráficos interactivos
6. 🔮 Solicitud de informe predictivo
7. 🧠 IA genera predicciones
8. 📄 Presentación del informe
9. 🔗 Compartir con stakeholders

### Flujos Alternativos:

- 🔔 Configuración de alertas
- 💡 Sugerencias de ajuste de estrategia

## 3 Modelo de datos y diagrama

# **Entidades Principales y Atributos**

1. **Candidato**

   - **ID**: Integer
   - **Nombre**: String
   - **Correo Electrónico**: String
   - **Teléfono**: String
   - **Experiencia**: Text
   - **Estado**: String

2. **Oferta de Trabajo**

   - **ID**: Integer
   - **Título**: String
   - **Descripción**: Text
   - **Fecha de Publicación**: Date
   - **Estado**: String

3. **Aplicación**

   - **ID**: Integer
   - **Candidato_ID**: Integer (FK)
   - **Oferta_ID**: Integer (FK)
   - **Fecha de Aplicación**: Date
   - **Estado**: String

4. **Entrevista**

   - **ID**: Integer
   - **Candidato_ID**: Integer (FK)
   - **Oferta_ID**: Integer (FK)
   - **Fecha**: Date
   - **Estado**: String

5. **Prueba**
   - **ID**: Integer
   - **Tipo**: String
   - **Descripción**: Text
   - **Fecha**: Date
   - **Resultado**: String

# Diagrama de Modelo de Datos

```pl
@startuml
entity "Candidato" as Candidato {
ID: Integer
Nombre: String
CorreoElectronico: String
Telefono: String
Experiencia: Text
Estado: String
}

entity "Oferta de Trabajo" as OfertaDeTrabajo {
ID: Integer
Titulo: String
Descripcion: Text
FechaDePublicacion: Date
Estado: String
}

entity "Aplicación" as Aplicacion {
ID: Integer
CandidatoID: Integer
OfertaID: Integer
FechaDeAplicacion: Date
Estado: String
}

entity "Entrevista" as Entrevista {
ID: Integer
CandidatoID: Integer
OfertaID: Integer
Fecha: Date
Estado: String
}

entity "Prueba" as Prueba {
ID: Integer
Tipo: String
Descripcion: Text
Fecha: Date
Resultado: String
}

Candidato ||--o{ Aplicacion : "hace"
OfertaDeTrabajo ||--o{ Aplicacion : "recibe"
Candidato ||--o{ Entrevista : "hace"
OfertaDeTrabajo ||--o{ Entrevista : "recibe"
Candidato ||--o{ Prueba : "hace"
@enduml

```

### 4. Diseño del Sistema a Alto Nivel

El diseño del sistema a alto nivel proporciona una vista general de la arquitectura del sistema, mostrando los principales componentes y sus interacciones. Esto incluye la arquitectura lógica y la distribución de los componentes.

#### **Componentes Principales**

1. **Portal del Candidato**
   - Interfaz de usuario donde los candidatos pueden registrarse, buscar ofertas de trabajo, aplicar, y seguir el estado de sus aplicaciones.
2. **Portal del Reclutador**
   - Interfaz de usuario donde los reclutadores pueden publicar ofertas, gestionar aplicaciones, programar entrevistas, y evaluar candidatos.
3. **Motor de Recomendación**
   - Componente basado en inteligencia artificial que clasifica y recomienda candidatos para las ofertas de trabajo.
4. **Gestor de Entrevistas**
   - Herramienta para programar y gestionar entrevistas, incluyendo la integración con calendarios externos.
5. **Evaluador de Pruebas**
   - Sistema que administra y evalúa pruebas técnicas y psicométricas.
6. **Base de Datos**
   - Almacena toda la información relacionada con candidatos, ofertas, aplicaciones, entrevistas, y pruebas.
7. **API de Integración**
   - Facilita la comunicación con sistemas externos como plataformas de empleo y herramientas de recursos humanos.

#### **Diagrama de Arquitectura a Alto Nivel**

```pl
@startuml
package "Frontend" {
  [Portal del Candidato] --> [API de Integración]
  [Portal del Reclutador] --> [API de Integración]
}

package "Backend" {
  [API de Integración] --> [Motor de Recomendación]
  [API de Integración] --> [Gestor de Entrevistas]
  [API de Integración] --> [Evaluador de Pruebas]
  [Motor de Recomendación] --> [Base de Datos]
  [Gestor de Entrevistas] --> [Base de Datos]
  [Evaluador de Pruebas] --> [Base de Datos]
}

package "Database" {
  [Base de Datos]
}

@enduml

```

### **Descripción de la Arquitectura**

- **Frontend**: Compuesto por el **Portal del Candidato** y el **Portal del Reclutador**, que proporcionan interfaces de usuario interactivas para los candidatos y reclutadores respectivamente. Ambos portales se comunican con el backend a través de la **API de Integración**.

- **Backend**: Incluye varios componentes clave:

  - **API de Integración**: Actúa como un intermediario, manejando todas las solicitudes y respuestas entre el frontend y los componentes backend.
  - **Motor de Recomendación**: Utiliza algoritmos de inteligencia artificial para clasificar y recomendar candidatos adecuados para las ofertas de trabajo.
  - **Gestor de Entrevistas**: Facilita la programación y gestión de entrevistas, incluyendo la sincronización con calendarios externos.
  - **Evaluador de Pruebas**: Administra las pruebas técnicas y psicométricas y evalúa los resultados.

- **Database**: Almacena toda la información esencial, incluyendo datos de candidatos, ofertas de trabajo, aplicaciones, entrevistas y resultados de pruebas.

### 5 **Diagrama C4 y Descripción de un Componente**

## Nivel 1: Diagrama de Contexto

```pl
@startuml
actor "Candidato" as Candidate
actor "Reclutador" as Recruiter

package "LTI System" {
  [Portal del Candidato] --> [API de Integración]
  [Portal del Reclutador] --> [API de Integración]
  [API de Integración] --> [Motor de Recomendación]
  [Motor de Recomendación] --> [Base de Datos]
}

Candidate --> [Portal del Candidato]
Recruiter --> [Portal del Reclutador]
@enduml
```

## Nivel 2: Diagrama de Contenedores

```pl
@startuml
package "LTI System" {
  package "Frontend" {
    [Portal del Candidato]
    [Portal del Reclutador]
  }

  package "Backend" {
    [API de Integración]
    [Motor de Recomendación]
    [Gestor de Entrevistas]
    [Evaluador de Pruebas]
  }

  package "Database" {
    [Base de Datos]
  }
}

[Portal del Candidato] --> [API de Integración]
[Portal del Reclutador] --> [API de Integración]
[API de Integración] --> [Motor de Recomendación]
[API de Integración] --> [Gestor de Entrevistas]
[API de Integración] --> [Evaluador de Pruebas]
[Motor de Recomendación] --> [Base de Datos]
[Gestor de Entrevistas] --> [Base de Datos]
[Evaluador de Pruebas] --> [Base de Datos]
@enduml
```

## Nivel 3: Diagrama de Componentes del Motor de Recomendación

```pl
@startuml
package "Motor de Recomendación" {
  [Service Interface] --> [Recommendation Engine]
  [Recommendation Engine] --> [Machine Learning Model]
  [Machine Learning Model] --> [Data Preprocessing]
  [Data Preprocessing] --> [Feature Extraction]
}

package "Database" {
  [Candidate Data]
  [Job Offer Data]
  [Application Data]
}

[Service Interface] --> [API de Integración]
[Recommendation Engine] --> [Candidate Data]
[Recommendation Engine] --> [Job Offer Data]
[Recommendation Engine] --> [Application Data]
@enduml
```

### **Descripción del Componente: Motor de Recomendación**

El Motor de Recomendación es un componente clave del sistema LTI, encargado de clasificar y recomendar candidatos adecuados para las ofertas de trabajo. Este componente utiliza algoritmos de inteligencia artificial y aprendizaje automático para analizar datos y generar recomendaciones precisas.

#### **Componentes del Motor de Recomendación**

- **Service Interface**: Proporciona una interfaz de servicio para que otros componentes del sistema (como la API de Integración) interactúen con el Motor de Recomendación.
- **Recommendation Engine**: El núcleo del componente, que ejecuta los algoritmos de recomendación basados en los modelos de aprendizaje automático.
- **Machine Learning Model**: Modelos entrenados que se utilizan para realizar las predicciones y recomendaciones.
- **Data Preprocessing**: Responsable de la limpieza y transformación de los datos antes de que sean utilizados por los modelos de aprendizaje automático.
- **Feature Extraction**: Extrae características relevantes de los datos para mejorar la precisión de los modelos de aprendizaje automático.

#### **Interacción con la Base de Datos**

El Motor de Recomendación se comunica con la base de datos para obtener datos de candidatos, ofertas de trabajo y aplicaciones, y utiliza estos datos para generar recomendaciones que son devueltas a través de la API de Integración.

- **Candidate Data**
- **Job Offer Data**
- **Application Data**

#### **Flujo de Datos**

1. **Service Interface** recibe solicitudes de recomendación a través de la **API de Integración**.
2. **Recommendation Engine** procesa la solicitud utilizando el **Machine Learning Model**.
3. **Data Preprocessing** limpia y transforma los datos necesarios.
4. **Feature Extraction** extrae las características relevantes de los datos.
5. **Recommendation Engine** genera recomendaciones basadas en los datos de **Candidate Data**, **Job Offer Data** y **Application Data**.
6. Las recomendaciones son devueltas a través de la **Service Interface** a la **API de Integración**.
