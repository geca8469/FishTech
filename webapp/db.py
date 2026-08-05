import os
import psycopg2

DATABASE_URL = os.environ.get('DATABASE_URL')

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