import cv2

rastreador = cv2.TrackerCSRT_create()

video = cv2.VideoCapture(
    r'C:\IA_e_Machine_Learning\1.3-Visao_computacional\videos\rua.mp4'
)
ok, frame = video.read()

bbox = cv2.selectROI(frame)

ok = rastreador.init(frame, bbox)

while True:
    ok, frame = video.read()
    if not ok:
        break

    ok, bbox = rastreador.update(frame)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, 1)
    else:
        cv2.putText(
            frame, 'Erro no rastreamento', (100, 80),
            cv2.FONT_HERSHEY_SIMPLEX, .75, (0, 0, 255), 2
        )
    cv2.imshow('Rastreamento', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
