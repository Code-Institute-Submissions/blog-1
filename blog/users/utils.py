import os
import secrets
from flask import current_app
from PIL import Image

# Rename and save profile picture from form.
def save_profile_pic(profile_pic):
    pic_name = secrets.token_hex(8)
    _, f_ext = os.path.splitext(profile_pic.filename)
    pic_fn = pic_name + f_ext
    pic_path = os.path.join(current_app.root_path, "static", "profile_pics", pic_fn)

    output_size = (125, 125)
    resized_pic = Image.open(profile_pic)
    resized_pic.thumbnail(output_size)
    resized_pic.save(pic_path)

    return pic_fn