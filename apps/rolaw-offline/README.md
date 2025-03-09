# 🚀 Installation and Usage Guide for the RO Law AI Module

This guide will help you set up and run the RO Law AI Module.


# 📑 Table of Contents

- [📋 Prerequisites](#-prerequisites)
- [🎯 Getting Started](#-getting-started)
- [📁 Project Structure](#-project-structure)
- [🏗️ Set Up Your Local Infrastructure](#-set-up-your-local-infrastructure)
- [⚡️ Running the Code](#️-running-the-code)
- [🔧 Utlity Commands](#-utility-commands)

# 📋 Prerequisites

## Local Tools

For all the modules, you'll need the following tools installed locally:

| Tool | Version | Purpose | Installation Link |
|------|---------|---------|------------------|
| Python | 3.11 | Programming language runtime | [Download](https://www.python.org/downloads/) |
| uv | ≥ 0.4.30 | Python package installer and virtual environment manager | [Download](https://github.com/astral-sh/uv) |
| GNU Make | ≥ 3.81 | Build automation tool | [Download](https://www.gnu.org/software/make/) |
| Git | ≥2.44.0 | Version control | [Download](https://git-scm.com/downloads) |
| Docker | ≥27.4.0 | Containerization platform | [Download](https://www.docker.com/get-started/) |

## Cloud Services

Also, the repository requires access to these cloud services. The authentication to these services is done by adding the corresponding environment variables to the `.env` file:

| Service | Purpose | Cost | Environment Variable | Setup Guide | Starting with Module |
|---------|---------|------|---------------------|-------------| ---------------------|
| [OpenAI API](https://openai.com/index/openai-api/) | LLM API | Pay-per-use | `OPENAI_API_KEY` | [Quick Start Guide](https://platform.openai.com/docs/quickstart) | Module 2 |
| [Hugging Face](https://huggingface.com/) | MLOps | Free tier | `HUGGINGFACE_ACCESS_TOKEN` | [Quick Start Guide](https://huggingface.co/docs/hub/en/security-tokens) | Module 3 |
| [Comet ML](https://rebrand.ly/second-brain-course-comet)  | Experiment tracking |  Free tier | `COMET_API_KEY` | [Quick Start Guide](https://rebrand.ly/second-brain-course-comet-quickstart) | Module 4 |
| [Opik](https://rebrand.ly/second-brain-course-opik) | LLM evaluation and prompt monitoring | Free tier  | `COMET_API_KEY` | [Quick Start Guide](https://rebrand.ly/second-brain-course-comet-quickstart) | Module 6 |

When working locally, the infrastructure is set up using Docker. Thus, you can use the default values found in the `config.py` for all the infrastructure-related environment variables.

But, in case you want to deploy the code, you'll need to setup the following services with their corresponding environment variables:

| Service | Purpose | Cost | Required Credentials | Setup Guide |
|---------|---------|------|---------------------|-------------| 
| [MongoDB](https://rebrand.ly/second-brain-course-mongodb) | NoSQL and vector database | Free tier | `MONGODB_URI` | 1. [Create a free MongoDB Atlas account](https://rebrand.ly/second-brain-course-mongodb-setup-1) <br> 2. [Create a Cluster](https://rebrand.ly/second-brain-course-mongodb-setup-2) </br> 3. [Add a Database User](https://rebrand.ly/second-brain-course-mongodb-setup-3) </br> 4. [Configure a Network Connection](https://rebrand.ly/second-brain-course-mongodb-setup-4) |

# 🎯 Getting Started

## 1. Clone the Repository

Start by cloning the repository and navigating to the project directory:
```
git clone https://github.com/florinhegedus/rolaw.ai.git
cd rolaw.ai
```

## 2. Installation

First deactivate any active virtual environment and move to the `rolaw-offline` directory:
```bash
deactivate
cd apps/rolaw-offline
```

To install the dependencies and activate the virtual environment, run the following commands:

```bash
uv venv .venv-offline
. ./.venv-offline/bin/activate # or source ./.venv-offline/bin/activate
uv pip install -e .
```

## 3. Environment Configuration

Before running any command, you have to set up your environment:
1. Create your environment file:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and configure the required credentials following the inline comments and the recommendations from the [Cloud Services](#-prerequisites) section.

## 4. Setup AWS
For using AWS, you need to have an AWS account.
1. From AWS Console Home, go to `IAM` -> `Access Management` -> `Users` -> `Create user`. 
2. Add `AmazonS3FullAccess` permission to the user.
3. Create an access key for the user.
4. In terminal, run `aws configure` and paste the access key and secret access key.


# 📁 Project Structure

The repo follows the structure of a real-world Python project:

```bash
.
├── configs/                   # ZenML configuration files
├── pipelines/                 # ZenML ML pipeline definitions
├── src/rolaw_offline/         # Main package directory
│   ├── application/           # Application layer
│   ├── domain/                # Domain layer
│   ├── infrastructure/        # Infrastructure layer
│   ├── config.py              # Configuration settings
│   └── utils.py               # Utility functions
├── steps/                     # ZenML pipeline steps
├── tests/                     # Test files
├── tools/                     # Entrypoint scripts that use the Python package
├── .env.example               # Environment variables template
├── .python-version            # Python version specification
├── Makefile                   # Project commands
└── pyproject.toml             # Project dependencies
```

# 🏗️ Set Up Your Local Infrastructure

We use Docker to set up the local infrastructure (MongoDB).

> [!WARNING]
> Before running the command below, ensure you do not have any processes running on port `27017` (MongoDB).

To start it, run:
```bash
make local-infrastructure-up
```

To stop it, run:
```bash
make local-infrastructure-stop
```

> [!NOTE]
> To visualize the raw and RAG data from MongoDB, we recommend using [MongoDB Compass](https://www.mongodb.com/products/tools/compass) or Mongo's official IDE plugin (e.g., `MongoDB for VS Code`). To connect to the working MongoDB instance, use the `MONGODB_URI` value from the `.env` file or found inside the [config.py](src/rolaw_offline/config.py) file.

# ⚡️ Running the Code

## ETL pipeline

### Prepare RO Law data

Download our prepared RO Law dataset from S3 (recommended):
```bash
make download-rolaw-dataset
# Validate using test: make test-download-notion-dataset
```
### Run the ETL pipeline

Run the ETL pipeline to crawl, score and ingest the rolaw data into MongoDB:
```bash
make etl-pipeline
```
Running criteria:
- Running costs: ~$0.5
- Running time: ~30 minutes
