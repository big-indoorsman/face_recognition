import face_recognition
import pickle
import csv
#打开存储信息表的csv文件，也可以直接存到数据库中
with open('picture.csv','r') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    name,path= [], []
    for row in reader:
        name.append(row[0])
        path.append(row[1])
known_face_encodings=[]
for i in path:
    #根据路径打开图片，信息表里的路径不能包含中文，否则无法读取
    img = face_recognition.load_image_file(i)
    #将图片中的人脸特征数据转换成数组
    locations = face_recognition.face_locations(img)
    face_encodings = face_recognition.face_encodings(img, locations)[0]#假定每张图片只有一张脸以及对应的姓名，如果超出一个人，则取第一组数据
    known_face_encodings.append(face_encodings)
known_names=name
#将名字与人脸特征数据存储到pickle文件中
file = open('show_name.pkl', 'wb')
pickle.dump(known_names, file)
file1 = open('show_data.pkl', 'wb')
pickle.dump(known_face_encodings, file1)
