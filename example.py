import pyascii

my_img = pyascii.Pyascii(
        "/home/puka/Desktop/Mona_Lisa.jpg",
        "/home/puka/Desktop/test6.jpg",
        enh_color=2.0
        )
my_img.default_convert()
my_img.image_show()
my_img.image_save()
