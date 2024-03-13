from typing import List, Union

from sqlalchemy import and_
from sqlalchemy.orm import Session

from src.database.models import Note, Tag, User
from src.schemas import NoteModel, NoteUpdate, NoteStatusUpdate


async def get_notes(skip: int, limit: int, user: User, db: Session) -> List[Note]:

    """
    The get_notes function returns a list of notes for the given user.

    :param skip: int: Skip the first n notes
    :param limit: int: Limit the number of notes that are returned
    :param user: User: Get the user_id from the database
    :param db: Session: Access the database
    :return: A list of notes for a particular user
    :doc-author: AR
    """
    return db.query(Note).filter(Note.user_id == user.id).offset(skip).limit(limit).all()


async def get_note(note_id: int, user: User, db: Session) -> Note:
    """
    The get_note function takes in a note_id and user, and returns the Note object with that id.
        Args:
            note_id (int): The id of the Note to be retrieved.
            user (User): The User who owns the Note to be retrieved.

    :param note_id: int: Get the note with the given id
    :param user: User: Get the user who is making the request
    :param db: Session: Pass the database session to the function
    :return: A note object from the database
    :doc-author: AR
    """
    return db.query(Note).filter(and_(Note.id == note_id, Note.user_id == user.id)).first()


async def create_note(body: NoteModel, user: User, db: Session) -> Note:
    """
    The create_note function creates a new note in the database.

    :param body: NoteModel: Get the title, description and tags from the request body
    :param user: User: Get the user from the database
    :param db: Session: Access the database
    :return: A note object
    :doc-author: AR
    """

    tags = db.query(Tag).filter(and_(Tag.id.in_(body.tags), Tag.user_id == user.id)).all()
    note = Note(title=body.title, description=body.description, tags=tags, user=user)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


async def remove_note(note_id: int, user: User, db: Session) -> Union[Note, None]:

    """
    The remove_note function removes a note from the database.
        Args:
            note_id (int): The id of the note to be removed.
            user (User): The user who owns the note to be removed.
            db (Session): A connection to our database, used for querying and deleting notes.

    :param note_id: int: Identify the note to be removed
    :param user: User: Identify the user who is making the request
    :param db: Session: Access the database
    :return: The note that was removed
    :doc-author: AR
    """
    note = db.query(Note).filter(and_(Note.id == note_id, Note.user_id == user.id)).first()
    if note:
        db.delete(note)
        db.commit()
    return note


async def update_note(note_id: int, body: NoteUpdate, user: User, db: Session) -> Union[Note, None]:

    """
    The update_note function updates a note in the database.
        Args:
            note_id (int): The id of the note to update.
            body (NoteUpdate): The updated information for the Note object.  This is a Pydantic model, so it will be validated before being passed into this function.
                It contains title, description, done and tags fields that are all optional and can be used to update any or all of those fields on an existing Note object in the database.
                If no value is provided for one of these fields then that field will not be updated on the existing Note object

    :param note_id: int: Specify the note we want to delete
    :param body: NoteUpdate: Pass the updated note data to the function
    :param user: User: Get the user id from the token
    :param db: Session: Access the database
    :return: The updated note or none if the note was not found
    :doc-author: AR
    """

    note = db.query(Note).filter(and_(Note.id == note_id, Note.user_id == user.id)).first()
    if note:
        tags = db.query(Tag).filter(and_(Tag.id.in_(body.tags), Note.user_id == user.id)).all()
        note.title = body.title
        note.description = body.description
        note.done = body.done
        note.tags = tags
        db.commit()
    return note


async def update_status_note(note_id: int, body: NoteStatusUpdate, user: User, db: Session) -> Union[Note, None]:

    """
    The update_status_note function updates the status of a note.
        Args:
            note_id (int): The id of the note to update.
            body (NoteStatusUpdate): The new status for the specified Note.  Must be either True or False, where True indicates that a task is complete and False indicates that it is not complete.
            user (User): A User object containing information about who made this request, including their username and password hash.  This function will only allow users to update notes they have created themselves; if another user attempts to update one of your notes, an error message will be returned instead

    :param note_id: int: Identify the note to be updated
    :param body: NoteStatusUpdate: Pass the data from the request body to this function
    :param user: User: Get the user id of the logged in user
    :param db: Session: Access the database
    :return: A note
    :doc-author: Trelent
    """
    note = db.query(Note).filter(and_(Note.id == note_id, Note.user_id == user.id)).first()
    if note:
        note.done = body.done
        db.commit()
    return note
