import os.path

import cv2
import face_recognition
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facerecog-attendance-sys-default-rtdb.firebaseio.com/",
    'storageBucket' :  "facerecog-attendance-sys.appspot.com"
})

# Importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
imgList = []
studentIds = []
for path in pathList:
    imgList.append((cv2.imread(os.path.join(folderPath,path))))
    studentIds.append(os.path.splitext(path)[0])
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    #print(path)
    #print(os.path.splitext(path))
print(len(imgList))


def findEncodings(imagelist):
    encodeList=[]
    for img in imagelist:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
print("Encoding started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown,studentIds]
print("Encoding complete")

file = open("EncodingFile.p",'wb')
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("File Saved")