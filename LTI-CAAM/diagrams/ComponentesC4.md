graph TD
    API[API REST]
    subgraph Componentes
        Controller[Controlador]
        Service[Servicio]
        Repository[Repositorio]
    end
    
    WebApp[Aplicación Web] -->|Hace peticiones a| Controller
    Controller -->|Llama a| Service
    Service -->|Usa| Repository
    Repository -->|Accede a| DB[Base de Datos]
