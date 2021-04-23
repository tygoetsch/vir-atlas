# @authors Brynn
# @date 4/22/21
# @brief The most recent main GUI file.
# @TODO Add the legend, annotations, and satellite frames to the main window

import tkinter as tk
import menu_bar as menu
import stella_frame
import map_gen
import color_legend


# Class creating the base window
class Root(tk.Tk):
    # Main window constructor
    def __init__(self):
        tk.Tk.__init__(self)

        self.geometry('1450x900')
        self.winfo_toplevel().title("VIR-Atlas")

        # Initialize data files
        self.stella_file = 0
        self.gps_file = 0
        self.map_file = 0

        self.map_data = map_gen.Map()

        # Add the stella_frame to the main window
        self.stella_frame = stella_frame.StellaFrame(self)
        self.stella_frame.set_canvas()
        self.stella_frame.place(x=20, y=20)

        # Add the legend frame to the main window
        self.color_legend_frame = color_legend.ColorLegend(self)
        self.color_legend_frame.place(x=880, y=20)

        # Add the annotation frame to the main window
        self.annotation_frame = None

        # Add the menu_bar to the main window
        menu_bar = menu.MenuBar(self)
        self.config(menu=menu_bar)

    def set_stella_data(self, file):
        self.stella_file = file

    def set_gps_data(self, file):
        self.gps_file = file

    def set_map_data(self, file):
        self.map_file = file

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.stella_frame is not None:
            self.stella_frame.destroy()
        self.stella_frame = new_frame
        self.stella_frame.place(x=20, y=20)


if __name__ == "__main__":
    root = Root()
    root.mainloop()
