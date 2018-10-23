import os
import sys
from PIL import Image
import random
from datetime import datetime
random.seed(datetime.now())

def take_photo(image_prefix, num_images=1, angle = 10.0, tilt = 0.0, distance = 2.0,
               bg_r = 1.0, bg_g = 1.0, bg_b = 1.0, obj_r = 1.0, obj_g = 1.0, obj_b = 1.0, img_sx = 960, img_sy = 540):
    start_angle = 270.0
    interval = 360.0 / num_images
    bg_color = str(bg_r)+","+str(bg_g)+","+str(bg_b)
    obj_color = str(obj_r)+","+str(obj_g)+","+str(obj_b)
    for i in range(0, num_images):
        image_name = image_prefix + str(i) + '.png'
        azimuth = start_angle + (interval*i)
        v = [azimuth, angle, tilt, distance]
        print ">> Selected view: ", v
        python_cmd = 'python %s -a %s -e %s -t %s -d %s -bg %s -oc %s -o %s' % (os.path.join(BASE_DIR, 'render_class_view.py'),
                                                                                str(v[0]), str(v[1]), str(v[2]), str(v[3]),
                                                                                bg_color, obj_color, os.path.join(syn_images_folder, model_name, image_name))
        print ">> Running rendering command: \n \t %s" % (python_cmd)
        os.system('%s %s' % (python_cmd, io_redirect))
        # show result
        print(">> Displaying rendered image ...")
        im = Image.open(os.path.join(syn_images_folder, model_name, image_name))
        im.show()

        im.resize((img_sx, img_sy))
        im.save(os.path.join(syn_images_folder, model_name, image_name))


#start code from here
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR,'../'))
from global_variables import *

# set debug mode
debug_mode = 1

if debug_mode:
    io_redirect = ''
else:
    io_redirect = ' > /dev/null 2>&1'

# -------------------------------------------
# RENDER
# -------------------------------------------

# set filepath
syn_images_folder = os.path.join(BASE_DIR, 'demo_images')
model_name = 'chair001'
image_prefix = 'demo_img'
if not os.path.exists(syn_images_folder):
    os.mkdir(syn_images_folder)
    os.mkdir(os.path.join(syn_images_folder, model_name))






take_photo(image_prefix, num_images=1, distance=3.5,bg_r=1.0, bg_g=1.0, bg_b=1.0, obj_r=(170.0/255), obj_g=(170.0/255), obj_b=(170.0/255))