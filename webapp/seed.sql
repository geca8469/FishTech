-- Seed data for local/dev use. Safe to re-run: clears and repopulates all tables.

TRUNCATE TABLE
    WaterBodyFish,
    UserSetting,
    UserFavorites,
    WaterCondition,
    FishCondition,
    WaterBody,
    Fish,
    Users
RESTART IDENTITY CASCADE;

INSERT INTO Users (Username, Password) VALUES
    ('demo', 'demo123'),
    ('jsmith', 'password1');

INSERT INTO Fish (FishName, FishImage1, FishImage2, Size, Description) VALUES
    ('Koi', '/static/images/koi_color_crop.jpg', NULL, 30.0, 'Ornamental domesticated carp, prized for their bright coloring.'),
    ('Largemouth Bass', '/static/images/largemouth_bass_color.jpg', NULL, 40.0, 'Popular North American freshwater gamefish with a large upper jaw.'),
    ('Rainbow Trout', '/static/images/rainbow_trout_color.jpg', NULL, 35.0, 'Freshwater trout species known for its iridescent, rainbow-like coloring.'),
    ('Bluegill', '/static/images/bluegill_color.jpg', NULL, 15.0, 'Common panfish found in ponds and lakes across the eastern US.'),
    ('Channel Catfish', '/static/images/channel_catfish_color.jpg', NULL, 50.0, 'Whiskered bottom-feeder common in rivers, lakes, and reservoirs.');

INSERT INTO WaterBody (Name, Type, Latitude, Longitude, Size, Description) VALUES
    ('Lake Michigan', 'Lake', 44.0000, -87.0000, 58030.0, 'One of the five Great Lakes of North America.'),
    ('Boulder Creek', 'River', 40.0150, -105.2705, 12.0, 'Creek running through Boulder, Colorado.'),
    ('Chatfield Reservoir', 'Reservoir', 39.5375, -105.0669, 5.6, 'Reservoir south of Denver, Colorado.');

INSERT INTO FishCondition (FishID, Temperature, PHLevel, Salinity, OxygenLevel) VALUES
    (1, 20.0, 7.5, 0.0, 8.0),
    (2, 22.0, 7.0, 0.0, 6.5),
    (3, 12.0, 7.2, 0.0, 9.0),
    (4, 24.0, 7.4, 0.0, 6.0),
    (5, 26.0, 7.1, 0.0, 5.5);

INSERT INTO WaterCondition (WaterBodyID, Temperature, PHLevel, Salinity, OxygenLevel) VALUES
    (1, 15.0, 8.1, 0.1, 9.5),
    (2, 10.0, 7.3, 0.0, 10.0),
    (3, 18.0, 7.6, 0.0, 8.0);

INSERT INTO WaterBodyFish (WaterBodyID, FishID) VALUES
    (1, 2),
    (1, 5),
    (2, 3),
    (2, 4),
    (3, 2),
    (3, 4);

INSERT INTO UserFavorites (UserID, FishID) VALUES
    (1, 1),
    (1, 3);

INSERT INTO UserSetting (UserID, FishConditionID) VALUES
    (1, 1);
