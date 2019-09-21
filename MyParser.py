from functools import partial
from TIGr import AbstractParser


class MyParser(AbstractParser):
    def __init__(self, drawer):
        self.drawer = drawer
        self.source = []
        self.command = ''
        self.data = 0
        
        self.no_parameter_commands = {
            'D': self.drawer.pen_down,
            'U': self.drawer.pen_up
        }
        self.one_parameter_commands = {
            'P': self.drawer.select_pen,
            'X': self.drawer.go_along,
            'Y': self.drawer.go_down,
            'C': self.drawer.draw_circle,
            'R': self.drawer.draw_rectangle,
            'T': self.drawer.draw_triangle
        }
        self.draw_line_commands = {
            'N': partial(self.drawer.draw_line, 90 * 0),
            'E': partial(self.drawer.draw_line, 90 * 1),
            'S': partial(self.drawer.draw_line, 90 * 2),
            'W': partial(self.drawer.draw_line, 90 * 3)
        }

    def parse(self, raw_source):
        self.source = raw_source

        for line in self.source:
            tempArr = line.split(" ")
            self.command = line[0]
            try:
                self.data = int(tempArr[1])
            except:
                self.data = 0
            self.call_drawer()
        try:
            self.drawer.end()
        except:
            pass
        
    def call_drawer(self):
        if self.command in self.no_parameter_commands:
            self.no_parameter_commands[self.command]()
        elif self.command in self.one_parameter_commands:
            self.one_parameter_commands[self.command](self.data)
        elif self.command in self.draw_line_commands:
            self.draw_line_commands[self.command](self.data)
        else:
            print('Command {} is invalid'.format(self.command))
