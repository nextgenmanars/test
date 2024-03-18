from sqlalchemy import Column, Integer, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from sqlalchemy.exc import IntegrityError

engine = create_engine("postgresql+psycopg2://postgres:12580@localhost/task_transaction", echo=True)
Base = sqlalchemy.orm.declarative_base()


class Account(Base):
    __tablename__ = "bank_accounts"
    account_id = Column(Integer(), primary_key=True)
    balance = Column(Float(), nullable=False)


# Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
try:
    new_balance1 = Account(account_id=1, balance=100)
    session.add(new_balance1)

    new_balance2 = Account(account_id=2, balance=500)
    session.add(new_balance2)

    updated_acc = session.query(Account).filter_by(account_id=1).first()
    updated_acc.balance = 150.0

    delete_acc = session.query(Account).filter_by(account_id=2).first()
    session.delete(delete_acc)

    session.commit()

except IntegrityError as i:
    print("Ошибка при выполнении транзакции:", i)
    session.rollback()

session.close()

print("AAA")
