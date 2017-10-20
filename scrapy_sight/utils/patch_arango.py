# coding: utf-8
import json

from pyArango.document import Document
from pyArango.theExceptions import CreationError
from pyArango.collection import Collection


class MyDocument(Document):
    def save(self, waitForSync=False, **docArgs):
        """Saves the document to the database by either performing a POST (for a new document) or 
        a PUT (complete document overwrite).
        If you want to only update the modified fields use the .path() function.
        Use docArgs to put things such as 'waitForSync = True' (for a full list cf ArangoDB's doc).
        It will only trigger a saving of the document if it has been modified since the last 
        save. If you want to force the saving you can use forceSave()"""
        payload = self._store.getStore()
        self._save(payload, waitForSync=False, **docArgs)

    def _save(self, payload, waitForSync=False, **docArgs):

        if self.modified:

            params = dict(docArgs)
            params.update({'collection': self.collection.name, "waitForSync": waitForSync})

            if self.collection._validation['on_save']:
                self.validate()
            if self.URL is None:
                if self._key is not None:
                    payload["_key"] = self._key
                payload = json.dumps(payload, encoding='gbk')
                r = self.connection.session.post(self.documentsURL, params=params, data=payload)
                update = False
            else:
                payload = json.dumps(payload, encoding='gbk')
                r = self.connection.session.put(self.URL, params=params, data=payload)
                update = True

            data = r.json()

            if (r.status_code == 201 or r.status_code == 202) and "error" not in data:
                if update:
                    self._rev = data['_rev']
                else:
                    self.setPrivates(data)
            else:
                if update:
                    from pyArango.theExceptions import UpdateError
                    raise UpdateError(data['errorMessage'], data)
                else:
                    raise CreationError(data['errorMessage'], data)

            self.modified = False

        self._store.resetPatch()


class Collection(Collection):
    def __init__(self):
        self.documentClass = MyDocument
