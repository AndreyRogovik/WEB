from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.models import Contact
from datetime import date, timedelta, datetime
fake = Faker()


SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:567234@localhost:5432/rest_app"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_fake_contacts(num_contacts):
    with SessionLocal() as db:
        for _ in range(num_contacts):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            phone_number = fake.phone_number()
            birthday = fake.date_between(start_date='-80y', end_date='-18y')
            additional_data = fake.text()

            contact = Contact(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                birthday=birthday,
                additional_data=additional_data
            )
            db.add(contact)
        db.commit()


# create_fake_contacts(100)


with SessionLocal() as db:
    skip = 0
    limit = 100
    days = 30
    current_day = date.today().timetuple().tm_yday
    filter_from = current_day
    filter_to = (date.today() + timedelta(days=days)).timetuple().tm_yday
    query = db.query(Contact)
    contacts = query.all()
    next_day_birthdays = []
    for contact in contacts:
        if filter_to > contact.birthday.timetuple().tm_yday >= filter_from:
            next_day_birthdays.append(contact)
            print(f"name {contact.first_name}, {contact.last_name}  birthday: {contact.birthday.date()}")

    next_day_birthdays_sorted = sorted(next_day_birthdays, key=lambda x: (x.birthday.month, x.birthday.day))
    print("------------------------------------")
    for contact in next_day_birthdays_sorted:
        print(f"name {contact.first_name}, {contact.last_name}  birthday: {contact.birthday.date()}")
    #
    # for contact in sorted_contacts:
    #     print("sorted")
    #     print(f"name {contact.first_name}, {contact.last_name}  birthday: {contact.birthday.date()}")


# Отримати поточну дату
current_date = datetime.now()

# Отримати порядковий номер дня у році

day_of_year = current_date.timetuple().tm_yday

print("Поточний день у році:", day_of_year)