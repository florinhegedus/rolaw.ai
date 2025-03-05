ifeq (,$(wildcard .env))
$(error .env file is missing. Please create one based on .env.example)
endif

include .env

export UV_PROJECT_ENVIRONMENT=.venv-offline
export PYTHONPATH = .

# --- Utilities ---
help:
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

# --- Infrastructure --- 
local-docker-infrastructure-up:  # start mongodb docker container
	docker compose -f ../infrastructure/docker/docker-compose.yml up --build -d 

local-docker-infrastructure-stop:  # stop mongodb docker container
	docker compose -f ../infrastructure/docker/docker-compose.yml stop
