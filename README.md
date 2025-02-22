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

## System Architecture

```mermaid
flowchart TB
    subgraph Users[Users]
    end

    subgraph Frontend[ ]
        direction TB
        WebApp[Web App (React)]
        MobileApp[Mobile App (React Native)]
    end

    subgraph APIGateway[API Gateway (Istio or Kong Gateway)]
    end

    subgraph Backend[ ]
        SemanticSearch[Semantic Search (FastAPI)]
        LLMService[LLM Service (FastAPI)]
        UserService[User Service (FastAPI)]
        AuthService[Auth Service (OAuth 2.0)]
    end

    subgraph DataLayer[Data Layer]
        VectorDB[Vector DB (Pinecone, Weaviate)]
        RelationalDB[Relational DB (PostgreSQL)]
        ObjectStorage[Object Storage (GCP or S3)]
    end

    subgraph Kubernetes[Kubernetes Cluster (GKE, EKS, or AKS)]
    end

    subgraph CICD[CI/CD Pipeline (GitHub Actions)]
    end

    subgraph Monitoring[Monitoring and Logging (Prometheus, Grafana, ELK Stack)]
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
