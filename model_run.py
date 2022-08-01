import cv2
import face_recognition as fr
import json
import pickle
import numpy as np

x = []
y = []

def model_load(model_path):
    global model
    model = pickle.load(open(model_path, 'rb'))

def embeddings(img_path):
    global x, y
    pic = cv2.imread(img_path)
    detected_pos = fr.face_locations(pic)
    for i in detected_pos:
        top, right, bottom, left = i
        face_image = pic[top:bottom, left:right]
        face_image = cv2.resize(face_image, (256, 256))
        face_embedding = fr.face_encodings(face_image)[0]
        x.append(face_embedding)
        # y.append(idx)
        
def run_embedding(img_path):
    pic = cv2.imread(img_path)
    face_embeddings = fr.face_encodings(pic)[0]
    test = np.asarray(face_embeddings)
    test=  np.reshape(test, (1, -1))
    return test
        
def run_test(img):
    class_f = open('classes.json')
    classes = json.load(class_f)
    # model = pickle.load(open("./model.pickle",'rb'))
    test_data = run_embedding(img)
    class_list = list(classes.keys())
    pred = model.predict_proba(test_data)[0]
    if np.max(pred) > 0.7:
        # print(classes[str(class_list[np.argmax(pred)])], np.max(pred))
        return (classes[str(class_list[np.argmax(pred)])])
    else:
        return ("Face not found!")


# def do():
#    img_path = 'IMAGE.png'
#    run_test(img_path)




# do()