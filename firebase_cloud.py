import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from SDK import credan
json_info = {
    "info from SDK json": "__________________"
}

cred = credentials.Certificate(json_info)
firebase_admin.initialize_app(cred)

db = firestore.client()

# ----> for taking all info from YOUR_COLLECTION <------
users_ref = db.collection('YOUR_COLLECTION')
docs = users_ref.stream()
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
# ------------------------------------------------------

# ----> for taking info from one document in YOUR_COLLECTION <-----
users_ref = db.collection('YOUR_COLLECTION').document('NAME_OF_YOUR_DOCUMENT').get().to_dict()
print(users_ref)
# ------------------------------------------------------
