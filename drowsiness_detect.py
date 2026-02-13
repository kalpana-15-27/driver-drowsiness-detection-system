import cv2
import pygame

# --- INITIALIZATION ---
pygame.mixer.init()
try:
    sound = pygame.mixer.Sound("alarm.wav")
except:
    print("[WARNING] 'alarm.wav' not found.")
    sound = None

# Load Standard Detectors (These are built-in to OpenCV, no downloads needed)
# We use the default Haar Cascades for face and eyes
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
score = 0  # Counts how many frames your eyes are closed

print("[INFO] Starting Camera (OpenCV Method)...")

while True:
    ret, frame = cap.read()
    if not ret: break
    
    # Pre-processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        # Draw box around face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Focus only on the face area to find eyes
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        # Detect Eyes
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4)
        
        # LOGIC: If Face is detected BUT 0 eyes are detected -> Eyes are Closed
        if len(eyes) == 0:
            score += 1
            cv2.putText(frame, "Eyes Closed", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            score = 0
            cv2.putText(frame, "Eyes Open", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            # Draw boxes around eyes
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        
        # ALARM TRIGGER (If eyes closed for > 15 frames)
        if score > 15:
            cv2.putText(frame, "****************ALERT!****************", (10, 400),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            if sound: 
                sound.play()
            
    cv2.imshow('Drowsiness System', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()