graph LR
  frontend(Frontend)
  api(API Gateway)
  microservice1[(DB1)]
  microservice2[(DB2)]
  microservice3[(DB3)]
  aws(AWS)
  lb[(Load Balancer)]
  cdn[(CDN)]

  frontend -- API request --> api
  api -- query DB1 --> microservice1
  api -- query DB2 --> microservice2
  api -- query DB3 --> microservice3
  microservice1 -- data --> microservice2
  microservice2 -- data --> microservice3
  api -- fetch data --> frontend
  aws -- host services --> frontend
  aws -- manage traffic --> lb
  lb -- distribute --> microservice1
  lb -- distribute --> microservice2
  lb -- distribute --> microservice3
  cdn -- cache assets --> frontend