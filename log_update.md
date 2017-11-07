Version 0.2
- We removed the big if/else/elif block of code and replaced it with a function that does that for us named "check_loop()"
- We re-coded
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
