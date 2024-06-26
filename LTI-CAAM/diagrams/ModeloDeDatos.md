erDiagram
    Candidato {
        int id
        string nombre
        string email
        string telefono
        string cv_url
        string perfil_linkedin
        date fecha_registro
    }

    Oferta {
        int id
        string titulo
        text descripcion
        string ubicacion
        date fecha_publicacion
        string estado
        int empresa_id
        int reclutador_id
    }

    Solicitud {
        int id
        int id_candidato
        int id_oferta
        date fecha_solicitud
        string estado_solicitud
    }

    Empresa {
        int id
        string nombre
        string ubicacion
        string industria
        string descripcion
        string website
    }

    Entrevista {
        int id
        int id_solicitud
        date fecha_entrevista
        string estado
        text comentarios
    }

    Reclutador {
        int id
        string nombre
        string email
        string telefono
        string posicion
    }

    Habilidad {
        int id
        string nombre
    }

    Educacion {
        int id
        int id_candidato
        string titulo
        string institucion
        date fecha_inicio
        date fecha_fin
        string descripcion
    }

    Experiencia {
        int id
        int id_candidato
        string empresa
        string titulo
        date fecha_inicio
        date fecha_fin
        string descripcion
    }

    Candidato ||--o{ Solicitud : "aplica"
    Oferta ||--o{ Solicitud : "recibe"
    Empresa ||--o{ Oferta : "publica"
    Solicitud ||--o{ Entrevista : "tiene"
    Reclutador ||--o{ Oferta : "gestiona"
    Candidato ||--o{ Habilidad : "posee"
    Candidato ||--o{ Educacion : "ha_completado"
    Candidato ||--o{ Experiencia : "ha_trabajado"
