# to generate test report run this file with the command
# pytest -v -s --alluredir="allure-reports" tests.py
# than run in CLI
# allure serve <PATH to the allure bin directory>


import allure
import pytest
import pypyodbc as odbc

from settings import db_conn as db
from selenium import webdriver

connectionString = db.GetConnectionString()
conn = odbc.connect(connectionString)

cursor = conn.cursor()


def test_check_duplicates_person_address():
    sql_query = """with query AS
                    (SELECT AddressLine1, AddressLine2, City, StateProvinceID, PostalCode, Count(*) CNT
                        FROM [Person].[Address]
                        GROUP BY AddressLine1, AddressLine2, City, StateProvinceID, PostalCode
                        HAVING COUNT(*) > 1)
                SELECT COUNT(*) FROM query"""
    cursor.execute(sql_query)
    row = cursor.fetchone()
    print(row[0])
    assert row[0] == 0


def test_check_future_dates_person_address():
    sql_query = """with query AS
                    (SELECT *
                        FROM [Person].[Address]
                        WHERE ModifiedDate > GETDATE())
                SELECT COUNT(*) FROM query"""
    cursor.execute(sql_query)
    row = cursor.fetchone()
    print(row[0])
    assert row[0] == 0


def test_check_consistency_for_folder_production_documents():
    sql_query = """with query AS
                    (SELECT *
                        FROM [Production].[Document]
                        WHERE FolderFlag = 1
                        AND FileExtension != '')
                SELECT COUNT(*) FROM query"""
    cursor.execute(sql_query)
    row = cursor.fetchone()
    print(row[0])
    assert row[0] == 0


def test_check_below_zero_values_production_documents():
    sql_query = """with query AS
                    (SELECT *
                        FROM [Production].[Document]
                        WHERE DocumentLevel < 0
                        OR Owner < 0
                        OR ChangeNumber < 0
                        OR Status < 0)
                SELECT COUNT(*) FROM query"""
    cursor.execute(sql_query)
    row = cursor.fetchone()
    print(row[0])
    assert row[0] == 0


def test_table_exists_production_unitmeasure():
    sql_query = """with query AS
                    (SELECT * FROM [AdventureWorks2012].[Production].[UnitMeasure] WHERE 1=2)
                SELECT COUNT(*) FROM query"""
    cursor.execute(sql_query)
    row = cursor.fetchone()
    print(row[0])
    assert row[0] == 0


def test_check_duplicates_production_unitmeasure():
    sql_query = """with query AS
                    (SELECT Name column_value, COUNT(*) CNT
                        FROM [Production].[UnitMeasure]
                        GROUP BY Name
                        HAVING COUNT(*) > 1
                        UNION ALL
                        SELECT UnitMeasureCode, COUNT(*) CNT
                        FROM [Production].[UnitMeasure]
                        GROUP BY UnitMeasureCode
                        HAVING COUNT(*) > 1)
                SELECT COUNT(*) FROM query"""
    cursor.execute(sql_query)
    row = cursor.fetchone()
    print(row[0])
    assert row[0] == 0

