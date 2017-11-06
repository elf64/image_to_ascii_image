from PIL import Image, ImageFont, ImageDraw, ImageEnhance

# Version 0.1

class Pyascii:
    def __init__(
            self,
            image_path,
            save_path,
                ):
        self.image_path = image_path
        self.save_path = save_path
        self.default_chars = list("_.:-=fg#%\\")
        self.block_size = 8
        self.font_size = 12
        self.font = "Anonymous_Pro.ttf"
        self.char_brightness_list = self.char_brightness()
        self.dict_test = {
            self.default_chars[k]: self.char_brightness_list[k]
            for k in range(10)
        }
        self.image = Image.open(self.image_path)
        self.font = ImageFont.truetype(self.font, self.font_size)
        self.rgb_image = self.image.convert("RGB")
        self.final_image = Image.new(self.rgb_image.mode, self.rgb_image.size, "black")
        self.w, self.h = self.image.size
        self.draw = ImageDraw.Draw(self.final_image)

    def avg_brightness_pixel(self, r, g, b):
        # Returns the average brightness value of a pixel
        return (r + g + b) / 3

    def default_convert(self):
        # Default function to convert an image to a ascii image
        for i in range(0, self.w, self.block_size):
            for j in range(0, self.h, self.block_size):
                r, g, b = self.rgb_image.getpixel((i, j))
                avg_brg = self.avg_brightness_pixel(r, g, b)
                # Find a better way to get the average rgb value for a subgroup of pixels
                # so we can have better colors on the image
                color = (r, g, b)
                # These if/else/elif needs to be removed!
                if avg_brg < self.char_brightness_list[0]:
                    self.draw_text(self.default_chars[0], self.draw, i, j, self.font, color)
                elif avg_brg >= self.char_brightness_list[0] and avg_brg < self.char_brightness_list[1]:
                    self.draw_text(self.default_chars[1], self.draw, i, j, self.font, color)
                elif avg_brg >= self.char_brightness_list[1] and avg_brg < self.char_brightness_list[2]:
                    self.draw_text(self.default_chars[2], self.draw, i, j, self.font, color)
                elif avg_brg >= self.char_brightness_list[2] and avg_brg < self.char_brightness_list[3]:
                    self.draw_text(self.default_chars[3], self.draw, i, j, self.font, color)
                elif avg_brg >= self.char_brightness_list[3] and avg_brg < self.char_brightness_list[4]:
                    self.draw_text(self.default_chars[4], self.draw, i, j, self.font, color)
                elif avg_brg >= self.char_brightness_list[4] and avg_brg < self.char_brightness_list[5]:
                    self.draw_text(self.default_chars[5], self.draw, i, j, self.font, color)
                elif avg_brg >= self.char_brightness_list[5] and avg_brg < self.char_brightness_list[6]:
                    self.draw_text(self.default_chars[6], self.draw, i, j, self.font, color)
                elif avg_brg >= self.char_brightness_list[6] and avg_brg < self.char_brightness_list[7]:
                    self.draw_text(self.default_chars[7], self.draw, i, j, self.font, color)
                elif avg_brg >= self.char_brightness_list[7] and avg_brg < self.char_brightness_list[8]:
                    self.draw_text(self.default_chars[8], self.draw, i, j, self.font, color)
                else:
                    self.draw_text(self.default_chars[9], self.draw, i, j, self.font, color)

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
        self.final_image.save(self.save_path)

    def default_show(self):
        # Show the default image
        self.image.show()
