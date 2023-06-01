import json
from typing import Any, Dict, List
from uuid import uuid4


class InMemoryDB:
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

    def save(self, table_name: str, document: str) -> str:
        self.auth()
        file_path = f"src/infrastructure/repositories/storage/{table_name}.json"
        try:
            with open(file_path, "r", encoding="utf8") as file:
                table: List[Dict[str, Any]] = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            table = []

        document_dict: Dict[str, Any] = json.loads(document)
        document_uuid = document_dict.get("uuid")
        if document_uuid is None:
            document_dict["uuid"] = str(uuid4())

        table.append(document_dict)

        with open(file_path, mode="w", encoding="utf8") as file:
            json.dump(table, file, indent=2)

        return document_dict["uuid"]

    def get_all(self, table_name: str) -> List[Dict[str, Any]]:
        self.auth()
        file_path = f"src/infrastructure/repositories/storage/{table_name}.json"
        try:
            with open(file_path, "r", encoding="utf8") as file:
                table: List[Dict[str, Any]] = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            raise Exception("InMemoryDB: Document not found")

        return table

    def get(self, table_name: str, document_uuid: str) -> Dict[str, Any]:
        self.auth()
        file_path = f"src/infrastructure/repositories/storage/{table_name}.json"
        try:
            with open(file_path, "r", encoding="utf8") as file:
                table: List[Dict[str, Any]] = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            raise Exception("InMemoryDB: Document not found")

        for document in table:
            if document["uuid"] == document_uuid:
                return document

        # TODO: raise correct exception.
        raise Exception("InMemoryDB: Document not found")

    def update(self, table_name: str, document_uuid: str, updates: str) -> None:
        self.auth()
        file_path = f"src/infrastructure/repositories/storage/{table_name}.json"
        try:
            with open(file_path, "r", encoding="utf8") as file:
                table: List[Dict[str, Any]] = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            raise Exception("InMemoryDB: Document not found")

        is_document_found = False
        for document in table:
            if document["uuid"] == str(document_uuid):
                updates_dict: Dict[str, Any] = json.loads(updates)
                document.update(**updates_dict)
                is_document_found = True
                break

        if not is_document_found:
            # TODO: raise correct exception.
            raise Exception("InMemoryDB: Document not found")

        with open(file_path, mode="w", encoding="utf8") as file:
            json.dump(table, file, indent=2)


# TODO: Get user and pass from .env
in_memory_db = InMemoryDB("sandia", "sandia")
