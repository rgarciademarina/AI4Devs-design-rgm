### prompt 1
Eres un experto en producto, con experiencia en sistemas de gestion de candidatos.
¿Qué funcionalidades básicas tiene un sistema de gestion de candidatos?
Descríbemelas en un listado, ordenado de mayor a menor prioridad

### prompt 2
¿Qué beneficios obtiene el cliente de un istema de gestion de candidatos para considerar su uso?


### prompt 3
¿Qué alternativas tiene a usar un sistema de gestion de candidatos y cuando pueden ser relevantes?

### prompt 4
¿Cómo es el customer journey normal de un cliente que usa un sistema de getion de candidatos? Descríbeme paso a paso todas las interacciones

### prompt 5
Qué sistemas de gestion de candidatos open source son más conocidos?

### prompt 6
¿Qué sistemas de gestion de candidatos comerciales son más conocidos? Compáralos en función de [funcionalidades a,b,c] y valora cuál sería mejor opción


### prompt 7
Eres un analista de software experto. Estoy construyendo un sistema de gestion de candidatos online. Enumera y describe brevemente los casos de uso más importantes a implementar para lograr una funcionalidad básica


### prompt 8
Representa estos casos de uso en el tipo de diagrama más adecuado usando el formato plantUML. Diferencia entre usuarios visitantes y usuarios logueados. Acorde a la sintaxis y buenas prácticas UML, define y describe lo que sea necesario. 

### prompt 9
Eres un arquitecto de software experto. Cuales son las 3 entidades de modelo de datos esenciales en un sistema de gestion de candidatos online? Dame algunos campos esenciales de cada una y cómo se relacionan

### prompt 10
Eres un brillante arquitecto de software. Eres capaz de diseñar, explicar y diagramar los diferentes aspectos de un sistema de software. 

Estoy construyendo un sistema de gestion de candidatos online. He definido las entidades 'candidato', 'oferta de trabajo' y 'solicitud', con sus campos y relaciones, lo adjunto. 

Qué otras entidades del modelo de datos son importantes en un sistema de gestion de candidatos online? Dame los campos más importantes de cada una y cómo se relacionan entre entidades.

(Código diagrama mermaid)


@startuml

entity "Candidato" as C {
  +id: int
  +nombre: string
  +email: string
  +telefono: string
  +cv_url: string
  +perfil_linkedin: string
  +fecha_registro: date
}

entity "Oferta de Trabajo" as O {
  +id: int
  +titulo: string
  +descripcion: text
  +ubicacion: string
  +fecha_publicacion: date
  +estado: string
}

entity "Solicitud" as S {
  +id: int
  +id_candidato: int
  +id_oferta: int
  +fecha_solicitud: date
  +estado_solicitud: string
}

C ||--o{ S : "aplica"
O ||--o{ S : "recibe"

@enduml

### prompt 11
Crea un diseño del sistema de alto nivel, con explicación de la arquitectura hexagonal y diagrama


### prompt 12 https://diagrammingai.com/
Implement a hexagonal architecture for an online Applicant Tracking System using Greenhouse, with microservices having their own database. The frontend communicates through APIs, hosted on AWS with load balancing and CDN. Use the provided code structure as a reference.

### prompt 13

revisa el Código del diagrama, hay un error de syntaxis linea 2 - 17

además, crea otro diagrama tipo C4.