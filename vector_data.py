import random
import tkinter as tk
from tkinter.messagebox import askyesno
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pydotplus
import graphviz
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class VerticalScrolledFrame:
    def __init__(self, master, **kwargs):
        width = kwargs.pop( 'width', None )
        height = kwargs.pop( 'height', None )
        bg = kwargs.pop( 'bg', kwargs.pop( 'background', None ) )
        self.outer = tk.Frame( master, **kwargs )

        self.vsb = tk.Scrollbar( self.outer, orient=tk.VERTICAL )
        self.hsb = tk.Scrollbar( self.outer, orient=tk.HORIZONTAL)
        self.vsb.pack( fill=tk.X, side=tk.BOTTOM)
        self.vsb.pack( fill=tk.Y, side=tk.RIGHT )
        self.canvas = tk.Canvas( self.outer, highlightthickness=0, width=width, height=height, bg=bg )
        self.canvas.pack( side=tk.LEFT, fill=tk.BOTH, expand=True )
        self.canvas['yscrollcommand'] = self.vsb.set
        self.canvas.bind( "<Enter>", self._mouse_binding )
        self.canvas.bind( "<Leave>", self._mouse_unbinding )
        self.vsb['command'] = self.canvas.yview

        self.inner = tk.Frame( self.canvas, bg=bg )
        self.canvas.create_window( 4, 4, window=self.inner, anchor='nw' )
        self.inner.bind( "<Configure>", self._on_frame_configure )

        self.outer_attr = set( dir( tk.Widget ) )

    def __getattr__(self, item):
        return getattr( self.outer, item ) if item in self.outer_attr else getattr( self.inner, item )

    def _on_frame_configure(self, event=None):
        x1, y1, x2, y2 = self.canvas.bbox( "all" )
        height = self.canvas.winfo_height()
        self.canvas.config( scrollregion=(0, 0, x2, max( y2, height )) )

    def _on_mousewheel(self, event):
        if event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll( -1, "units" )
        elif event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll( 1, "units" )

    def _mouse_binding(self, event=None):
        self.canvas.bind_all( "<4>", self._on_mousewheel )
        self.canvas.bind_all( "<5>", self._on_mousewheel )
        self.canvas.bind_all( "<MouseWheel>", self._on_mousewheel )

    def _mouse_unbinding(self, event=None):
        self.canvas.unbind_all( "<4>" )
        self.canvas.unbind_all( "<5>" )
        self.canvas.unbind_all( "<MouseWheel>" )

    def __str__(self):
        return str( self.outer )


if __name__ == "__main__":
    root = tk.Tk()
    root.title( "Mass Geometry Calculator" )
    root.configure( background="#C5ECF3" )
    root.geometry( '1350x800+150+0' )
    VerticalScrolledFrame( root, width=1000, height=700, borderwidth=2,
                           relief=tk.SUNKEN, background="#c4a990" ).grid()
    root.grid_columnconfigure( 0, weight=1 )
    root.grid_rowconfigure( 1, weight=1 )
    root.mainloop()