from global_val import GlobalVal,const

def coordinate_map(x, y):
    if x >= const.MIN_HEIGHT_LOCAL and x < const.MAX_HEIGHT_LOCAL and y >= const.MIN_WIDTH_LOCAL and y < const.MAX_WIDTH_LOCAL:
        if y % 2 == 0:
            point = (7 - x) + 8 * (16 - y)
        else:
            point = x + 8 * (16 - y)
    else:
        point = -1
    return point
