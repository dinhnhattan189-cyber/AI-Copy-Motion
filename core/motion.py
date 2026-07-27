from moviepy.editor import ImageClip
import os


class MotionEngine:

    def create_motion(self, image_path):

        if image_path is None:
            return None

        output_folder = "outputs"
        os.makedirs(output_folder, exist_ok=True)

        output_path = os.path.join(output_folder, "motion_preview.mp4")

        clip = (
            ImageClip(image_path)
            .set_duration(5)
            .resize(height=720)
            .set_position("center")
        )

        clip.write_videofile(
            output_path,
            fps=30,
            codec="libx264",
            audio=False
        )

        return output_path