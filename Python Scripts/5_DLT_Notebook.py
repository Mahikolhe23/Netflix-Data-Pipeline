# Databricks notebook source
# MAGIC %md
# MAGIC # DLT NOTEBOOK - GOLD LAYER

# COMMAND ----------

looktables_rules = {
    'rule1':'showid is NOT NULL'
}


# COMMAND ----------

# Step 1️⃣: Check if `dlt` module is installed correctly
try:
    import dlt
    print("✅ 'dlt' module found.")
    print("📌 dlt module path:", dlt.__file__)
except ImportError:
    print("❌ 'dlt' module NOT found. Make sure you are in a Delta Live Tables pipeline.")
    exit()

# Step 2️⃣: Check available functions in `dlt` module
dlt_functions = dir(dlt)
print("🔍 Available functions in 'dlt':", dlt_functions)

if "table" not in dlt_functions:
    print("❌ 'dlt.table' not found. Likely, you installed the wrong package.")
    print("⚠️ Uninstalling incorrect `dlt` package...")
    !pip uninstall -y dlt
    print("✅ Uninstalled. Now, restart your cluster and run inside a Delta Live Tables pipeline.")
    exit()

# Step 3️⃣: Check Python version (Databricks Runtime)
import sys
print("🐍 Python version:", sys.version)

# Step 4️⃣: Verify Databricks Runtime
try:
    dbutils.library.restartPython()
    print("✅ Databricks cluster restarted.")
except:
    print("⚠️ Warning: Could not restart Databricks cluster. Do it manually.")

# Step 5️⃣: Check if running inside a Delta Live Tables pipeline
import os
is_dlt = os.environ.get("DATABRICKS_RUNTIME_VERSION", "") != ""

if not is_dlt:
    print("❌ ERROR: You are NOT running inside a Delta Live Tables pipeline.")
    print("➡️ Go to Databricks UI > Workflows > Delta Live Tables > Create Pipeline.")
    exit()
else:
    print("✅ Running inside a Delta Live Tables pipeline.")

# Step 6️⃣: Test a simple Delta Live Table function
import dlt
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DLT Test").getOrCreate()

@dlt.table(
    name="test_table"
)
def test_function():
    return spark.createDataFrame([(1, "Alice"), (2, "Bob")], ["id", "name"])

print("✅ Successfully created `test_table` using dlt.table.")


# COMMAND ----------

