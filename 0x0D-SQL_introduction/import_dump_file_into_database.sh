#!/bin/bash

# Define color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Define variables
URL="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql"
FILE="temperatures.sql"
DB="hbtn_0c_0"

# Check if the file already exists
if [ -f "$FILE" ]; then
    echo -e "${GREEN}Dump File ${FILE} already exists.${NC}"
else
    # Download the SQL dump file
    if wget "$URL"; then
        echo -e "${GREEN}Dump File ${FILE} downloaded successfully.${NC}"
    else
        echo -e "${RED}Error downloading dump file${FILE}.${NC}"
        exit 1
    fi
fi

# Import the SQL dump file into the MySQL database
if mysql -u root -p "$DB" < "$FILE"; then
    echo -e "${GREEN}Dump File ${FILE} imported successfully into ${DB} DB.${NC}"
else
    echo -e "${RED}Error importing ${FILE} file.${NC}"
    exit 1
fi

