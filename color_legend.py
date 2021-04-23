# @authors  Timothy Goetsch
# 4/21/2021
# @brief    ColorLegend object:  creates legends for the following modes: VIS, NIR, TEMP, SVA, NDVI, EVI, SAVI, MSAVI
# last updated: 4/22/2021 by Timothy Goetsch
# @updates  SVA mode now produces a sample legend. We might actually be able use it for generic VIR-ATLAS stuff? idk.
# TODO:

import tkinter as tk
from tkinter import Canvas, Frame, BOTH, W
import color as col
from math import floor

TEST_LIST = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']


class ColorLegend(Frame):
    def __init__(self, mode="vis"):
        super().__init__()

        self.master.title("ColorBar")
        self.pack(fill=BOTH, expand=1)

        # set display mode
        self.mode = mode

        # set display size
        self.width = 110
        self.height = 840

        # create canvas
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)

        # set scale
        self.scale = set_scale(self.mode)

        # collect color and scale lists
        color, scale = get_colors(self.mode, self.scale)

        # specify how much space to leave above/below legend and canvas top/bottom
        start = 10
        stop = self.height - start
        step = 1

        # create colored rectangles
        x_start = 10  # goes with window atm, may move to a method if both vertical and horizontal legends are produced
        x_end = 60  # same as x_start
        y = 10  # arbitrary y start value
        # create rectangles, depends on x starting and ending values, y start value, and box_size, generalized for any mode
        if color:
            # determine size of bounding box for each color depending on number of elements in the color List
            box_size = floor((stop - start) / len(color))
            legend_size = box_size * len(color) + start

            # create vertical bar for tick marks, generalized for any mode
            x = 70
            self.canvas.create_line(x, start, x, legend_size)

            for num, c in enumerate(color):
                self.canvas.create_rectangle(x_start, y, x_end, y+box_size, outline=c, fill=c)
                self.canvas.create_line(70, y, 75, y)
                if y == 0:
                    self.canvas.create_text(80, y, anchor=W, font=("Arial", 8), text=scale[num])
                else:
                    self.canvas.create_text(80, y + (box_size/2), anchor=W, font=("Arial", 8), text=scale[num])
                y += box_size
                # print(y)

            self.canvas.create_line(70, y, 75, y)

        # pack canvas
        self.canvas.pack(fill=BOTH, expand=1)


def set_scale(mode: str):
    scale = []
    if mode == "temp":
        scale = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0]  # 11 values
    elif mode == "ndvi" or mode == "evi" or mode == "savi" or mode == "msavi":
        scale = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0, -0.1, -0.2, -0.3, -0.4, -0.5, -0.6, -0.7, -0.8, -0.9, -1]  # 21 values
    elif mode == "sva":
        max_temp = 85
        min_temp = -41  # range is exclusive of the max value, so we're adding 1 to the actual max value of the sva scale
        for _ in range(max_temp, min_temp, -5):
            scale.append(float(_))
    return scale


def get_colors(mode: str, scale: list):
    """
    8 maps (only need 3 unique legends)
    VIS (VISUAL LIGHT) (data_to_hex)
    NIR (NEAR INFRARED LIGHT) (data_to_hex)

    TEMP (DISTRIBUTION FROM MIN_TEMP TO MAX_TEMP RECORDED)
    SVA (SURFACE VS AIR TEMP, WHITE IS AIR TEMP, SUBTRACTS AIR TEMP FROM SURFACE TO OBTAIN DELTA)
    VI There are (-1, 1) NEGATIVE NUMBER SYMBOLIZES DEAD
    """
    color = []

    if mode == "vis":
        # visible spectrum, will likely need a different legend type than a plain bar.
        # scale = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]  # 11 values
        # for i in scale:
        #     color.append(col.false_color(i, 0, 1))
        pass
    elif mode == "nir":
        # near infrared spectrum, will likely need a different legend type than a plain bar. (same as vis i think)
        # scale = [-1, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]  # 21 values
        # for i in scale:
        #     color.append(col.false_color_vi(i))
        pass
    elif mode == "temp":
        # temperatures, range(0, 1, 0.1) -> (d_blue, cyan, yellow, orange, red)
        for i in scale:
            color.append(col.false_color(i, 0, 1))
    elif mode == "sva":
        # surface vs air temp, range(?) -> (?)
        temp = [0] * len(scale)  # list containing hex values for corresponding surface temps
        air_temp = scale[0] + scale[-1]  # arbitrary air temperature value, however it needs to be inside the (min, max) range of scale

        for num, s in enumerate(scale):
            temp[num] = set_temp(s, scale[0], scale[-1], air_temp)

        for num, i in enumerate(scale):
            color.append(col.false_two_color(air_temp, scale[0], scale[-1], temp[num], temp[-num]))
        pass
    elif mode == "ndvi" or mode == "evi" or mode == "savi" or mode == "msavi":
        # vegetative indexes, range(-1, 1, 0.1) -> (d_blue, white, tan, green, d_green)
        for i in scale:
            color.append(col.false_color_vi(i))

    return color, scale


def set_temp(surface_temp, min_temp, max_temp, air_temp):
    """
    @todo: this likely needs to be placed in color.py and removed from here and stella_frame.py
    """
    # max_temp = 85.0
    # min_temp = -40.0 #max and min the sensor can see
    temp_rgb = col.false_color(surface_temp, min_temp, max_temp)

    temp_delta = surface_temp - air_temp
    min_delta = min_temp - air_temp
    max_delta = max_temp - air_temp
    red = '#ff0000'
    blue = '#0000ff'

    sva_rgb = col.false_two_color(temp_delta, min_delta, max_delta, blue, red)
    return sva_rgb

# def create_legend(mode: str, temp_max: str, temp_min: str)


def main():
    root = tk.Tk()
    cb = ColorLegend("sva")
    # WIDTH X HEIGHT + Location on screen when opening (WIDTH + HEIGHT)
    # root.geometry("100x600+1000+500")
    root.mainloop()


if __name__ == '__main__':
    main()