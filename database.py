from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime


engine = create_engine(
    "sqlite:///intrusion.db"
)


Base = declarative_base()



class Detection(Base):

    __tablename__ = "detections"


    id = Column(
        Integer,
        primary_key=True
    )


    dataset = Column(
        String
    )


    time = Column(
        String
    )


    normal = Column(
        Integer
    )


    attack = Column(
        Integer
    )



Base.metadata.create_all(
    engine
)



Session = sessionmaker(
    bind=engine
)



def save_result(
    dataset,
    normal,
    attack
):

    session = Session()


    record = Detection(

        dataset=dataset,

        time=str(datetime.now()),

        normal=normal,

        attack=attack

    )


    session.add(record)

    session.commit()

    session.close()