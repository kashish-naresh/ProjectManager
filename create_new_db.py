import sqlite3

def create_new_db(db_name):
    """Sets up tables for new database"""
    
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()

            # Create Tasks table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Tasks(
                TaskID INTEGER PRIMARY KEY,
                Description TEXT,
                Deadline DATE,
                Created TIMESTAMP,
                Completed TIMESTAMP,
                ProjectID INTEGER,
                FOREIGN KEY(ProjectID) REFERENCES Projects(ProjectID)
            );
        """)

        # Create Projects table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Projects(
                ProjectID INTEGER PRIMARY KEY,
                Description TEXT,
                Deadline DATE,
                Created TIMESTAMP,
                Completed TIMESTAMP
            );
        """)

        
        db.commit()
        
       



        