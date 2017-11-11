from PIL import Image, ImageFont, ImageDraw, ImageEnhance

# Version 0.3


class Pyascii:
    def __init__(
            self,
            image_path,
            save_path,
            chars=None,
            enh_color=None,
            enh_brg=None,
            font_path=None,
            rgb_color=None,
            optimize=False,
            quality=100
                ):
        self.optimize = optimize
        self.quality = quality
        self.rgb_color = rgb_color
        self.enh_color = enh_color
        self.enh_brg = enh_brg
        self.image_path = image_path
        self.save_path = save_path
        self.bg_color = "black"
        # (0, 0, 0)
        # If no color is provided to bg_color PIL library will by
        # default set the background color to black.
        # If we set the new image mode to RGBA and bg_color is None
        # the image will have no background
        self.default_chars = list("_^:-=fg#%@") if chars == None else chars
        # _.:-=fg#%@    -> First char list
        # ^.:-=fg#%\\   -> Second char list
        self.block_size = 6
        self.font_size = 12
        # Some good block size  -> 6    }
        # Some good font size   -> 12   } Resolution 1024x768
        # and with img.enhance_color(2.0)
        # without brightness enhancement
        self.font = "Anonymous_Pro.ttf" if font_path == None else font_path
        self.char_brightness_list = self.char_brightness()
        self.image = Image.open(self.image_path)
        self.font = ImageFont.truetype(self.font, self.font_size)
        self.rgb_image = self.image.convert("RGB")
        self.final_image = Image.new(self.rgb_image.mode, 
                        self.rgb_image.size, self.bg_color)
        self.w, self.h = self.image.size
        self.draw = ImageDraw.Draw(self.final_image)

    def avg_brightness_pixel(self, r, g, b):
        # Returns the average brightness value of a pixel
        return (r + g + b) / 3

    def default_convert(self):
        # Default function to convert an image to a ascii image
        self.print_info()
        for i in range(0, self.w, self.block_size):
            for j in range(0, self.h, self.block_size):
                r, g, b = self.rgb_image.getpixel((i, j))
                avg_brg = self.avg_brightness_pixel(r, g, b)
                r_list = []
                g_list = []
                b_list  = []
                for x in range(i, i+self.block_size):
                    for y in range(j, j+self.block_size):
                        #print(x, y)
                        try:
                            # The error
                            # "IndexError: image index out of range"
                            # might happen if the block size is a certain
                            # number -> for ex. 6
                            r2, g2, b2 = self.rgb_image.getpixel((x, y))
                        except IndexError as e:
                            pass
                            
                        r_list.append(r2)
                        g_list.append(g2)
                        b_list.append(b2)
                try:
                    color = (
                            int(sum(r_list) / float(len(r_list))),
                            int(sum(g_list) / float(len(g_list))),
                            int(sum(b_list) / float(len(b_list)))
                            ) if self.rgb_color == None else self.rgb_color
                except:
                    pass
                
                self.draw_text(self.default_chars[self.check_loop(avg_brg)],
                        self.draw, i, j, self.font, color)
        if self.enh_color != None: 
            self.enhance_color(self.enh_color)
        if self.enh_brg != None:
            self.enhance_brightness(self.enh_brg)

    def check_loop(self, value):
        # We're doing a loop in range 10 (length of the ascii chars we use)
        # and it returns what index of the ascii character we need to use
        for i in range(len(self.default_chars)):
            if value < self.char_brightness_list[i]:
                return i
            elif (value >= self.char_brightness_list[i-1] and
                        value < self.char_brightness_list[i]):
                return i

    def image_show(self):
        # Show the ascii image
        self.final_image.show()

    def char_brightness(self):
        # Will return a list of all the brightness values for each character
        # in the charset
        amount_levels = len(self.default_chars)
        inner_list = []
        for i in range(amount_levels):
            level_brightness = (i + 1) * (255 / amount_levels)
            inner_list.append(level_brightness)
        return inner_list

    def draw_text(self, char, draw, x, y, font, color):
        # Draw the char into the new image we created (self.final_image)
        # at x, y with the default font + default color
        return draw.text((x, y), char, font=font, fill=color)

    def enhance_color(self, value=1.0):
        # Enhance the color of the final image
        # Default value is 1.0
        # - 0.0 for gray
        # - 1.0 default
        # - 2.0 enhanced :D
        enhancer = ImageEnhance.Color(self.final_image)
        self.final_image = enhancer.enhance(value)

    def enhance_brightness(self, value=1.0):
        # Enhance the brightness of the image
        # Default value is 1.0
        enhancer = ImageEnhance.Brightness(self.final_image)
        self.final_image = enhancer.enhance(value)

    def print_info(self):
        # Print info about the original image, font, chars used, width + height
        print(f"Size: {self.w}, {self.h}\nImage Path: {self.image_path}\nFont: {self.font.getname()}"
              f"\nChars used: {self.default_chars}")

    def image_save(self):
        # Save the final image to the specified path
        # Optimize=True -> Default=False
        # quality       -> Default=None
        self.final_image.save(
                self.save_path, 
                optimize=self.optimize,
                quality=self.quality
                )

    def default_show(self):
        # Show the default image
        self.image.show()
