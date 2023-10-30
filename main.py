from ultralytics import YOLO
import cv2
import math 
# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# model
model = YOLO("yolo-Weights/yolov8n.pt")

# object classes
classNames = ["insan", "bisiklet", "araba", "motorsiklet", "ucak", "otobus", "tren", "kamyon", "bot",
              "trafik isigi", "yangin sondurucu", "dur tabelasi", "park sayici", "bank", "kus", "kedi",
              "kopek", "at", "koyun", "inek", "fil", "ayi", "zebra", "zurafa", "sirt cantasi", "semsiye",
              "el cantasi", "kravat", "bavul", "frizbi", "kayak", "snowboard", "spor topu", "ucurtma", "beyzbol sopasi",
              "beyzbol eldiveni", "kaykay", "sorf tahtasi", "tenis raketi", "sise", "sarap kadehi", "fincan",
              "catal", "bicak", "kasik", "kase", "muz", "elma", "sandvic", "portakal", "brokoli",
              "havuc", "sosisli sandvic", "pizza", "corek", "kek", "sandalye", "kanepe", "saksi bitkisi", "yatak",
              "yemek masasi", "tuvalet", "tvmonitor", "dizustu bilgisayar", "fare", "uzaktan kumanda", "klavye", "telefon",
              "mikrodalga", "firin", "ekmek kizartma makinesi", "lavabo", "buzdolabi", "kitap", "saat", "vazo", "makas",
              "oyuncak ayi", "sac kurutma makinesi", "dis fircasi"
              ]


while True:
    success, img = cap.read()
    results = model(img, stream=True)

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # confidence
            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence --->",confidence)

            # class name
            cls = int(box.cls[0])
            print("Class name -->", classNames[cls])

            # object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()