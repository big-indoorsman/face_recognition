import face_recognition
import ft2
import pickle
import cv2

def face_picture(path):
    #提取pickle文件的数据
    f1 = open('show_name.pkl', 'rb')
    known_names = pickle.load(f1)
    f = open('show_data.pkl', 'rb',)
    known_face_encodings = pickle.load(f)
    #导入图片
    img = cv2.imread(path)
    #缩小图片，防止图片过大，不能完全显示在界面中
    a = img.shape
    b = a[1] / 500
    img = cv2.resize(img, (int(a[1] / b), int(a[0] / b)), interpolation=cv2.INTER_CUBIC)
    #提取要测试图片的人脸特征
    locations = face_recognition.face_locations(img)
    face_encodings = face_recognition.face_encodings(img, locations)
    #将测试的人脸特征与存储的人脸特征进行匹配，若不匹配，则输出‘不在信息表里！’
    for (top, right, bottom, left), face_encoding in zip(locations, face_encodings):
        matchs = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.4)
        name = '不在信息表里！'
        #将匹配数据与名字做成字典
        for match, known_name in zip(matchs, known_names):
            if match:
                name = known_name
                break
        #在人脸的区域画框
        cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
        #实现在图片上打印汉字，msyh.ttf为字体，ft2.py为引用该字体的文件
        ft = ft2.put_chinese_text('msyh.ttf')
        #防止人脸显示不全，导致代码崩溃
        try:
            img = ft.draw_text(img, (left - 30, bottom + 10), name, 30, (0, 255, 255))
        except:
            pass
    #输出最终带有姓名和人脸框的图片
    cv2.imshow('picture', img)
    cv2.waitKey(0)
