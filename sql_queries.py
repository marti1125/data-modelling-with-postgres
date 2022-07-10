# DROP TABLES

songplay_table_drop = "drop table songplays;"
user_table_drop = "drop table users;"
song_table_drop = "drop table songs;"
artist_table_drop = "drop table artists;"
time_table_drop = "drop table time;"

# CREATE TABLES

songplay_table_create = ("""
    create table if not exists songplays(start_time varchar not null, user_id int not null, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar);
""")

user_table_create = ("""
    create table if not exists users(user_id int, first_name varchar, last_name varchar, gender varchar, level varchar, primary key(user_id));
""")

song_table_create = ("""
    create table if not exists songs(song_id varchar, title varchar not null, artist_id varchar, year int, duration decimal not null, primary key (song_id));
""")

artist_table_create = ("""
    create table if not exists artists(artist_id varchar, name varchar not null, location varchar, latitude float, longitude float, primary key (artist_id));
""")

time_table_create = ("""
    create table if not exists time(id serial primary key, timestamp varchar, hour int, day int, week_of_year int, month int, year int, weekday int);
""")

# INSERT RECORDS

songplay_table_insert = ("""
    insert into songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) values(%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
    insert into users(user_id, first_name, last_name, gender, level) values(%s, %s, %s, %s, %s) ON CONFLICT
    (user_id) DO UPDATE SET level = EXCLUDED.level;
""")

song_table_insert = ("""
    insert into songs(song_id, title, artist_id, year, duration) values(%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
    insert into artists(artist_id, name, location, latitude, longitude) values(%s, %s, %s, %s, %s) ON CONFLICT
    (artist_id) DO NOTHING;
""")

time_table_insert = ("""
    insert into time(timestamp, hour, day, week_of_year, month, year, weekday) values(%s,%s,%s,%s,%s,%s,%s);
""")

# FIND SONGS

song_select = ("""
    select s.song_id, a.artist_id
    from songs as s
    join artists as a on a.artist_id = s.artist_id
    where s.title = %s and a.name = %s and s.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]