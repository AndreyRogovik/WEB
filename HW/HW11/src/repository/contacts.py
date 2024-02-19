from typing import List
from sqlalchemy.orm import Session
from src.database.models import Contact
from src.schemas import ContactCreate, ContactUpdate
from datetime import date, timedelta

from src.database.db import has_date_next_days


async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()


async def get_contact(contact_id: int, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def create_contact(body: ContactCreate, db: Session) -> Contact:
    contact = Contact(first_name=body.first_name, last_name=body.last_name, email=body.email,
                      phone_number=body.phone_number, birthday=body.birthday, additional_data=body.additional_data)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def remove_contact(contact_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if Contact:
        db.delete(contact)
        db.commit()
    return contact


async def update_contact(contact_id: int, body: ContactUpdate, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.phone_number = body.phone_number
        contact.birthday = body.birthday
        contact.additional_data = body.additional_data
        db.commit()
    return contact


async def search_birthday(param: dict, db: Session):
    days: int = int(param.get("days", 7)) + 1
    current_day = date.today().timetuple().tm_yday
    filter_from = current_day
    filter_to = (date.today() + timedelta(days=days)).timetuple().tm_yday
    query = db.query(Contact)
    contacts = query.all()
    next_day_birthdays = []
    for contact in contacts:
        if filter_to > contact.birthday.timetuple().tm_yday >= filter_from:
            next_day_birthdays.append(contact)
    next_day_birthdays_sorted = sorted(next_day_birthdays, key=lambda x: (x.birthday.month, x.birthday.day))
    return next_day_birthdays_sorted


async def search_contacts(param: dict, db: Session):
    query = db.query(Contact)
    first_name = param.get("first_name")
    last_name = param.get("last_name")
    email = param.get("email")
    if first_name:
        query = query.filter(Contact.first_name.ilike(f"%{first_name}%"))
    if last_name:
        query = query.filter(Contact.last_name.ilike(f"%{last_name}%"))
    if email:
        query = query.filter(Contact.email.ilike(f"%{email}%"))
    contacts = query.all()
    return contacts

