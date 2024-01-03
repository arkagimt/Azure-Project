# Data-Integration-and-Analytics-Pipeline

# Overview

This project establishes a comprehensive data processing pipeline leveraging Azure services to orchestrate the flow of data from multiple sources to a data lake, perform transformations, and finally publish the cleansed data for reporting and alerting purposes. The architecture facilitates continuous integration and delivery (CI/CD) practices to maintain and scale the solution efficiently.

# Architecture

The architecture follows a multi-stage process:

- **Data Ingestion**: Various data sources including CSV files, SQL databases, APIs, PDF documents, and Excel files are ingested into the pipeline.
- **Processing with Azure Data Factory**: The ingested data is then pipelined through Azure Data Factory for initial processing and routed to a RAW Data Lake.
- **Transformation with Azure Databricks**: Azure Databricks takes over to perform more complex transformations and data cleansing operations.
- **Data Storage**: Post-transformation, the data is stored in two forms:
    - A cleansed version in a data mart for further analytics.
    - A published version in Azure SQL for accessibility and visualization.
- **Reporting**: The transformed data is connected to Power BI, providing a platform for building interactive reports and dashboards.
- **Alerting with Azure Logic Apps**: Finally, Azure Logic Apps are set up to trigger alerts and notifications based on specified events or conditions.

# Architecture Diagram
![Architecture Diagram](https://github.com/DataThread/DataFlow-Analytics-Engine/blob/096b13fd62139dc9b003b5d991e5d336f0567a8e/Architectre.PNG)

# Components

- **Azure Data Factory**: Orchestrates and automates the movement and transformation of data.
- **Azure Databricks**: Provides a collaborative environment with scalable resources for big data processing and machine learning.
- **Azure SQL Database**: Hosts the published data, ready for consumption by reporting tools.
- **Power BI**: Serves as the visualization tool to create reports and dashboards.
- **Azure Logic Apps**: Manages communication and alerting mechanisms via email or other channels.

# Data Flow

1. Data is ingested from multiple source formats.
2. RAW data is stored in categories such as Flights, Plane, Airport, Cancellation, Airlines, and Unique Carriers.
3. Data is cleansed, transformed, and stored in a data mart.
4. The data is then published to Azure SQL.
5. Power BI connects to Azure SQL to fetch data for reports.
6. Azure Logic Apps monitors the data pipeline and sends notifications as needed.

# Usage

This pipeline is designed to be adaptable for various data processing needs. It can be cloned and configured according to the specific requirements of different data sources and business logic.


