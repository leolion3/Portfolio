# DLU Installation Instructions

## Prerequisites

Install the Windows Subsystem for Linux (WSL), it is much easier than doing the stuff in native windows.

## Compiling the sourcecode

Open powershell and navigate into the cloned directory. Run the following commands

```bash
mkdir build
cd build
wsl
sudo apt update && sudo apt upgrade -y && sudo apt install gcc cmake -y
cmake ..
make
```

One-liner 

```bash
mkdir build && cd build && wsl && sudo apt update && sudo apt upgrade -y && cmake .. && make
````

## Setting up the database

### mariaDB

- Install MariaDB
```bash
sudo apt-get install mariadb-server
```
- Start the service
```bash
sudo /etc/init.d/mysql start
```
- Login
```bash
mysql -u your_root_username -p
```
and enter the password

- Create a new database and name it whatever you like, in this example were using "darkflame" as the name
```sql
CREATE DATABASE `darkflame`;
```

- Create a new user for the darkflame server
```sql
CREATE USER 'dflame'@'localhost' IDENTIFIED BY 'dflame';
GRANT ALL PRIVILEGES ON darkflame.* TO 'dflame'@'localhost';
```

- Select the database using
```sql
select darkflame;
```

### Persisting data

- Create the tables from the initial.sql file (you can copy paste each query - it starts with CREATE and ends with ); - into the console and then hit enter)
```sql
CREATE OR REPLACE TABLE accounts (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(35) NOT NULL UNIQUE,
    password TEXT NOT NULL,
    gm_level INT UNSIGNED NOT NULL DEFAULT 0,
    locked BOOLEAN NOT NULL DEFAULT FALSE,
    banned BOOLEAN NOT NULL DEFAULT FALSE,
    play_key_id INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    mute_expire BIGINT UNSIGNED NOT NULL DEFAULT 0
);

CREATE OR REPLACE TABLE charinfo (
    id BIGINT NOT NULL PRIMARY KEY,
    account_id INT NOT NULL REFERENCES accounts(id),
    name VARCHAR(35) NOT NULL,
    pending_name VARCHAR(35) NOT NULL,
    needs_rename BOOLEAN NOT NULL DEFAULT FALSE,
    prop_clone_id BIGINT UNSIGNED AUTO_INCREMENT UNIQUE,
    last_login BIGINT UNSIGNED NOT NULL DEFAULT 0,
    permission_map BIGINT UNSIGNED NOT NULL DEFAULT 0
);

CREATE OR REPLACE TABLE charxml (
    id BIGINT NOT NULL PRIMARY KEY REFERENCES charinfo(id),
    xml_data LONGTEXT NOT NULL
);

CREATE OR REPLACE TABLE command_log (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    character_id BIGINT NOT NULL REFERENCES charinfo(id),
    command VARCHAR(256) NOT NULL
);

CREATE OR REPLACE TABLE friends (
    player_id BIGINT NOT NULL REFERENCES charinfo(id),
    friend_id BIGINT NOT NULL REFERENCES charinfo(id),
    best_friend BOOLEAN NOT NULL DEFAULT FALSE,

    PRIMARY KEY (player_id, friend_id)
);

CREATE OR REPLACE TABLE leaderboard (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    game_id INT UNSIGNED NOT NULL DEFAULT 0,
    last_played TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    character_id BIGINT NOT NULL REFERENCES charinfo(id),
    time BIGINT UNSIGNED NOT NULL,
    score BIGINT UNSIGNED NOT NULL DEFAULT 0
);

