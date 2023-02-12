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


def get_data(url: str, query: str,
             inner_dict: str):  # inner_dict - название внутреннего словаря, надо чтоб вернуть только лист
    response = requests.post(url, json={'query': query})
    data = json.loads(response.text)

    return data['data'][inner_dict]


def insert_into_publications(cursor, item, category: str) -> int:
    cursor.execute("INSERT INTO publication (category, article_link, presskit, reddit_campaign, reddit_launch, "
                   "reddit_media, reddit_recovery, wikipedia, website) "
                   "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id",
                   (category, item.get('article_link', None), item.get('presskit', None),
                    item.get('reddit_campaign', None), item.get('reddit_launch', None),
                    item.get('reddit_media', None), item.get('reddit_recovery', None),
                    item.get('wikipedia', None), item.get('website', None)))

    new_row_id = -1

    try:
        new_row_id = cursor.fetchone()
    except Exception:
        return None

    return new_row_id[0]  # id of new row

def insert_into_missions(cursor, missions):
    for mission in missions:
        publication_id = insert_into_publications(cursor, mission, 'mission')

        cursor.execute("INSERT INTO mission (id, description, name, publication) VALUES(%s, %s, %s, %s)",
                       (mission['id'], mission['description'], mission['name'], publication_id))


def insert_into_rockets(cursor, rockets):
    for rocket in rockets:
        publication_id = insert_into_publications(cursor, rocket, 'rocket')

        cursor.execute("INSERT INTO rocket (id, description, name, active, company, first_flight, publication) "
                       "VALUES(%s, %s, %s, %s, %s, %s, %s)",
                       (rocket['id'], rocket['description'], rocket['name'],
                        rocket['active'], rocket['company'], rocket['first_flight'], str(publication_id)))


def insert_into_launches(cursor, launches):
    for launch in launches:
        publication_id = insert_into_publications(cursor, launch['links'], 'launch')

        cursor.execute("INSERT INTO launch (id, mission_id, rocket_id, upcoming, launch_success, launch_date_unix, publication)"
                       "VALUES(%s, %s, %s, %s, %s, %s, %s)",
                       (launch['id'], launch['mission_id'], launch['rocket']['rocket']['id'],
                        launch['upcoming'], launch['launch_success'], launch['launch_date_utc'], publication_id))


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
        wikipedia
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
        links {
          article_link
          presskit
          reddit_campaign
          reddit_launch
          reddit_media
          reddit_recovery
          wikipedia
        }
        upcoming
        launch_success
        mission_id
        launch_date_utc
      }
    }"""
    missions_query = """query MissionsQuery {
      missions {
        id
        description
        name
        website
        wikipedia
      }
    }"""
    rockets = get_data(url, rocket_query, 'rockets')
    missions = get_data(url, missions_query, 'missions')
    launches = get_data(url, launch_query, 'launches')
    conn = connect_to_db()
    cursor = conn.cursor()
    conn.commit()

    insert_into_missions(cursor, missions)
    insert_into_rockets(cursor, rockets)
    insert_into_launches(cursor, launches)
    conn.commit()

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
