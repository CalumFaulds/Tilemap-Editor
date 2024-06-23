import pygame
pygame.init()
clock = pygame.time.Clock()
blocksize = 80
running = True
window = pygame.display.set_mode((1920,1080))
blockid = 1
file = int(input("please type id"))
type = input("what preset? [b]order, [f]illed, [back]ground? ")
txt = ""
height = 16
width = 16
row = 0
def check(id):
    return int(id) in [1,4]
for a in range(height):
    print (txt)
    if type == "back":
        for b in range (width):
            if b == 0:
                txt += "2"
            elif b != 15:
                txt += " 2"
            if b == 15:
                txt += " 2\n"
    if type == "f":
        for b in range (width):
            if b == 0:
                txt += "1"
            elif b != 15:
                txt += " 1"
            if b == 15:
                txt += " 1\n"
    if type == "b":
        for b in range (width):
            print (b)
            if row == 0 or row == 15:
                    if b == 0:
                        txt += "1"
                    elif b != 15:
                        txt += " 1"
                    if b == 15:
                        txt += " 1\n"
                        row += 1
            else:
                if b == 0:
                    txt += "1"
                elif b != 15: 
                    txt += " 2"
                if b == 15:
                    txt += " 1\n"
                    row += 1

with open("%s.tilemap" % file, "w") as text_file:
    text_file.write(str(txt))
def load_tilemap(id):
    tilemap = []
    with open("%s.tilemap" % id, "r") as tilemap_file:
        lines = [x.strip("\n").strip(" ") for x in tilemap_file.readlines()]
    for line in lines:
        tilemap.append([int(x) for x in line.split(" ")])
    return tilemap

tilemap = load_tilemap(file)
def draw():
    window.fill((255,255,255))
tiles = {}
def export(id):
    string = ""
    for row in tilemap:
        row_str = " ".join([str(x) for x in row])
        string += str(row_str)
        string += "\n"
    with open("%s.tilemap" % id, "w") as text_file:
        text_file.write(string)
egg = 400
def refresh(a, i):
    try:
        if not check(tilemap[a - 1][i]) and check(tilemap[a][i]): 
            tilemap[a][i] = 4.0
            print (a+1)
            print (i+1)
        if not check(tilemap[a][i-1]) and check(tilemap[a][i]):
            tilemap[a][i] = 4.03
        if not check(tilemap[a][i+1]) and check(tilemap[a][i]):
            tilemap[a][i] = 4.01
        if not check(tilemap[a+1][i]) and check(tilemap[a][i]):
            tilemap[a][i] = 4.02
        if not check(tilemap[a][i-1]) and not check(tilemap[a-1][i]) and check(tilemap[a][i]):
            tilemap[a][i] = 4.07
        if not check(tilemap[a][i-1]) and not check(tilemap[a+1][i]) and check(tilemap[a][i]):
            tilemap[a][i] = 4.06
        if not check(tilemap[a][i+1]) and not check(tilemap[a+1][i]) and check(tilemap[a][i]):
            tilemap[a][i] = 4.05
        if not check(tilemap[a][i+1]) and not check(tilemap[a-1][i]) and check(tilemap[a][i]):
            tilemap[a][i] = 4.04
        if not check(tilemap[a][i+1]) and not check(tilemap[a][i-1]) and check(tilemap[a][i]):
            tilemap[a][i] = 4.14
        if not check(tilemap[a+1][i]) and not check(tilemap[a-1][i]) and check(tilemap[a][i]):
            tilemap[a][i] = 4.13
        if not check(tilemap[a-1][i]) and not check(tilemap[a][i+1]) and not check(tilemap[a][i-1]) and check(tilemap[a][i]):
            tilemap[a][i] = 4.08
        if not check(tilemap[a-1][i]) and not check(tilemap[a][i+1]) and not check(tilemap[a+1][i]) and check(tilemap[a][i]):
            tilemap[a][i] = 4.09
        if not check(tilemap[a+1][i]) and not check(tilemap[a][i+1]) and not check(tilemap[a][i-1]) and check(tilemap[a][i]):
            tilemap[a][i] = 4.1
        if not check(tilemap[a-1][i]) and not check(tilemap[a+1][i]) and not check(tilemap[a][i-1]) and check(tilemap[a][i]):
            tilemap[a][i] = 4.11
        if not check(tilemap[a-1][i]) and not check(tilemap[a][i+1]) and not check(tilemap[a][i-1]) and not check(tilemap[a+1][i]) and check(tilemap[a][i]):
                tilemap[a][i] = 1
        if  check(tilemap[a-1][i]) and  check(tilemap[a][i+1]) and  check(tilemap[a][i-1]) and check(tilemap[a+1][i]) and check(tilemap[a][i]):
            tilemap[a][i] = 4.15
        if a == 0 or a == 15:
            tilemap[a][i] = 6
        if i == 0 or i == 16:
            tilemap[a][i] = 6
    except:
        pass

for i in range(1,8):
    tiles[i] = pygame.transform.scale(pygame.image.load("tiles/%s.png" % i).convert_alpha(), (blocksize, blocksize))
    if i == 4:
        for b in range (16):
            tiles[egg/100] = pygame.transform.scale(pygame.image.load("tiles/%s.png" % (egg/100)).convert_alpha(), (blocksize, blocksize))
            egg += 1
playerX = 0
playerY = 0
while running: 
    dt = clock.tick(60)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX += blocksize
            if event.key == pygame.K_LEFT:
                playerX -= blocksize
            if event.key == pygame.K_UP:
                playerY -= blocksize
            if event.key == pygame.K_DOWN:
                playerY += blocksize
            if event.key == pygame.K_e:
                if blockid <7:
                    blockid += 1
            if event.key == pygame.K_q:
                if blockid > 1 :
                    blockid -= 1
            if event.key == pygame.K_j:
                export(file)
    draw()
    if keys[pygame.K_p]:
        for a in range(len(tilemap)):
            for i in range(len(tilemap[a])):
                refresh(a,i)
    indexX = int((playerX + 880) / blocksize)
    indexY = int((playerY + 460) / blocksize)
   # print(indexX, indexY)
    for a in range(len(tilemap)):
        for i in range(len(tilemap[a])):
            window.blit(tiles[tilemap[a][i]], (i*blocksize - playerX, a*blocksize - playerY))
    window.blit(tiles[blockid],(880, 540-140))
    
    if keys[pygame.K_SPACE]:
        try:
            tilemap[indexY][indexX] = blockid

        except:
            pass

    pygame.display.update()

pygame.quit()