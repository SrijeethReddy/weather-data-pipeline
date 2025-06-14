Weather Data Pipeline

An end-to-end data engineering project that collects real-time weather data, processes it, and enables analytics.

Project Overview

This project builds a data pipeline to:





Ingest weather data from OpenWeatherMap API.



Store raw data in a data lake (local storage or MinIO).



Transform data using PySpark.



Load processed data into PostgreSQL.



Schedule workflows with Apache Airflow.



Visualize insights with Metabase.

Tech Stack





Ingestion: Python (requests)



Processing: PySpark



Storage: Local file system/MinIO, PostgreSQL



Orchestration: Apache Airflow



Visualization: Metabase



Containerization: Docker



Version Control: Git/GitHub

Setup Instructions

(Work in progress: Detailed setup instructions will be added as the project develops.)

Folder Structure

weather-data-pipeline/
├── dags/                # Airflow DAGs
├── scripts/             # Python scripts for ingestion/processing
├── configs/             # Configuration files
├── data/                # Local data lake storage
├── README.md

License

MIT