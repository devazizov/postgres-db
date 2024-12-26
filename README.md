
# PostgreSQL Database Interaction

This project demonstrates a simple Python application for interacting with a PostgreSQL database using the `psycopg2` library. It provides methods to perform CRUD operations (Create, Read, Update, Delete) on a `users` table, which stores user information such as `user_id` and `full_name`.

## Features

- **Create**: Add new users to the database.
- **Read**: Retrieve user details based on `user_id`.
- **Update**: Modify user details.
- **Delete**: Remove a user from the database.
- **List**: Retrieve a list of all users.
- **Count**: Count the total number of users in the database.

## Requirements

- Python 3.x
- `psycopg2` library
- PostgreSQL server

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/devazizov/postgres-db.git
   cd postgres-db
   ```

2. Install the required dependencies:

   ```bash
   pip install psycopg2.binary
   ```

3. Set up the PostgreSQL database:
   - Ensure you have a PostgreSQL server running.
   - Create a new database, e.g., `users`.
   - Update the connection details in the `database.py` file (e.g., `db_name`, `db_user`, `db_password`, `db_host`, `db_port`).

## Usage

### Create the `users` table

The `create_users_table` method will create the `users` table in the database if it does not already exist.

```python
db.create_users_table()
```

### Add a new user

The `create` method adds a new user to the `users` table.

```python
db.create(user_id="123", full_name="Azizov Aziz")
```

### Read user details

The `read` method retrieves user details based on the `user_id`.

```python
user = db.read(user_id="123")
print(user)
```

### Update user details

The `update` method modifies the `full_name` of a user.

```python
db.update(user_id="123", full_name="Azizov Azizbek")
```

### List all users

The `list` method returns a list of all users in the database.

```python
users = db.list()
print(users)
```

### Count users

The `count` method returns the total number of users in the database.

```python
count = db.count()
print(count)
```

### Delete a user

The `delete` method removes a user based on `user_id`.

```python
db.delete(user_id="123")
```

## Example Workflow

Here is an example of how to use the methods:

```python
from database import db

# Create users table
db.create_users_table()

# Add a new user
db.create(user_id="123", full_name="Azizov Aziz")

# Read user details
user = db.read(user_id="123")
print("User Details:", user)

# Update user details
db.update(user_id="123", full_name="Azizov Azizbek")

# List all users
users = db.list()
print("All Users:", users)

# Count users
count = db.count()
print("Total Users:", count["count"])

# Delete a user
db.delete(user_id="123")

# List all users after deletion
users = db.list()
print("All Users After Deletion:", users)
```

## Author

This project was developed by Azizov Azizbek.  
You can contact me via email at azizoov.uz@gmail.com, check out my GitHub profile: [GitHub](https://github.com/devazizov), or visit my website: [Your Website](https://azizov.dev).
