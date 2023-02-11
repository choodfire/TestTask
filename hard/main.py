import json
import os
import psycopg2
import requests
from dotenv import load_dotenv


def connect_to_db():
    load_dotenv()

    conn = 0
    dbname = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')

    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    except Exception as e:
        print(e)

    return conn

def get_data(url: str, query: str, inner_dict: str): # inner_dict - название внутреннего словаря, надо чтоб вернуть только лист
    response = requests.post(url, json={'query': query})
    data = json.loads(response.text)

    return data['data'][inner_dict]

def insert_into_rockets(cursor, rockets):
    for rocket in rockets:
        cursor.execute("INSERT INTO rocket (id, description, name, active, company, first_flight) "
                       "VALUES(%s, %s, %s, %s, %s, %s)",
                       (rocket['id'], rocket['description'], rocket['name'],
                        rocket['active'], rocket['company'], rocket['first_flight']))

def insert_into_launches(cursor, launches):
    for launch in launches:
        cursor.execute("INSERT INTO launch (id, mission_id, rocket_id, upcoming, launch_success, launch_date_unix) "
                       "VALUES(%s, %s, %s, %s, %s, %s)",
                       (launch['id'], launch['mission_id'], launch['rocket']['rocket']['id'],
                        launch['upcoming'], launch['launch_success'], launch['launch_date_utc']))

def main():
    url = 'https://spacex-production.up.railway.app/'
    rocket_query = """query RocketsQuery {
          rockets {
            id
            name
            description
            active
            company
            first_flight
          }
        }"""
    launch_query = """query LaunchesQuery {
      launches {
        id
        rocket {
          rocket {
            id
          }
        }
        upcoming
        launch_success
        mission_id
        launch_date_utc
      }
    }"""
    rockets = get_data(url, rocket_query, 'rockets')
    launches = get_data(url, launch_query, 'launches')
    conn = connect_to_db()
    cursor = conn.cursor()

    insert_into_rockets(cursor, rockets)
    insert_into_launches(cursor, launches)
    conn.commit()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()