from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.database import RDS, Dynamodb
from diagrams.aws.network import APIGateway
from diagrams.aws.storage import S3
from diagrams.aws.security import Cognito
from diagrams.aws.analytics import Quicksight, Glue
from diagrams.aws.management import Cloudwatch
from diagrams.aws.integration import SQS, SNS
from diagrams.onprem.client import Users
from diagrams.programming.framework import React

with Diagram("ATS de LTI - Arquitectura en AWS", show=False):

    users = Users("Usuarios")

    with Cluster("Frontend"):
        frontend = React("Aplicación Web")

    with Cluster("Backend"):
        api_gw = APIGateway("API Gateway")
        auth = Cognito("Autenticación")
        with Cluster("Microservicios"):
            services = [Lambda("Servicio 1"),
                        Lambda("Servicio 2"),
                        Lambda("Servicio 3")]

    with Cluster("Base de Datos"):
        rds = RDS("Amazon RDS")
        dynamo = Dynamodb("Amazon DynamoDB")

    with Cluster("Almacenamiento"):
        storage = S3("Amazon S3")

    with Cluster("Mensajería y Colas"):
        sqs = SQS("Amazon SQS")
        sns = SNS("Amazon SNS")

    with Cluster("Analítica y Reporting"):
        quicksight = Quicksight("AWS QuickSight")
        glue = Glue("AWS Glue")

    with Cluster("Monitorización y Logging"):
        cloudwatch = Cloudwatch("Amazon CloudWatch")

    users >> frontend >> api_gw >> services
    api_gw >> auth
    services >> rds
    services >> dynamo
    services >> storage
    services >> sqs
    sqs >> sns
    services >> cloudwatch
    services >> quicksight
    services >> glue
