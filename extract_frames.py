import cv2
import os

def extract_frames(video_path, output_folder):
    # Open the video file
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print("Error: Unable to open video file.")
        return

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get some video properties
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(video.get(cv2.CAP_PROP_FPS))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(f"Total frames: {total_frames}, FPS: {fps}, Resolution: {width}x{height}")

    # Loop through each frame and save it
    success, frame = video.read()
    count = 0
    while success:
        frame_path = os.path.join(output_folder, f"frame_{count}.jpg")
        cv2.imwrite(frame_path, frame)  # Save the frame as an image
        success, frame = video.read()
        count += 1

    print(f"Frames extracted: {count}")

    # Release video object
    video.release()

if __name__ == "__main__":
    video_path = "video.mp4"  # Video file path
    output_folder = "frames"  # Output folder path
    extract_frames(video_path, output_folder)
