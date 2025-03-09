from datetime import datetime as dt
from pathlib import Path
from typing import Any

import click

from pipelines import (
    colect_rolaw_data,
    compute_rag_vector_index,
    etl,
    etl_precomputed,
    generate_dataset,
)


@click.command(
    help="""
RO Law AI CLI v0.0.1. 

Main entry point for the pipeline execution. 
This entrypoint is where everything comes together.

Run the ZenML RO Law AI project pipelines with various options.

Run a pipeline with the required parameters. This executes
all steps in the pipeline in the correct order using the orchestrator
stack component that is configured in your active ZenML stack.

Examples:

  \b
  # Run the pipeline with default options
  python run.py
               
  \b
  # Run the pipeline without cache
  python run.py --no-cache
  
  \b
  # Run only the RO Law data collection pipeline
  python run.py --run-collect-rolaw-data

"""
)
@click.option(
    "--no-cache",
    is_flag=True,
    default=False,
    help="Disable caching for the pipeline run.",
)
@click.option(
    "--run-collect-rolaw-data-pipeline",
    is_flag=True,
    default=False,
    help="Whether to run the collection data from RO Law pipeline.",
)
@click.option(
    "--run-etl-pipeline",
    is_flag=True,
    default=False,
    help="Whether to run the ETL pipeline.",
)
@click.option(
    "--run-etl-precomputed-pipeline",
    is_flag=True,
    default=False,
    help="Whether to run the ETL precomputed pipeline.",
)
@click.option(
    "--run-generate-dataset-pipeline",
    is_flag=True,
    default=False,
    help="Whether to run the generate dataset pipeline.",
)
@click.option(
    "--run-compute-rag-vector-index-huggingface-contextual-simple-pipeline",
    is_flag=True,
    default=False,
    help="Whether to run the compute RAG vector index pipeline with the Hugging Face Dedicated Endpoint, Hugging Faceembedding model in simple contextual retrieval mode.",
)
@click.option(
    "--run-compute-rag-vector-index-openai-contextual-simple-pipeline",
    is_flag=True,
    default=False,
    help="Whether to run the compute RAG vector index pipeline with the OpenAI API, embedding model in simple contextual retrieval mode.",
)
@click.option(
    "--run-compute-rag-vector-index-openai-contextual-pipeline",
    is_flag=True,
    default=False,
    help="Whether to run the compute RAG vector index pipeline with the OpenAI API, embedding model in contextual retrieval mode.",
)
@click.option(
    "--run-compute-rag-vector-index-openai-parent-pipeline",
    is_flag=True,
    default=False,
    help="Whether to run the compute RAG vector index pipeline with the OpenAI API, embedding model in parent retrieval mode.",
)
def main(
    no_cache: bool = False,
    run_colect_rolaw_data_pipeline: bool = False,
    run_etl_pipeline: bool = False,
    run_etl_precomputed_pipeline: bool = False,
    run_generate_dataset_pipeline: bool = False,
    run_compute_rag_vector_index_huggingface_contextual_simple_pipeline: bool = False,
    run_compute_rag_vector_index_openai_contextual_simple_pipeline: bool = False,
    run_compute_rag_vector_index_openai_contextual_pipeline: bool = False,
    run_compute_rag_vector_index_openai_parent_pipeline: bool = False,
) -> None:
    assert (
        run_colect_rolaw_data_pipeline
        or run_etl_pipeline
        or run_etl_precomputed_pipeline
        or run_generate_dataset_pipeline
        or run_compute_rag_vector_index_huggingface_contextual_simple_pipeline
        or run_compute_rag_vector_index_openai_contextual_simple_pipeline
        or run_compute_rag_vector_index_openai_contextual_pipeline
        or run_compute_rag_vector_index_openai_parent_pipeline
    ), "Please specify an action to run."

    pipeline_args: dict[str, Any] = {
        "enable_cache": not no_cache,
    }
    root_dir = Path(__file__).resolve().parent.parent

    if run_colect_rolaw_data_pipeline:
        run_args = {}
        pipeline_args["config_path"] = root_dir / "configs" / "colect_rolaw_data.yaml"
        assert pipeline_args["config_path"].exists(), (
            f"Config file not found: {pipeline_args['config_path']}"
        )
        pipeline_args["run_name"] = (
            f"colect_rolaw_data_run_{dt.now().strftime('%Y_%m_%d_%H_%M_%S')}"
        )
        colect_rolaw_data.with_options(**pipeline_args)(**run_args)

    if run_etl_pipeline:
        run_args = {}
        pipeline_args["config_path"] = root_dir / "configs" / "etl.yaml"
        assert pipeline_args["config_path"].exists(), (
            f"Config file not found: {pipeline_args['config_path']}"
        )
        pipeline_args["run_name"] = f"etl_run_{dt.now().strftime('%Y_%m_%d_%H_%M_%S')}"
        etl.with_options(**pipeline_args)(**run_args)

    if run_etl_precomputed_pipeline:
        run_args = {}
        pipeline_args["config_path"] = root_dir / "configs" / "etl_precomputed.yaml"
        assert pipeline_args["config_path"].exists(), (
            f"Config file not found: {pipeline_args['config_path']}"
        )
        pipeline_args["run_name"] = (
            f"etl_precomputed_run_{dt.now().strftime('%Y_%m_%d_%H_%M_%S')}"
        )
        etl_precomputed.with_options(**pipeline_args)(**run_args)

    if run_generate_dataset_pipeline:
        run_args = {}
        pipeline_args["config_path"] = root_dir / "configs" / "generate_dataset.yaml"
        assert pipeline_args["config_path"].exists(), (
            f"Config file not found: {pipeline_args['config_path']}"
        )
        pipeline_args["run_name"] = (
            f"generate_dataset_run_{dt.now().strftime('%Y_%m_%d_%H_%M_%S')}"
        )
        generate_dataset.with_options(**pipeline_args)(**run_args)

    if run_compute_rag_vector_index_huggingface_contextual_simple_pipeline:
        run_args = {}
        pipeline_args["config_path"] = (
            root_dir
            / "configs"
            / "compute_rag_vector_index_huggingface_contextual_simple.yaml"
        )
        assert pipeline_args["config_path"].exists(), (
            f"Config file not found: {pipeline_args['config_path']}"
        )
        pipeline_args["run_name"] = (
            f"compute_rag_vector_index_huggingface_contextual_simple_run_{dt.now().strftime('%Y_%m_%d_%H_%M_%S')}"
        )
        compute_rag_vector_index.with_options(**pipeline_args)(**run_args)

    if run_compute_rag_vector_index_openai_contextual_simple_pipeline:
        run_args = {}
        pipeline_args["config_path"] = (
            root_dir
            / "configs"
            / "compute_rag_vector_index_openai_contextual_simple.yaml"
        )
        assert pipeline_args["config_path"].exists(), (
            f"Config file not found: {pipeline_args['config_path']}"
        )
        pipeline_args["run_name"] = (
            f"compute_rag_vector_index_openai_contextual_simple_run_{dt.now().strftime('%Y_%m_%d_%H_%M_%S')}"
        )
        compute_rag_vector_index.with_options(**pipeline_args)(**run_args)

    if run_compute_rag_vector_index_openai_contextual_pipeline:
        run_args = {}
        pipeline_args["config_path"] = (
            root_dir / "configs" / "compute_rag_vector_index_openai_contextual.yaml"
        )
        assert pipeline_args["config_path"].exists(), (
            f"Config file not found: {pipeline_args['config_path']}"
        )
        pipeline_args["run_name"] = (
            f"compute_rag_vector_index_openai_contextual_run_{dt.now().strftime('%Y_%m_%d_%H_%M_%S')}"
        )
        compute_rag_vector_index.with_options(**pipeline_args)(**run_args)

    if run_compute_rag_vector_index_openai_parent_pipeline:
        run_args = {}
        pipeline_args["config_path"] = (
            root_dir / "configs" / "compute_rag_vector_index_openai_parent.yaml"
        )
        assert pipeline_args["config_path"].exists(), (
            f"Config file not found: {pipeline_args['config_path']}"
        )
        pipeline_args["run_name"] = (
            f"compute_rag_vector_index_openai_parent_run_{dt.now().strftime('%Y_%m_%d_%H_%M_%S')}"
        )
        compute_rag_vector_index.with_options(**pipeline_args)(**run_args)


if __name__ == "__main__":
    main()
