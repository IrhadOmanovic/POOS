# -*- coding: cp1252 -*-
import face_recognition
import os

trenutni = os.getcwd();
print("Current Working Directory " , os.getcwd())

#predefinisana 4 lica koja prepoznajemo
os.chdir(trenutni + "\p")
obama = face_recognition.load_image_file("obama.jpg")
bush = face_recognition.load_image_file("bush.jpg")
irhad = face_recognition.load_image_file("irhad.jpg")
keanu = face_recognition.load_image_file("keanu.jpg")

os.chdir(trenutni + "\\np")

print(os.listdir())
lista_nepoznatih_slika = os.listdir();


    

obama_encoding = face_recognition.face_encodings(obama)[0]
bush_encoding = face_recognition.face_encodings(bush)[0]
irhad_encoding = face_recognition.face_encodings(irhad)[0]
keanu_encoding = face_recognition.face_encodings(keanu)[0]

known_faces = [
    obama_encoding,
    bush_encoding,
    irhad_encoding,
    keanu_encoding
]

known_faces_names = [
    "Obama",
    "Bush",
    "Irhad",
    "Keanu"
]

for k in range(len(lista_nepoznatih_slika)):
    unknown_image = face_recognition.load_image_file(lista_nepoznatih_slika[k])
    unknown_encoding = face_recognition.face_encodings(unknown_image)
    rez = []
    for i in unknown_encoding:
        rez.append(face_recognition.compare_faces(known_faces, i)) #lista nizova koji sadrze informacije o licima(da li je bush¡ ili obama)

    for lice in rez:
        for j in range(len(known_faces)):
            if lice[j] == 1:
                print("Na slici "+ str(k) + " je " + known_faces_names[j])
                break
