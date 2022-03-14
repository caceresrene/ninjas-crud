from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.age = data['age']
    self.dojo_id = data['dojo_id']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def get_all(cls):
    results = connectToMySQL('esquema_dojos_y_ninjas').query_db('SELECT * FROM ninjas;')
    ninjas = []
    for row_ninja in results:
      ninjas.append(cls(row_ninja))
    return ninja

  @classmethod
  def get_all_ninjas(cls, data):
    print(data)
    query = 'SELECT * FROM ninjas WHERE dojo_id = (%(dojo_id)s);'
    results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query, data)
    print(results)
    return results

  @classmethod
  def create(cls, data):
    query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
    result = connectToMySQL('esquema_dojos_y_ninjas').query_db(query, data)
    return result