CREATE OR REPLACE TABLE mail (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    sender_id INT NOT NULL DEFAULT 0,
    sender_name VARCHAR(35) NOT NULL DEFAULT '',
    receiver_id BIGINT NOT NULL REFERENCES charinfo(id),
    receiver_name VARCHAR(35) NOT NULL,
    time_sent BIGINT UNSIGNED NOT NULL,
    subject TEXT NOT NULL,
    body TEXT NOT NULL,
    attachment_id BIGINT NOT NULL DEFAULT 0,
    attachment_lot INT NOT NULL DEFAULT 0,
    attachment_subkey BIGINT NOT NULL DEFAULT 0,
    attachment_count INT NOT NULL DEFAULT 0,
    was_read BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE OR REPLACE TABLE object_id_tracker (
    last_object_id BIGINT UNSIGNED NOT NULL DEFAULT 0 PRIMARY KEY
);

CREATE OR REPLACE TABLE pet_names (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    pet_name TEXT NOT NULL,
    approved INT UNSIGNED NOT NULL
);

CREATE OR REPLACE TABLE play_keys (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    key_string CHAR(19) NOT NULL UNIQUE,
    key_uses INT NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    active BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE OR REPLACE TABLE properties (
    id BIGINT NOT NULL PRIMARY KEY,
    owner_id BIGINT NOT NULL REFERENCES charinfo(id),
    template_id INT UNSIGNED NOT NULL,
    clone_id BIGINT UNSIGNED REFERENCES charinfo(prop_clone_id),
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    rent_amount INT NOT NULL,
    rent_due BIGINT NOT NULL,
    privacy_option INT NOT NULL,
    mod_approved BOOLEAN NOT NULL DEFAULT FALSE,
    last_updated BIGINT NOT NULL,
    time_claimed BIGINT NOT NULL,
    rejection_reason TEXT NOT NULL,
    reputation BIGINT UNSIGNED NOT NULL,
    zone_id INT NOT NULL
);

CREATE OR REPLACE TABLE ugc (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL REFERENCES accounts(id),
    character_id BIGINT NOT NULL REFERENCES charinfo(id),
    is_optimized BOOLEAN NOT NULL DEFAULT FALSE,
    lxfml MEDIUMBLOB NOT NULL,
    bake_ao BOOLEAN NOT NULL DEFAULT FALSE,
    filename TEXT NOT NULL DEFAULT ''
);

CREATE OR REPLACE TABLE properties_contents (
    id BIGINT NOT NULL PRIMARY KEY,
    property_id BIGINT NOT NULL REFERENCES properties(id),
    ugc_id INT NULL REFERENCES ugc(id),
    lot INT NOT NULL,
    x FLOAT NOT NULL,
    y FLOAT NOT NULL,
    z FLOAT NOT NULL,
    rx FLOAT NOT NULL,
    ry FLOAT NOT NULL,
    rz FLOAT NOT NULL,
    rw FLOAT NOT NULL
);

CREATE OR REPLACE TABLE activity_log (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    character_id BIGINT NOT NULL REFERENCES charinfo(id),
    activity INT NOT NULL,
    time BIGINT UNSIGNED NOT NULL,
    map_id INT NOT NULL
);

CREATE OR REPLACE TABLE bug_reports (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    body TEXT NOT NULL,
    client_version TEXT NOT NULL,
    other_player_id TEXT NOT NULL,
    selection TEXT NOT NULL,
    submitted TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP()
);

CREATE OR REPLACE TABLE servers (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name TEXT NOT NULL,
    ip TEXT NOT NULL,
    port INT NOT NULL,
    state INT NOT NULL,
    version INT NOT NULL DEFAULT 0
);
```
- Check to see that all tables were created using
```sql
SHOW TABLES;
```
- In the build/ directory create a new directory called res
- Copy the folders maps, macros, BrickModels, names and the file chatplus_en_us.txt from the res/ folder in your client to the res/ folder in the build folder
- Unzip the /resources/navmeshes.zip file to build/res/maps/navmeshes
- In the build directory create a locale directory if it does not already exist
- Copy over or create symlinks from locale.xml in your client locale directory to the build/locale directory
- Download <a href="https://github.com/lcdr/utils/blob/master/utils/fdb_to_sqlite.py">this</a> and place it inside the unpacked client's res folder, then execute
```bash
python ./fdb_to_sqlite.py ./cdclient.fdb
```
- Move and rename cdclient.sqlite into build/res/CDServer.sqlite
- Install sqlite3
```bash
sudo apt install sqlite3
```
- Execute the queries found under migrations/cdserver (while in /build/res execute)
```bash
sqlite3 CDServer.sqlite < ../../migrations/cdserver/0_nt_footrace.sql
sqlite3 CDServer.sqlite < ../../migrations/cdserver/1_fix_overbuild_mission.sql
sqlite3 CDServer.sqlite < ../../migrations/cdserver/2_script_component.sql
```
- Ctrl + C to exit
- Execute 
```bash
./MasterServer -a
``` 
to add an admin
- Run the server using
```bash
sudo ./MasterServer
```
(sudo because the port is under 1000 and either needs firewall access or sudo)
- Connect using your LU Client