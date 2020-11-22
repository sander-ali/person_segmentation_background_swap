#pip install pixellib
import pixellib
from pixellib.tune_bg import alter_bg

#Download the model from the repository first
change_bg = alter_bg(model_type = "pb")
change_bg.load_pascalvoc_model("ali_xcep_pascalvoc.pb")
#for blurring the background
change_bg.blur_video("2.mp4", extreme = True, frames_per_second=10, detect="person", output_video_name="blur_video.mp4")

#for changing the background
change_bg.change_video_bg("2.mp4", "bg.jpg", frames_per_second = 10, detect="person", output_video_name="output_video.mp4")

