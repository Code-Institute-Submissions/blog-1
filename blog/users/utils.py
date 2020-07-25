import os
import secrets
from PIL import Image
from flask import current_app

# Picture saving function
def save_profile_pic(profile_pic):
    # Generating random hex name for picture and saving original extension.
    pic_name = secrets.token_hex(8)
    _, f_ext = os.path.splitext(profile_pic.filename)
    pic_fn = pic_name + f_ext
    pic_path = os.path.join(current_app.root_path, "static", "profle_pics", pic_fn)
    # Resizing picture in order to save memory.
    output_size = (125, 125)
    resized_pic = Image.open(profile_pic)
    resized_pic.thumbnail(output_size)
    resized_pic.save(pic_path)
    return pic_fn