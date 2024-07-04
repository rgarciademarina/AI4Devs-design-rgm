graph TD
    Sistema[<b>Sistema de Gestión de Candidatos</b>]
    subgraph Contenedores
        WebApp[Aplicación Web]
        API[API REST]
        DB[Base de Datos]
        ExternalServices[Servicios Externos]
    end
    
    Usuario[Usuario] -->|Usa| WebApp
    WebApp -->|Comunica con| API
    API -->|Lee/Escribe| DB
    API -->|Conecta a| ExternalServices[Servicios Externos]
    Empresa[Empresa] -->|Publica ofertas a través de| WebApp
    Reclutador[Reclutador] -->|Gestiona a través de| WebApp
