
import sqlite3

DATABASE = "simulation.db"


def init_db():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS simulation_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_type TEXT NOT NULL
                CHECK(event_type IN ('clicked', 'reported')),
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def record_event(event_type):
    if event_type not in ("clicked", "reported"):
        raise ValueError("Invalid simulation event")

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO simulation_events (event_type) VALUES (?)",
        (event_type,)
    )

    connection.commit()
    connection.close()


def get_statistics():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT event_type, COUNT(*)
        FROM simulation_events
        GROUP BY event_type
    """)

    results = dict(cursor.fetchall())
    connection.close()

    return {
        "clicked": results.get("clicked", 0),
        "reported": results.get("reported", 0)
    }


def get_recent_events():
    connection = sqlite3.connect("simulation.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("""
        SELECT event_type, timestamp
        FROM simulation_events
        ORDER BY id DESC
        LIMIT 10
    """)

    events = [dict(row) for row in cursor.fetchall()]
    connection.close()

    return events

if __name__ == "__main__":
    init_db()
    print("SQLite database created successfully!")
