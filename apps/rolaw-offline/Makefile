ifeq (,$(wildcard .env))
$(error .env file is missing. Please create one based on .env.example)
endif

include .env

export UV_PROJECT_ENVIRONMENT=.venv-offline
export PYTHONPATH = .

# --- Default Values ---
CHECK_DIRS := .
AWS_S3_BUCKET_NAME := rolaw
ROLAW_LOCAL_DATA_PATH := ./data/


# --- Utilities ---
help:
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done


# --- Infrastructure --- 
local-docker-infrastructure-up:
	docker compose -f ../infrastructure/docker/docker-compose.yml up --build -d 

local-docker-infrastructure-stop:
	docker compose -f ../infrastructure/docker/docker-compose.yml stop

local-zenml-server-up:
ifeq ($(shell uname), Darwin)
	OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES uv run zenml login --local
else
	uv run zenml login --local
endif

local-zenml-server-stop:
	uv run zenml logout --local

local-infrastructure-up: local-docker-infrastructure-up local-zenml-server-stop local-zenml-server-up  # Start MongoDB and ZenML

local-infrastructure-stop: local-docker-infrastructure-stop local-zenml-server-stop  # Stop MongoDB and ZenML


# --- AWS ---
validate_aws_boto3:  # Check AWS credentials
	@echo "Validating AWS Boto3 credentials..."
	uv run python -m tools.validate_aws_boto3

s3-upload-rolaw-dataset:  # Upload rolaw dataset from local folder to S3
	@echo "Uploading rolaw dataset to S3 bucket: $(AWS_S3_BUCKET_NAME)/rolaw/dataset"
	uv run python -m tools.use_s3 upload $(ROLAW_LOCAL_DATA_PATH) $(AWS_S3_BUCKET_NAME) --s3-prefix rolaw/dataset

s3-download-rolaw-dataset:  # Download rolaw dataset from S3 to local folder
	@echo "Downloading rolaw dataset from S3 bucket: $(AWS_S3_BUCKET_NAME)/rolaw/dataset/data.zip"
	uv run python -m tools.use_s3 download $(AWS_S3_BUCKET_NAME) rolaw/dataset/data.zip $(ROLAW_LOCAL_DATA_PATH)

download-rolaw-dataset: s3-download-rolaw-dataset


# --- Offline ML Pipelines ---
collect-rolaw-data-pipeline:
	uv run python -m tools.run --run-collect-rolaw-data-pipeline --no-cache

etl-pipeline:
	uv run python -m tools.run --run-etl-pipeline --no-cache

etl-precomputed-pipeline:
	uv run python -m tools.run --run-etl-precomputed-pipeline --no-cache

generate-dataset-pipeline:
	uv run python -m tools.run --run-generate-dataset-pipeline --no-cache

compute-rag-vector-index-huggingface-contextual-simple-pipeline:
	uv run python -m tools.run --run-compute-rag-vector-index-huggingface-contextual-simple-pipeline --no-cache

compute-rag-vector-index-openai-contextual-simple-pipeline:
	uv run python -m tools.run --run-compute-rag-vector-index-openai-contextual-simple-pipeline --no-cache

compute-rag-vector-index-openai-contextual-pipeline:
	uv run python -m tools.run --run-compute-rag-vector-index-openai-contextual-pipeline --no-cache

compute-rag-vector-index-openai-parent-pipeline:
	uv run python -m tools.run --run-compute-rag-vector-index-openai-parent-pipeline --no-cache

delete-rag-collection:
	uv run python -m tools.delete_rag_collection
