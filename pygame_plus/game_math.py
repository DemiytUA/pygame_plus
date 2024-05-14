def tg(opposite_side, adjacent_side):#протилежна та прилегла сторони відповідно
    tg_angle = opposite_side/adjacent_side
    return tg_angle
def opposite_side(tg, adjacent_side):
    op_side = tg*adjacent_side
    return op_side
def adjacent_side(tg, opposite_side):
    ad_side = opposite_side/tg
    return ad_side
def gip(a, b):
    gip_l = (a**2 + b**2)**0.5
    return gip_l