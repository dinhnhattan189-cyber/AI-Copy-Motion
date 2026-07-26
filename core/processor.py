from core.remove_bg import remove_background
from core.motion import copy_motion
from core.render import render_video


def process(image, video, background):

    print("Đang tách nền...")

    person = remove_background(image)


    print("Đang copy chuyển động...")

    motion = copy_motion(
        person,
        video
    )


    print("Đang render video...")

    output = render_video(
        motion,
        background
    )


    return output