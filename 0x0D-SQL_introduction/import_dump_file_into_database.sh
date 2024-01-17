#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

URL="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql"
FILE="temperatures.sql"
DB="hbtn_0c_0"

if [ -f "$FILE" ]; then
    echo -e "${GREEN}Dump File ${FILE} already exists.${NC}"
else
    if wget "$URL"; then
        echo -e "${GREEN}Dump File ${FILE} downloaded successfully.${NC}"
    else
        echo -e "${RED}Error downloading dump file${FILE}.${NC}"
        exit 1
    fi
fi

# Check if the database exists
DB_EXISTS=$(mysql -u root -p -e "SHOW DATABASES LIKE '$DB';" | grep "$DB")

if [ "$DB_EXISTS" = "$DB" ]; then
    echo -e "${GREEN}Database ${DB} already exists.${NC}"
else
    echo -e "${GREEN}Database ${DB} does not exist.${NC}"
    echo -e "${GREEN}Creating database ${DB}.${NC}"
    mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS $DB;"
fi

if mysql -u root -p "$DB" < "$FILE"; then
    echo -e "${GREEN}Dump File ${FILE} imported successfully into ${DB} DB.${NC}"
else
    echo -e "${RED}Error importing ${FILE} file.${NC}"
    exit 1
fi
