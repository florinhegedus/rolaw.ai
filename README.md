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
          +-----------------------------------------------------------+
          |                          Users                            |
          +---------------------+--------------------------+----------+
                                |                          |
                             Web App                   Mobile App
                              (React)                    (React Native)
                                |                          |
          +---------------------v--------------------------v----------+
          |                        API Gateway                        |
          |                  (Istio or Kong Gateway)                  |
          +------------+------------+------------+------------+-------+
                       |            |            |            |
                       |            |            |            |
                       v            v            v            v
                Semantic Search   LLM Service   User Service   Auth Service
                  (FastAPI)         (FastAPI)      (FastAPI)      (OAuth 2.0)
                       |            |            |            |
                       |            |            |            |
          +------------v------------+------------v------------+---------+
          |                           Data Layer                        |
          |            +--------------+--------------+                  |
          |            |                             |                  |
          |      Vector Database                Relational Database     |
          |        (Pinecone,                      (PostgreSQL)         |
          |        Weaviate)                                            |
          +-------------------------------+-----------------------------+
                                          |
                                   Object Storage
                                  (GCP Storage or S3)
                                          |
                                  Legal Document Corpus
                            (Raw text, PDFs, JSON, etc.)
                                          |
                              +------------v------------+
                              |      Kubernetes Cluster |
                              | (GKE, EKS, or AKS)      |
                              +-------------------------+
                                          |
                                 CI/CD Pipeline (GitHub Actions)
                                          |
                                  Monitoring and Logging
                              (Prometheus, Grafana, ELK Stack)

