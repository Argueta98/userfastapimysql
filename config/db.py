from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root: @localhost:3306/prueba1")

conn = engine.connect()

meta_data = MetaData()


