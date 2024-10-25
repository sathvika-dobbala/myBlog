# projects.py
import sqlite3

class Project:
    def __init__(self, title, description, image_file):
        self.title = title
        self.description = description
        self.image_file = image_file

    @staticmethod
    def create_table():
        connection = sqlite3.connect('projects.db')
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                image_file TEXT NOT NULL
            )
        ''')
        connection.commit()
        connection.close()

    def save(self):
        connection = sqlite3.connect('projects.db')
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO projects (title, description, image_file)
            VALUES (?, ?, ?)
        ''', (self.title, self.description, self.image_file))
        connection.commit()
        connection.close()

    @staticmethod
    def get_all_projects():
        connection = sqlite3.connect('projects.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM projects')
        projects = cursor.fetchall()
        connection.close()
        return projects

    @staticmethod
    def delete_project(project_id):
        connection = sqlite3.connect('projects.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM projects WHERE id = ?', (project_id,))
        connection.commit()
        connection.close()
