import cv2
import os
import image_to_console
import pickle as pk

debug = True

# Path to the video file
video_path = 'RocketBoys-small.mp4'

# Open the video
cap = cv2.VideoCapture(video_path)

frame_count = 0
frames = []
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # End of video

    frames += [frame]
    frame_count += 1

cap.release()

print(len(frames), type(frames[0]), len(frames[0]), len(frames[0][0]))


console_frames = []
count = 0

if debug:    
    file_ = open("video_pickle.pk", "rb")
    console_frames = pk.load(file_)
    file_.close()
else:
    for frame_ in frames:
        print(count)
        count += 1
        if count%9==0:
            console_frames += [  image_to_console.get_console_matrix_from_numpy_ndarray(frame_)    ]
    file_ =  open('video_pickle.pk', 'wb')
    pk.dump(console_frames, file_)
    file_.close()



# print console frames for video on console

for console_matrix_ in console_frames:
    image_to_console.print_image_on_console(console_matrix_)
    os.system("cls")

