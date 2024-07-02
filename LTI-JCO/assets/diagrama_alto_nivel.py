from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS, DynamodbTable
from diagrams.aws.network import ELB, Route53, VPC
from diagrams.aws.security import IAM, WAF
from diagrams.aws.management import Cloudwatch
from diagrams.aws.integration import SQS
from diagrams.aws.ml import Sagemaker
from diagrams.aws.storage import S3

with Diagram("High-Level ATS Architecture", show=False):
    with Cluster("VPC"):
        with Cluster("Public Subnet"):
            lb = ELB("Load Balancer")
            web_server = EC2("Web Server")

        with Cluster("Private Subnet"):
            app_server = EC2("Application Server")
            db = RDS("Relational Database")
            nosql_db = DynamodbTable("NoSQL Database")
            ml_model = Sagemaker("ML Model")

        with Cluster("Storage"):
            storage = S3("CV Storage")

        queue = SQS("Task Queue")
        monitoring = Cloudwatch("Monitoring")

    dns = Route53("DNS")
    firewall = WAF("Web Application Firewall")
    iam = IAM("IAM Roles")

    dns >> firewall >> lb >> web_server >> app_server
    app_server >> db
    app_server >> nosql_db
    app_server >> ml_model
    app_server >> storage
    app_server >> queue
    monitoring >> app_server
    monitoring >> db
    monitoring >> nosql_db
    monitoring >> ml_model
