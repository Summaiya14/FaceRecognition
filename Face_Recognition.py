import face_recognition

#image = face_recognition.load_image_file('./images/group1.jpg')
#face_locations = face_recognition.face_locations(image)

#print(face_locations)
#print(f'There are {len(face_locations)} people in this image')

img1 = face_recognition.load_image_file('./images/img.jpg')
img1_encoding = face_recognition.face_encodings(img1)[0]

img2 = face_recognition.load_image_file('./images/boy.jpg')
img2_encoding = face_recognition.face_encodings(img2)[0]

results = face_recognition.compare_faces([img1_encoding], img2_encoding)

if results[0]:
    print('Match Found')

else: 
    print('Match Not Found')

