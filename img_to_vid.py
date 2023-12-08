from moviepy.editor import VideoFileClip
from moviepy.editor import ImageSequenceClip
import glob

fps = 20

image_paths = glob.glob('../input/lisa_traffic_light_dataset/lisa-traffic-light-dataset/daySequence1/daySequence1/frames/*.jpg')
image_paths.sort()
print(image_paths[:5])
clip = ImageSequenceClip(image_paths, fps=fps)
clip.write_videofile('../input/lisa_traffic_light_dataset/input/test_data/day_seq1.mp4', fps=fps)
print('DONE')