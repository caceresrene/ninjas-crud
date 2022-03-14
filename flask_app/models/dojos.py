from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def get_all(cls):
    results = connectToMySQL('esquema_dojos_y_ninjas').query_db('SELECT * FROM dojos;')
    dojos = []
    for row_dojo in results:
      dojos.append(cls(row_dojo))
    return dojos

  @classmethod
  def get_dojo(cls, data):
    query = 'SELECT * FROM dojos WHERE id = (%(id)s);'
    results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query, data)
    return results[0]

  @classmethod
  def create(cls, data):
    query = "INSERT INTO dojos (name) VALUES (%(name)s);"
    result = connectToMySQL('esquema_dojos_y_ninjas').query_db(query, data)
    return result
