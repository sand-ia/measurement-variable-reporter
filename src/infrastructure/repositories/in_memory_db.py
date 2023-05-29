from typing import Any, Dict, List
from uuid import uuid4, UUID
import json
from datetime import datetime
from enum import Enum
from inspect import isclass


class InMemoryDB:
    class Encoder(json.JSONEncoder):
        def default(self, o: Any):
            if isinstance(o, UUID):
                return str(o)
            if isinstance(o, datetime):
                return o.isoformat()
            if isinstance(o, Enum):
                return o.value
            if isclass(o):
                return o.__name__
            if o.__class__ is not None:
                return o.__dict__
            return super().default(o)

    def __init__(self, user: str, password: str) -> None:
        self._user: str = user
        self._password: str = password
        self._is_authorized: bool = False

    def connect(self, user: str, password: str) -> None:
        if self._user == user and self._password == password:
            self._is_authorized = True
            return
        raise PermissionError("InMemoryDB: Unauthorazed Access")

    def auth(self):
        if self._is_authorized:
            return
        raise PermissionError("InMemoryDB: Unauthorazed Access")

    def save(self, table_name: str, document: Dict[str, Any]) -> str:
        file_path = f"src/infrastructure/repositories/storage/{table_name}.json"
        table: List[Dict[str, Any]]

        try:
            with open(file_path, "r", encoding="utf8") as file:
                table = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            table = []

        document_uuid = document.get("uuid")
        if document_uuid is None:
            document["uuid"] = str(uuid4())

        table.append(document)

        with open(file_path, mode="w", encoding="utf8") as file:
            json.dump(table, file, indent=2, cls=InMemoryDB.Encoder)

        return document["uuid"]

    def get_all(self, table_name: str) -> List[Dict[str, Any]]:
        file_path = f"src/infrastructure/repositories/storage/{table_name}.json"
        table: List[Dict[str, Any]]

        try:
            with open(file_path, "r", encoding="utf8") as file:
                table = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            raise Exception("InMemoryDB: Document not found")

        return table

    def get(self, table_name: str, document_uuid: str) -> Dict[str, Any]:
        file_path = f"src/infrastructure/repositories/storage/{table_name}.json"
        table: List[Dict[str, Any]]

        try:
            with open(file_path, "r", encoding="utf8") as file:
                table = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            raise Exception("InMemoryDB: Document not found")

        for document in table:
            if document["uuid"] == document_uuid:
                return document

        # TODO: raise correct exception.
        raise Exception("InMemoryDB: Document not found")

    def update(self, table_name: str, new_document: Dict[str, Any]) -> None:
        document_uuid = new_document.get("uuid")
        if document_uuid is None:
            raise TypeError("InMemoryDB: Document doesn't have a uuid")

        file_path = f"src/infrastructure/repositories/storage/{table_name}.json"
        table: List[Dict[str, Any]]

        try:
            with open(file_path, "r", encoding="utf8") as file:
                table = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            raise Exception("InMemoryDB: Document not found")

        for document in table:
            if document["uuid"] == str(document_uuid):
                document.update(**new_document)
                break

        with open(file_path, mode="w", encoding="utf8") as file:
            json.dump(table, file, indent=2, cls=InMemoryDB.Encoder)


# TODO: Get user and pass from .env
in_memory_db = InMemoryDB("sandia", "sandia")
