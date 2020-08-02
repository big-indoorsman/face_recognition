import cv2
import face_recognition
import ft2
import pickle

def face_in_camera():
    # pickle文件提取
    f1 = open('show_name.pkl', 'rb')
    known_names = pickle.load(f1)
    f = open('show_data.pkl', 'rb', )
    known_face_encodings = pickle.load(f)
    # opencv
    vc = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while True:
        # 获取视频中每一帧的图片
        ret, img = vc.read()
        if not ret:
            print('没有捕获到视频！')
            break
        locations = face_recognition.face_locations(img)
        face_encodings = face_recognition.face_encodings(img, locations)
        for (top, right, bottom, left), face_encoding in zip(locations, face_encodings):
            matchs = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.44)
            name = '不在信息表里！'
            for match, known_name in zip(matchs, known_names):
                if match:
                    name = known_name
                    break
            cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
            ft = ft2.put_chinese_text('msyh.ttf')
            try:
                img = ft.draw_text(img, (left - 30, bottom + 10), name, 20, (0, 0, 255))
            except:
                pass
        cv2.imshow('Video', img)
        if cv2.waitKey(1) != -1:
            # 6.关闭视像头，释放资源
            vc.release()
            cv2.destroyAllWindows()
            break


