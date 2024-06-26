@startuml
actor "Visitante" as Visitor
actor "Usuario Logueado" as LoggedInUser
actor "Reclutador" as Recruiter
actor "Administrador" as Admin

usecase "Publicar Ofertas de Trabajo" as U1
usecase "Recepción de Solicitudes" as U2
usecase "Gestión de Solicitudes" as U3
usecase "Base de Datos de Candidatos" as U4
usecase "Seguimiento del Proceso de Selección" as U5
usecase "Programación de Entrevistas" as U6
usecase "Comunicación con Candidatos" as U7
usecase "Evaluación de Candidatos" as U8
usecase "Informes y Análisis" as U9
usecase "Gestión de Usuarios y Permisos" as U10
usecase "Cumplimiento Legal y Gestión de Documentos" as U11

Visitor --> U2 : "Enviar solicitud"
Visitor --> U3 : "Consultar ofertas"

LoggedInUser --> U2 : "Enviar solicitud"
LoggedInUser --> U3 : "Consultar ofertas"

Recruiter --> U1 : "Crear y publicar ofertas"
Recruiter --> U3 : "Consultar solicitudes"
Recruiter --> U4 : "Consultar candidatos"
Recruiter --> U5 : "Actualizar estado de candidatos"
Recruiter --> U6 : "Programar entrevistas"
Recruiter --> U7 : "Enviar correos"
Recruiter --> U8 : "Evaluar candidatos"
Recruiter --> U9 : "Generar informes"

Admin --> U10 : "Gestionar usuarios"
Admin --> U11 : "Gestionar documentos y cumplir normativas"
@enduml