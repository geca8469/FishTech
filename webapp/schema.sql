CREATE TABLE IF NOT EXISTS Users (
    UserID SERIAL PRIMARY KEY,
    Username VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Fish (
    FishID SERIAL PRIMARY KEY,
    FishName VARCHAR(255),
    FishImage1 VARCHAR(255),
    FishImage2 VARCHAR(255),
    Size DECIMAL,
    Description TEXT
);

CREATE TABLE IF NOT EXISTS WaterBody (
    WaterBodyID SERIAL PRIMARY KEY,
    Name VARCHAR(255),
    Type VARCHAR(255),
    Latitude DECIMAL,
    Longitude DECIMAL,
    Size DECIMAL,
    Description TEXT
);

CREATE TABLE IF NOT EXISTS FishCondition (
    FishConditionID SERIAL PRIMARY KEY,
    FishID INTEGER REFERENCES Fish(FishID),
    Temperature DECIMAL,
    PHLevel DECIMAL,
    Salinity DECIMAL,
    OxygenLevel DECIMAL
);

CREATE TABLE IF NOT EXISTS WaterCondition (
    WaterConditionID SERIAL PRIMARY KEY,
    WaterBodyID INTEGER REFERENCES WaterBody(WaterBodyID),
    Temperature DECIMAL,
    PHLevel DECIMAL,
    Salinity DECIMAL,
    OxygenLevel DECIMAL
);

CREATE TABLE IF NOT EXISTS UserFavorites (
    UserFavoriteID SERIAL PRIMARY KEY,
    UserID INTEGER REFERENCES Users(UserID),
    FishID INTEGER REFERENCES Fish(FishID)
);

CREATE TABLE IF NOT EXISTS UserSetting (
    UserSettingID SERIAL PRIMARY KEY,
    UserID INTEGER REFERENCES Users(UserID),
    FishConditionID INTEGER REFERENCES FishCondition(FishConditionID)
);

CREATE TABLE IF NOT EXISTS WaterBodyFish (
    WaterBodyID INTEGER REFERENCES WaterBody(WaterBodyID),
    FishID INTEGER REFERENCES Fish(FishID),
    PRIMARY KEY (WaterBodyID, FishID)
);
