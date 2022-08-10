# adludio-DE-challenge

## Overview

Adludio is an online moblile Ad Business that designs an interactive Ad and serves these creatives to audiences on behalf of a client. In this project linking of related data from multiple sources will be implemented.

**Table of content**

- [Overview](#overview)
- [Install](#install)
- [Data](#data)
- [Tech-Stack](#tech-Stack)
- [Description](#description)



## Install

```
git clone https://github.com/meriab21/adludio-DE-challenge.git
cd adludio-DE-challenge
pip install -r requirements.txt
```
     cd airflow
     
     docker-compose up 

    

## Data

Please find the data sources in the dataset folder attached.
- Design data ( global_design_data.json): 
    This data is found by analyzing the advertisements using computer vision. It constitutes the ad-unit components. Note that the unique identifier in this data is game_key

- Campaigns data (campaigns_inventory.csv) 
    Campaign historical performance dataset. It contains historical inventories of the campaign created placed and also KPI events associated with it. The type column is the one you will find the KPI events. 

- Briefs data (briefing.csv)
    Campaign & creative plan data. 

- Creative Assets(Creative_assets_) Zipped File
    The data contains images for particular game keys. Use computer vision to extract features that enrich the already existing features in design data. Hint: The naming convention of the images(to identify the game key), change ‘-’ to ‘/’.


## Tech-Stack
Tech Stack used in this project

-   [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/)
-   [PostgreSQL](https://dev.PostgreSQL.com/doc/)
-   [dbt](https://docs.getdbt.com/)


## Description

The data engineering tasks of the challenge are to link related data from multiple data sources into single   table, ingestion of the given raw data into data lake and building ETL pipleline to enrich data into data   warehouse.

The ML Engineering tasks of the challenge are to  develop a Machine Learning framework in a modular way to determine the KPI likelihood (engagement & click) of an impression given its inventory, brief, and creative design components. The main goal of the task is to explore Natural language processing, computer vision and machine learning techniques to tackle the problem. Use the dataset you used for the above task & implement the ML pipeline that takes the three (Brief, Campaign & Design) datasets and applies suitable machine learning techniques to predict KPI likelihood.

## Author

- 👤 **Meron Abate**
- meriab1234@gmail.com


