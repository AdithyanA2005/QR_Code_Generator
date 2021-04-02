import os
import qrcode
from urllib.parse import unquote
from generator.settings import config
from generator.settings import name_remove_list


def qr_img_gen(qr_data):
    """
    This fucntion will create the qrcode
    """
    file = f"{config['qr_dir']}qrcode.png"
    qr_data = unquote(qr_data)
    qr = qrcode.QRCode(version=4, box_size=30, border=1)
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='red', back_color='white')
    delete_on_exist(file)
    img.save(file)


def create_qr_file(url):
    """
    This fuction will provide a valid filename for the qrcode
    """
    for words in name_remove_list:
        filename = url.replace(words, '')
    
    qr_file = f"{config['qr_dir']}{config['qr_brand']}{filename}{config['qr_extention']}"
    delete_on_exist(qr_file)
    return qr_file


def delete_on_exist(filename):
    """
    This fucntion will delete the existing file
    """
    if os.path.exists(filename):
        os.remove(filename)


def qr_img_del():
    print("delete")
