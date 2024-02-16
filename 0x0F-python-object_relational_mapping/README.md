# 0x0F. Python - Object-relational mapping

This project is part of the Alx - SE curriculum of software engineering. The main objective is to understand and implement the concepts of Object-relational mapping (ORM) in Python.

## Learning Objectives

- Understand how to connect to a MySQL database from a Python script.
- Learn how to SELECT rows in a MySQL table from a Python script.
- Understand how to INSERT rows in a MySQL table from a Python script.
- Learn what ORM (Object-relational mapping) means.
- Understand how to map a Python Class to a MySQL table.
- Learn how to create a Python Virtual Environment.

## Installation

To get started with this project, clone the repository to your local system. Then, navigate to the project directory and create a virtual environment:

```bash
python3 -m venv venv
```

### Activate the virtual environment:

```bash
source venv/bin/activate
```

### Install the required packages:

```bash
pip install -r requirements.txt
```

### Usage

All scripts in this project are executable and are designed to interact with a MySQL database. Each script should be run using the following format:

```bash
./script_name.py mysql_username mysql_password database_name
```

Here, `mysql_username` is the username for your MySQL server, `mysql_password` is the password, and `database_name` is the name of the database you want to interact with.

For example, if you want to run the `101-relationship_states_cities_list.py` script with `root` as the username and password, and `hbtn_0e_101_usa` as the database name, you would use the following command:

```bash
./101-relationship_states_cities_list.py root root hbtn_0e_101_usa
```

Please replace `script_name.py`, `mysql_username`, `mysql_password`, and `database_name` with the actual values based on your setup and the specific script you want to run.
