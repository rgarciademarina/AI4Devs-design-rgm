from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.database import RDS
from diagrams.aws.network import APIGateway
from diagrams.aws.security import Cognito
from diagrams.aws.storage import S3
from diagrams.onprem.client import Users

with Diagram("ATS de LTI - API REST", show=False):

    users = Users("Usuarios")

    with Cluster("Frontend"):
        webapp = Lambda("Aplicación Web")

    with Cluster("Backend"):
        api_gw = APIGateway("API Gateway")
        auth = Cognito("Autenticación")

        with Cluster("Microservicios"):
            auth_service = Lambda("AuthController")
            candidate_service = Lambda("CandidateController")
            job_service = Lambda("JobController")
            filtering_service = Lambda("FilteringController")

    with Cluster("Base de Datos"):
        database = RDS("Amazon RDS")

    with Cluster("Servicio de IA"):
        ia_service = Lambda("IAService")

    with Cluster("Almacenamiento"):
        storage = S3("Amazon S3")

    users >> webapp >> api_gw >> Edge(label="Autentica") >> auth
    api_gw >> Edge(label="Gestiona candidatos") >> candidate_service
    api_gw >> Edge(label="Gestiona trabajos") >> job_service
    api_gw >> Edge(label="Filtra candidatos") >> filtering_service
    filtering_service >> Edge(label="Envía a análisis") >> ia_service
    filtering_service >> Edge(label="Guarda resultados") >> database

    candidate_service >> Edge(label="Accede a datos") >> database
    job_service >> Edge(label="Accede a datos") >> database
    auth_service >> Edge(label="Accede a datos") >> database
