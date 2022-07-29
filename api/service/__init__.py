# import os
# import psycopg2
# from flask_sqlalchemy import SQLAlchemy

# # link with docker
# conn = psycopg2.connect(
#         host="localhost",
#         database="", 
#         user=os.environ['DB_USERNAME'],
#         password=os.environ['DB_PASSWORD'])

# cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS users;')
# cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
#                                  'name varchar (150) NOT NULL,'
#                                  'author varchar (50) NOT NULL);'
#                                  )

# cur.execute('INSERT INTO users (name)'
#             'VALUES (%s)',
#             ('amani')
#             )


# cur.execute('INSERT INTO users (name)'
#             'VALUES (%s)',
#             ('samer')
#             )

# conn.commit()

# cur.close()
# conn.close()