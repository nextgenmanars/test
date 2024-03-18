from sqlalchemy import Column, Integer, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from sqlalchemy.exc import IntegrityError

engine = create_engine("postgresql+psycopg2://postgres:12580@localhost/task_transaction")
Base = sqlalchemy.orm.declarative_base()


class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), nullable=False)
    total_amount = Column(Float(), nullable=False)


# Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

try:
    new_order1 = Order(customer_id=12, total_amount=500)
    session.add(new_order1)

    new_order2 = Order(total_amount=125)
    session.add(new_order2)

    session.commit()
except IntegrityError as i:
    print("Ошибка при вставке данных:", i)
    session.rollback()

session.close()

print("Something")
