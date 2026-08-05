import os
import psycopg2
from psycopg2 import sql

DATABASE_URL = os.environ.get('DATABASE_URL')

### Main Functions
def create_tables():
    conn = None
    c = None
    
    try:
        conn = psycopg2.connect(DATABASE_URL)
        c = conn.cursor()
        
# Users
        c.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                UserID SERIAL PRIMARY KEY,
                Username VARCHAR(255) NOT NULL,
                Password VARCHAR(255) NOT NULL
            );
        
        ''')
        
# Fish
        c.execute('''
            CREATE TABLE IF NOT EXISTS Fish (
                FishID SERIAL PRIMARY KEY,
                FishName VARCHAR(255),
                FishImage1 VARCHAR(255),
                FishImage2 VARCHAR(255),
                Size DECIMAL,
                Description TEXT
            );
        ''')

# WaterBody
        c.execute('''
            CREATE TABLE IF NOT EXISTS WaterBody (
                WaterBodyID SERIAL PRIMARY KEY,
                Name VARCHAR(255),
                Type VARCHAR(255),
                Latitude DECIMAL,
                Longitude DECIMAL,
                Size DECIMAL,
                Description TEXT
            );
        ''')

# FishCondition
        c.execute('''
            CREATE TABLE IF NOT EXISTS FishCondition (
                FishConditionID SERIAL PRIMARY KEY,
                FishID INTEGER REFERENCES Fish(FishID),
                Temperature DECIMAL,
                PHLevel DECIMAL,
                Salinity DECIMAL,
                OxygenLevel DECIMAL
            );
        ''')

# WaterCondition
        c.execute('''
            CREATE TABLE IF NOT EXISTS WaterCondition (
                WaterConditionID SERIAL PRIMARY KEY,
                WaterBodyID INTEGER REFERENCES WaterBody(WaterBodyID),
                Temperature DECIMAL,
                PHLevel DECIMAL,
                Salinity DECIMAL,
                OxygenLevel DECIMAL
            );
        ''')
        
# UserFavorites
        c.execute('''
            CREATE TABLE IF NOT EXISTS UserFavorites (
                UserFavoriteID SERIAL PRIMARY KEY,
                UserID INTEGER REFERENCES Users(UserID),
                FishID INTEGER REFERENCES Fish(FishID)
            );
        ''')
        
# UserSettings
        c.execute('''
            CREATE TABLE IF NOT EXISTS UserSetting (
                UserSettingID SERIAL PRIMARY KEY,
                UserID INTEGER REFERENCES Users(UserID),
                FishConditionID INTEGER REFERENCES FishCondition(FishConditionID)
            );
        ''')

# WaterBodyFish
        c.execute('''
            CREATE TABLE IF NOT EXISTS WaterBodyFish (
                WaterBodyID INTEGER REFERENCES WaterBody(WaterBodyID),
                FishID INTEGER REFERENCES Fish(FishID),
                PRIMARY KEY (WaterBodyID, FishID)
            );
        ''')
        
        conn.commit()

        c.execute('''
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public';
        ''')
        
        tables = c.fetchall()
        return f'Tables in database: {tables}'
        
    except Exception as e:
        if conn is not None:
            conn.rollback()
        return f"Couldn't create tables: {e}"

    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()


def get_user(username, password):
    conn = None
    c = None
    
    try:
        conn = psycopg2.connect(DATABASE_URL)
        c = conn.cursor()
        
        c.execute('''
            SELECT userID, username
            FROM Users
            WHERE username = %s AND PASSWORD = %s;
            ''', (username, password)
        )
        
        user = c.fetchone()
        return user
        
    except Exception as e:
        if conn is not None:
            conn.rollback()
        print(f'Error looking up user: {e}')
        return None

    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()

def add_user(username, password):
    conn = None
    c = None

    try:
        conn = psycopg2.connect(DATABASE_URL)
        c = conn.cursor()

        c.execute('''
            SELECT UserID
            FROM Users
            WHERE Username = %s;
            ''', (username,)
        )
        if c.fetchone() is not None:
            return (False, 'Username already in use')

        c.execute(
            '''
            INSERT INTO Users (username, password)
            VALUES (%s, %s);
            ''', (username, password)
        )

        conn.commit()

        return (True, 'User added')

    except Exception as e:
        if conn is not None:
            conn.rollback()

        print(f"Error adding user: {e}")
        return (False, 'Database Error')

    finally:
        if c is not None:
            c.close()

        if conn is not None:
            conn.close()

def get_fish():
    conn = None
    c = None
    
    try:
        conn = psycopg2.connect(DATABASE_URL)
        c = conn.cursor()
        
        c.execute('''
            SELECT FishName, FishImage1, Size, Description
            FROM Fish;
            '''
        )
        
        fish = c.fetchall()
        return fish
        
    except Exception as e:
        if conn is not None:
            conn.rollback()
        print(f'Error Getting Fish collection: {e}')
        return None

    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()
            
### Test Functions
def get_table(table_name):
    conn = None
    c = None
    
    try:
        conn = psycopg2.connect(DATABASE_URL)
        c = conn.cursor()

        query = sql.SQL('''
            SELECT *
            FROM {};
        ''').format(sql.Identifier(table_name))

        c.execute(query)

        table = c.fetchall()

        print('successfully retrived table')
        return table

    except Exception as e:
        if conn is not None:
            conn.rollback()

        print(f"Error getting table: {e}")
        return None

    finally:
        if c is not None:
            c.close()

        if conn is not None:
            conn.close()


def drop_all_tables():
    conn = None
    c = None

    try:
        conn = psycopg2.connect(DATABASE_URL)
        c = conn.cursor()

        c.execute('''
            DROP TABLE IF EXISTS
                WaterBodyFish,
                UserSetting,
                UserFavorites,
                WaterCondition,
                FishCondition,
                WaterBody,
                Fish,
                Users
            CASCADE;
        ''')

        conn.commit()

        return "Deleted All tables"

    except Exception as e:
        if conn is not None:
            conn.rollback()

        print(f"Error deleting tables: {e}")
        return None

    finally:
        if c is not None:
            c.close()

        if conn is not None:
            conn.close()