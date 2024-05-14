import pygame as pg
import time
from pygame_plus.game_math import *




def FPS(clock):
    fps = clock.get_fps()
    return int(fps)


#def viewing_angle(player_x, player_y, wall_pos):
    #player_x = player_x
    #player_y = player_y
    #pos1, pos2, pos3, pos4 = wall_pos

    #gtlist = {}
    #for w in wall_pos:
        #xx = max(w[0], player_x)
        #xn = min(w[0], player_x)
        #yx = max(w[1], player_y)
        #yn = min(w[1], player_y)
        #a = xx - xn
        #b = yx - yn

        #ggg = game_math.gip(a, b)
        #gtlist[w] = ggg
    #print(gtlist)


def diagonal(player_x, player_y, wall_pos):
    pos1, pos2, pos3, pos4 = wall_pos
    if player_x <= pos1[0] and player_y <= pos1[1]:
        return -1
    if player_x <= pos2[0] and player_y >= pos2[1]:
        return -2
    if player_x >= pos3[0] and player_y >= pos3[1]:
        return -3
    if player_x > pos4[0] and player_y <= pos4[1]:
        return -4
    else:
        if player_y >= pos1[1] and player_y <= pos2[1]:
            if player_x <= pos1[0]:
                return 0
            elif player_x >= pos1[0]:
                return 2
        if player_x >= pos1[0] and player_x <= pos4[0]:
            if player_y < pos1[1]:
                return 1
            elif player_y >= pos1[1]:
                return 3

def ffeg(player_x, player_y, wall_pos):
    pos1, pos2, pos3, pos4 = wall_pos
    dg = diagonal(player_x, player_y, wall_pos)


    gtlist = {}
    #for w in wall_pos:
    #    xx = max(w[0], player_x)
    #    xn = min(w[0], player_x)
    #    yx = max(w[1], player_y)
    #    yn = min(w[1], player_y)
    #    a = xx - xn
    #    b = yx - yn

    #    ggg = game_math.gip(a, b)
    #    gtlist[ggg] = w
    #sn = sorted(gtlist)

    if dg is not None:
        if dg == -1:
            return (pos2, pos4)
        if dg == -2:
            return (pos1, pos3)
        if dg == -3:
            return (pos2, pos4)
        if dg == -4:
            return (pos1, pos3)
        if dg == 0:
            return (pos1, pos2)
        elif dg == 1:
            return (pos1, pos4)
        elif dg == 2:
            return (pos3, pos4)
        elif dg == 3:
            return (pos2, pos3)


    #return #sn[0], sn[1]

def darkened_pos(player_x, player_y, wall_pos, width, height):
    player_x, player_y = player_x+5, player_y+5
    #pos1, pos2, pos3, pos4 = wall_pos
    side = diagonal(player_x, player_y, wall_pos)
    ff = ffeg(player_x, player_y, wall_pos)
    start_pos1 = ff[0]
    start_pos2 = ff[1]

    if side == 0 or side == -1 or side == 1 or side == -4:
        rx1 = start_pos1[0] - player_x
        ry1 = start_pos1[1] - player_y
        rx2 = start_pos2[0] - player_x
        ry2 = start_pos2[1] - player_y
    else:
        rx1 = player_x - start_pos1[0]
        ry1 = player_y - start_pos1[1]
        rx2 = player_x - start_pos2[0]
        ry2 = player_y - start_pos2[1]

    if rx1 == 0: rx1 = 1
    if ry1 == 0: ry1 = 1
    if rx2 == 0: rx2 = 1
    if ry2 == 0: ry2 = 1

    if side == 0 or side == -1:
        tg1 = tg(ry1, rx1)
        sp1 = opposite_side(tg1, width - start_pos1[0])
        end_pos1 = (width, sp1)

        tg2 = tg(ry2, rx2)
        sp2 = opposite_side(tg2, width - start_pos2[0])
        end_pos2 = (width, start_pos2[1]+sp2)

        sspos = end_pos2

    elif side == 1 or side == -4:

        tg1 = tg(rx1, ry1)
        sp1 = opposite_side(tg1, height - start_pos1[1])
        end_pos1 = (sp1, height)

        if side == -4:
            tg2 = tg(ry2, rx2)
            sp2 = opposite_side(tg2, start_pos2[0])
            end_pos2 = (0, start_pos2[1] - sp2)
        else:
            tg2 = tg(ry2, rx2)
            sp2 = opposite_side(tg2, width - start_pos2[0])
            end_pos2 = (width, start_pos2[1]+sp2)

        sspos = (width, height+300)

    elif side == 2:
        tg1 = tg(-ry1, rx1)
        sp1 = adjacent_side(tg1, height-start_pos1[1])
        end_pos1 = (start_pos1[0]-sp1, height)

        tg2 = tg(ry2, rx2)
        sp2 = opposite_side(tg2, start_pos2[0])
        end_pos2 = (0, start_pos2[1] - sp2)

        sspos = (-300, height)
    elif side == 3 or side == -3:
        tg1 = tg(rx1, ry1)
        sp1 = opposite_side(tg1, height - start_pos1[1])
        end_pos1 = (start_pos1[0]-sp1, 0)

        if side == -3:
            tg2 = tg(ry2, rx2)
            sp2 = opposite_side(tg2, start_pos2[0])
            end_pos2 = (0, start_pos2[0]-sp2)

            sspos = (0, 0)
        else:
            tg2 = tg(ry2, rx2)
            sp2 = opposite_side(tg2, width-start_pos2[0])
            end_pos2 = (width, start_pos2[1]+sp2)

            sspos = (width, 0)


    elif side == -2:
        tg1 = tg(rx1, ry1)
        sp1 = opposite_side(tg1, start_pos1[1])
        end_pos1 = (start_pos1[0]-sp1, 0)

        tg2 = tg(ry2, rx2)
        sp2 = opposite_side(tg2, width - start_pos2[0])
        end_pos2 = (width, start_pos2[1]+sp2)

        sspos = (width, 0)


    if  side == 0 or side == -1 or side == 1 or side == -4 or side == 3 or side == -2:
        return (start_pos1, end_pos1, sspos, end_pos2, start_pos2)
    else:
        return (start_pos1, end_pos1, sspos, end_pos2,  start_pos2)

