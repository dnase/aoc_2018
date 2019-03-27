# original code modified from https://rosettacode.org/wiki/Voronoi_diagram#Python
from PIL import Image
import random
import math
from util import parse_file

def generate_voronoi_diagram(width, height, num_cells, coords):
    image = Image.new("RGB", (width, height))
    putpixel = image.putpixel
    imgx, imgy = image.size
    nx = []
    ny = []
    nr = []
    ng = []
    nb = []

    for c in coords:
        nx.append(c[0])
    	ny.append(c[1])
        nr.append(random.randrange(256))
    	ng.append(random.randrange(256))
    	nb.append(random.randrange(256))
    for y in range(imgy):
    	for x in range(imgx):
    		dmin = abs(imgx-1) + abs(imgy-1)
    		j = -1
    		for i in range(num_cells):
    			d = abs(nx[i]-x) + abs(ny[i]-y)
    			if d < dmin:
    				dmin = d
    				j = i
    		putpixel((x, y), (nr[j], ng[j], nb[j]))
    for c in coords:
        putpixel((c[0], c[1]), (255, 255, 255))
    image.save("VoronoiDiagram.png", "PNG")
    image.show()

def parsefunc(s):
    buff = [n.strip() for n in s.split(",")]
    return (int(buff[0]), int(buff[1]))

seq = get_data(6, parsefunc)

generate_voronoi_diagram(400, 400, len(seq), seq)
