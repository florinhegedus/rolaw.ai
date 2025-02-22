# rolaw.ai
Gather all Romanian laws and build a RAG system.

## Consulted documents
The system has access to the following:
- Codul Civil
- Codul Penal
- Codul de Procedură Civilă
- Codul de Procedură Penală

Auxiliary material to be checked in the future:
- Codul Muncii
- Codul Fiscal
- Legea Contenciosului Administrativ
- Legea Protecției Datelor
- Legea Societăților Comerciale
- Legea Educației Naționale
- Legea Sănătății
- Legea privind comerțul electronic
- Hotărâri de Guvern (HG) și Ordonanțe de Urgență (OUG)
- Regulamente locale

## Architecture overview
## System Architecture

```mermaid
flowchart TB
    subgraph Users[Users]
    end

    subgraph Frontend[ ]
        direction TB
        WebApp[Web App<br>(React)]
        MobileApp[Mobile App<br>(React Native)]
    end

    subgraph APIGateway[API Gateway<br>(Istio or Kong Gateway)]
    end

    subgraph Backend[ ]
        SemanticSearch[Semantic Search<br>(FastAPI)]
        LLMService[LLM Service<br>(FastAPI)]
        UserService[User Service<br>(FastAPI)]
        AuthService[Auth Service<br>(OAuth 2.0)]
    end

    subgraph DataLayer[Data Layer]
        VectorDB[Vector Database<br>(Pinecone, Weaviate)]
        RelationalDB[Relational Database<br>(PostgreSQL)]
        ObjectStorage[Object Storage<br>(GCP Storage or S3)]
    end

    subgraph Kubernetes[Kubernetes Cluster<br>(GKE, EKS, or AKS)]
    end

    subgraph CICD[CI/CD Pipeline<br>(GitHub Actions)]
    end

    subgraph Monitoring[Monitoring and Logging<br>(Prometheus, Grafana, ELK Stack)]
    end

    Users --> Frontend
    Frontend --> APIGateway
    APIGateway --> Backend
    Backend --> DataLayer
    DataLayer --> ObjectStorage
    ObjectStorage --> Kubernetes
    Kubernetes --> CICD
    CICD --> Monitoring
```
