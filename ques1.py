"""
importing mysql connector to establish connection with sql server
"""
# pylint: disable=broad-except,import-error
import mysql.connector

def execute_query_to_point_table():
    """"Execute sql query to  point employee_details table"""

    MY_CURSOR.execute("select * from employee_details")


def get_ten_records_of_employee_details_of_table():
    """"
    Implementation of generator function ,Returning 10 records each time using Yield
    """
    while True:
        many_records = MY_CURSOR.fetchmany(10)
        if many_records:
            yield many_records

        else:
            break

def print_each_record_list_wise(many_records):
    """" printing one by one records from 10 records"""
    for record in many_records:
        print(list(record))
if __name__ == "__main__":
    try:
        MY_DB = mysql.connector.connect(host="localhost", user="root", password="123@abc#", database="employee_schema")
        MY_CURSOR = MY_DB.cursor()
        execute_query_to_point_table()
        for records in get_ten_records_of_employee_details_of_table():
            print_each_record_list_wise(records)

    except Exception as exception_name:
        print(exception_name)
    finally:
        MY_CURSOR.close()
        MY_DB.close()
