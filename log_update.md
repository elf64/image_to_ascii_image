Version 0.3
- Added chars,enh_color,enh_brg,font_path,rgb_color,optimize,quality arguments
```
chars       -> Default is None  . (needs to be a list)
enh_color   -> Default is None  . Value Ex: 1.0 / 2.0 / 3.0 etc..
enh_brg     -> Default is None  . Value Ex: 1.0 / 2.0 / 3.0 etc..
font_path   -> Default is None  . The path to the font we want to use
rgb_color   -> Default is None  . The color we want the picture to be (white, blue, green or (0, 0, 0) (255, 255, 255)
optimize    -> Default is False . If we want to save space when saving the picture
quality     -> Default is None  . Picture quality when we save it 10, 50, 70 ...
```
- Found a way around the blocksize bug when it throws IndexError

Version 0.2
- Removed the big if/else/elif block of code and replaced it with a function that does that for us named "check_loop()"
- Re-coded
```python
color = (r, g, b)
# We replaced this with
color = (255, 255, 255) # <- this is not necessary 
r_list = []
g_list = []
b_list  = []
for x in range(i, i+self.block_size):
    for y in range(j, j+self.block_size):
        r2, g2, b2 = self.rgb_image.getpixel((x, y))
        r_list.append(r2)
        g_list.append(g2)
        b_list.append(b2)
# I don't think this try/except is needed anymore but i'm too lazy to check >.<
try:
    color = (
            int(sum(r_list) / float(len(r_list))),
            int(sum(g_list) / float(len(g_list))),
            int(sum(b_list) / float(len(b_list)))
            )
except:
    pass
```
