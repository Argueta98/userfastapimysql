from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://jesiel:jcste9710@localhost:3306/prueba1")

conn = engine.connect()

meta_data = MetaData()


