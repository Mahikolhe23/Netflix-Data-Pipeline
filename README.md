# 📌 Netflix Data Pipeline

## Project Overview
The **Netflix Data Pipeline** is designed to efficiently process and analyze Netflix data using Azure services. This pipeline ingests raw CSV data from GitHub and processes it through **Bronze, Silver, and Gold** layers to ensure structured transformation. It leverages **Databricks and Delta Lake** for optimized data storage and processing, while **Synapse Analytics and Power BI** enable real-time analysis and reporting.

---

## 📂 Architecture & Data Flow

### 1️⃣ Data Ingestion (Bronze Layer)
- **Source:** Raw Netflix dataset (CSV) stored in GitHub.
- **Storage:** Azure Data Lake Storage (**ADLS Gen2**) with separate containers (raw, bronze, silver, gold).
- **Processing Tool:** Azure Data Factory (**ADF**) orchestrates data movement.
- **Pipeline Workflow:**
  - A **ForEach loop** dynamically processes files from GitHub.
  - The loop extracts `file_name` and `folder_name` to copy data from GitHub to **Bronze Layer** in ADLS Gen2.
  - The folder structure in Bronze mirrors the GitHub repository.

### 2️⃣ Data Processing (Silver Layer)
- **Transformation:** Databricks & PySpark perform data cleansing and normalization.
- **Storage Format:** Delta Lake for efficient querying and version control.
- **Workflow:**
  - **Auto Loader** is used for incremental data loading (single file processing).
  - Other files are read from the **Bronze Layer**, cleaned, and written to the **Silver Layer**.

### 3️⃣ Data Aggregation (Gold Layer)
- **Aggregation & Business Logic:** Additional transformations in Databricks.
- **Storage:** Synapse Analytics stores processed data for querying.
- **Workflow:**
  - **Databricks Delta Live Tables (DLT)** processes and loads data into **Gold Layer**.

### 4️⃣ Data Visualization & Reporting
- **Analysis:** Synapse Analytics enables querying via SQL Pools.
- **Reporting:** Power BI dashboards provide real-time insights and trend analysis.

---

## 🛠️ Technologies Used
- **Azure Data Lake Storage (ADLS Gen2)** – Storing raw & processed data
- **Azure Data Factory (ADF)** – Orchestrating data movement
- **Azure Databricks** – Transforming and optimizing data using PySpark
- **Unity Catalog Access Control** – Secure access to ADLS from Databricks
- **Delta Lake** – Ensuring efficient data storage and versioning
- **Azure Synapse Analytics** – Querying processed data
- **Power BI** – Visualizing and analyzing insights

---

## 🚀 Implementation Steps
1. **Set up ADLS Gen2**: Create storage containers (raw, bronze, silver, gold).
2. **Configure ADF Pipelines**: Automate data ingestion from GitHub to ADLS using a **ForEach loop** for dynamic copying.
3. **Implement Access Control**:
   - **Databricks cannot directly access ADLS**.
   - Created **access_unity_catalog**, enabling Databricks workspace to securely access ADLS.
4. **Develop Databricks Notebooks**: Implement ETL logic for data transformation.
5. **Enable Delta Lake**: Optimize storage and versioning of processed data.
6. **Load Data into Synapse Analytics**: Store structured data for querying.
7. **Create Power BI Reports**: Design dashboards for trend analysis.

---

## 🔍 Key Features
✅ **Automated Data Ingestion**: Seamless integration with GitHub and Azure.
✅ **Layered Data Processing**: Organized Bronze, Silver, Gold data architecture.
✅ **Optimized Querying**: Fast analytics using Delta Lake & Synapse SQL Pools.
✅ **Secure Access Control**: Databricks access to ADLS via Unity Catalog.
✅ **Interactive Dashboards**: Real-time insights via Power BI.

---

## 📈 Expected Outcomes
📊 **Improved data organization** with layered architecture.
⚡ **Faster query performance** using optimized storage.
📡 **Real-time insights** into Netflix viewing patterns.

---

## 📌 Future Enhancements
🔹 **Integrate Azure Machine Learning** for predictive analytics.
🔹 **Implement real-time streaming** using Azure Event Hubs.
🔹 **Expand dataset sources** to include additional streaming platforms.

---

## 🏗️ Repository Structure
```
netflix-pipeline/
│── adf-pipeline/        # ADF JSON pipeline configuration
│── db-workspace/        # Databricks workspace DBC files
│── netflix-datasets/    # Source CSV files from GitHub
│── python-scripts/      # PySpark notebooks for ETL processing
```

---

## 🏗️ Setup & Deployment
To deploy this project, follow these steps:
1. Clone the **GitHub repository** containing the raw Netflix dataset.
2. Set up **Azure resources** (ADLS, ADF, Databricks, Synapse).
3. Configure **ADF pipelines** to ingest data from GitHub.
4. Develop and execute **Databricks ETL notebooks**.
5. Implement **Unity Catalog** for secure access between Databricks and ADLS.
6. Query processed data using **Synapse SQL Pools**.
7. Connect **Power BI to Synapse** for visualization.

---

## 📧 Contact
For any queries or improvements, feel free to reach out! 

💡 Contributions are welcome! If you have suggestions, submit a PR. 🚀