def inside_in(point, polygon):
    n = len(polygon)
    inside = False

    x, y = point

    for i in range(n):
        p1x, p1y = polygon[i]
        p2x, p2y = polygon[(i+1) % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    xinters = (y - p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
    return inside



def dialog_text(text, font, text_color, fone_color, x, y, w, h, scr, pg):
    texts = text
    s = len(text)
    p = 15
    fc = (fone_color[0]+p, fone_color[1]+p, fone_color[2]+p)
    pg.draw.rect(scr, fone_color, (x, y, w, h))
    pg.draw.rect(scr, fc, (x+3, y+3, w-6, h-6))
    for q in range(s):
        text = font.render(texts[q], True, text_color)
        scr.blit(text, (x+x/90, 15*q+(y+y/1.3)))

def next_to(player_x, player_y, obj_x, obj_y, min_distance):
    minpx, maxpx = (min(player_x, obj_x), max(player_x, obj_x))
    minpy, maxpy = (min(player_y, obj_y), max(player_y, obj_y))
    if maxpx - minpx <= min_distance:
        if maxpy - minpy <= min_distance:
            return True
        else:
            return False
    else:
        return False


def pluspos(poss, plus):
    wpos = []
    for s in range(len(poss)):
        rt = poss[s]
        ss = []
        for g in range(len(poss[s])):
            if s == 0:
                ss.append(rt[g] - plus)
            elif s == 1:
                if g == 0:
                    ss.append(rt[g] - plus)
                else:
                    ss.append(rt[g] + plus)
            elif s == 2:
                ss.append(rt[g] + plus)
            elif s == 3:
                if g == 0:
                    ss.append(rt[g] + plus)
                else:
                    ss.append(rt[g] - plus)
        wpos.append(ss)

    return wpos

def darkened_screen(width, height, pg, scr, timew):
    alfs = pg.Surface((width, height), pg.SRCALPHA)
    for alf in range(0, 150):
        alfs.fill((0, 0, 0, alf))
        scr.blit(alfs, (0, 0))
        pg.display.flip()
        time.sleep(timew)
def n_obj(player_x, player_y, player_size, speed, obj_pos):
    s1 = obj_pos[0]
    s2 = obj_pos[2]
    wx1, wy1 = s1
    wx2, wy2 = s2
    qx, qy = player_size

    if player_y - speed < wy2 and player_x + qx > wx1 and player_x < wx2 and player_y >= wy1:
        return 'u'
    if player_y + qy + speed > wy1 and player_x + qx > wx1 and player_x < wx2 and player_y < wy2:
        return 'd'
    if player_x - speed < wx2 and player_y + qy > wy1 and player_y < wy2 and player_x > wx1:
        return 'l'
    if player_x + qx + speed > wx1 and player_y + qy > wy1 and player_y < wy2 and player_x < wx2:
        return 'r'


class Button:
    def __init__(self, x, y, default_image, hover_image, click_image, action=None):
        self.default_image = default_image
        self.hover_image = hover_image
        self.click_image = click_image
        self.image = default_image
        self.rect = self.default_image.get_rect(topleft=(x, y))  # Встановлення положення кнопки
        self.action = action
        self.is_hovered = False
        self.is_clicked = False

    def update(self, events):
        mouse_pos = pg.mouse.get_pos()
        mouse_clicked = pg.mouse.get_pressed()[0]

        self.is_hovered = self.rect.collidepoint(mouse_pos)

        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN and self.is_hovered:
                self.is_clicked = True
            elif event.type == pg.MOUSEBUTTONUP and self.is_clicked:
                self.is_clicked = False
                if self.is_hovered and self.action is not None:
                    self.action()

    def draw(self, surface):
        if self.is_clicked:
            surface.blit(self.click_image, self.rect)
        elif self.is_hovered:
            surface.blit(self.hover_image, self.rect)
        else:
            surface.blit(self.default_image, self.rect)