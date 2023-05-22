from typing import Any, Dict, List
from uuid import uuid4


class InMemoryDB:
    def __init__(self, user: str, password: str) -> None:
        self._user: str = user
        self._password: str = password
        self._is_authorized: bool = False
        self._tables: Dict[str, List[Dict[str, Any]]] = {}

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
        table = self._tables.get(table_name)
        if table is None:
            table = []
            self._tables[table_name] = table
        document_id = document.get("uuid")
        if document_id is None:
            document["uuid"] = str(uuid4())
        table.append(document)
        return document["uuid"]

    def get_all(self, table_name: str) -> List[Dict[str, Any]]:
        table = self._tables.get(table_name)
        if table is None:
            # TODO: raise correct exception.
            raise Exception("InMemoryDB: Table doesn't exist")

        return table

    def get(self, table_name: str, document_id: str) -> Dict[str, Any]:
        table = self.get_all(table_name)

        for document in table:
            if document["uuid"] == document_id:
                return document

        # TODO: raise correct exception.
        raise Exception("InMemoryDB: Document not found")


# TODO: Get user and pass from .env
in_memory_db = InMemoryDB("sandia", "sandia")
