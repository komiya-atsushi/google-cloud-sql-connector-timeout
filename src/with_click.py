import logging
import os

import click
import pymysql
import sqlalchemy
from google.cloud.sql.connector import connector

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT, level='DEBUG')


def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        os.getenv("CONNECTION_NAME"),
        "pymysql",
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        db=os.getenv("DATABASE_NAME"),
    )
    return conn


@click.command()
def main() -> None:
    pool = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=getconn,
    )

    with pool.connect() as conn:
        result = conn.execute(sqlalchemy.text("select 1")).fetchall()

        for row in result:
            print(row)

    print("Done.")


if __name__ == "__main__":
    main()
