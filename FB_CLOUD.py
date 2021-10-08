import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage

class My_FB:
    def __init__(self, credantial: dict, projectId = None, storageBucket = None):
        self.cred = credentials.Certificate(credantial)
        firebase_admin.initialize_app(self.cred, {
            'projectId': projectId,
            'storageBucket': storageBucket,
        })
        self.db = firestore.client()

    def reader(self, collection, document = None):
        """
this func can help you reads information from single-level fb-structure (collection -> document) or (collection)
        :param collection: name of collection from bd -> str
        :param document: name of a document from this collection (optional) -> str
        :return: dict with information from document or group of documents
        """
        if document:
            return self.db.collection(collection).document(document).get().to_dict()

        else:
            def infoGenerator(info):
                for i in info:
                    yield {i.id: i.to_dict()}

            docs = self.db.collection(collection).stream()
            return infoGenerator(docs)

    def sender(self, obvious_info: dict, collection, document, kind = 'new',pictures: dict = None):
        """
this function allow you add or update information in a single-level fb-structure (collection -> document)
        :param obvious_info: dict with {'field_name': 'value (dict, list, str, int)'}
        :param collection: name of collection from bd -> str
        :param document: name of a document from this collection -> str
        :param kind: what do you want to do with this document (add new - 'new', update old - 'update')
        :param pictures: dict with ('unique picture name': 'full path of this picture')
        """
        if pictures:
            for name in pictures.keys():
                path = pictures[name]
                URL = self.uploadImage(path, name)
                obvious_info[name] = URL

        if kind == 'new':
            self.db.collection(collection).document(document).set(obvious_info)
        elif kind == 'update':
            self.db.collection(collection).document(document).update(obvious_info)
        else:
            print('Are you an idiot???')

    def uploadImage(self, image_path, image_name):
        # Put your local file path
        bucket = storage.bucket()
        blob = bucket.blob(image_name + '.png')
        blob.upload_from_filename(image_path)

        # Opt : if you want to make public access from the URL
        blob.make_public()

        return (blob.public_url)
