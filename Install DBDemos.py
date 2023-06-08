# Databricks notebook source
# MAGIC %pip install dbdemos

# COMMAND ----------

import dbdemos
dbdemos.help()
dbdemos.list_demos()

# COMMAND ----------

dbdemos.install('uc-01-acl')
dbdemos.install('uc-02-external-location')
dbdemos.install('uc-03-data-lineage')
dbdemos.install('uc-04-audit-log')
dbdemos.install('uc-05-upgrade')
