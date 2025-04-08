from sqlalchemy.orm import Session
from models.thread import Thread

class ThreadRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_by_id(self, thread_id: str):
        return self.db.query(Thread).filter(Thread.thread_id == thread_id).first()
    
    def get_all(self) -> list[Thread]:
        return self.db.query(Thread).all()
    
    def create(self, thread: dict) -> Thread:
        nuevo_thread = Thread(**thread)
        self.db.add(nuevo_thread)
        self.db.commit()
        self.db.refresh(nuevo_thread)
        return nuevo_thread
    
    def update(self, thread: Thread, update_data: dict) -> Thread:
        for key, value in update_data.items():
            setattr(thread, key, value)
        self.db.commit()
        self.db.refresh(thread)
        return thread
    
    def delete(self, thread: Thread) -> None:
        self.db.delete(thread)
        self.db.commit()