import pandas as pd
import plotly.graph_objects as go
from . import _error_handling as eh

class scatter:
    # ------------------------------------------------------------------------------------------
    # ------------------------------------ Constructor -----------------------------------------
    # ------------------------------------------------------------------------------------------
    def __init__(self, data, title='', xlabel='x', ylabel='y', dropdown=False, legend=True, mode='lines') -> None:
        '''
        Constructor:
        data - ndarray (structured or homogeneous), Iterable, dict, or DataFrame
        title - string
        xlabel - string
        ylabel - string
        dropdown - boolean
        mode - string -> choose from 'lines', 'markers', 'lines+markers'
        '''
        self.data = pd.DataFrame(data) # Set data variable

        eh.check_str(title, 'title') # If title is not string -> raise ValueError
        self.title = title # Else set title variable

        eh.check_str(xlabel, 'xlabel') # If xlabel is not string -> raise ValueError
        self.xlabel = xlabel # Else set xlabel variable

        eh.check_str(ylabel, 'ylabel') # If ylabel is not string -> raise ValueError
        self.ylabel = ylabel # Else set ylabel variable
        
        eh.check_bool(dropdown, 'dropdown') # If dropdown is not boolean -> raise ValueError
        self.dropdown = dropdown # Else set dropdown variable

        eh.check_bool(legend, 'legend') # If legend is not boolean -> raise ValueError
        self.legend = legend # Else set legend variable

        eh.check_mode(mode) # If mode is not "lines", "markers" or "lines+markers" -> raise ValueError
        self.mode = mode # Else set mode variable

    # ------------------------------------------------------------------------------------------
    # ----------------------------------- Setter -----------------------------------------------
    # ------------------------------------------------------------------------------------------
    def set_data(self, data) -> None:
        '''Takes data as input. Sets self.data to data, if data is pandas.DataFrame readable. 
        Please check https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html for 
        further information!'''
        self.data = pd.DataFrame(data)

    def set_title(self, title) -> None:
        '''Takes title as input. Sets self.title to title, if title has type string'''
        eh.check_str(title, 'title')
        self.title = title

    def set_xlabel(self, label) -> None:
        '''Takes label as input. Sets self.xlabel to label, if label has type string'''
        eh.check_str(label, 'xlabel')
        self.xlabel = label

    def set_ylabel(self, label) -> None:
        '''Takes label as input. Sets self.ylabel to label, if label has type string'''
        eh.check_str(label, 'ylabel')
        self.ylabel = label

    def set_dropdown(self, boolean) -> None:
        '''Takes boolean as input. Sets self.dropdown to boolean, if boolean has type boolean'''
        eh.check_bool(boolean, 'dropdown')
        self.dropdown = boolean

    def set_legend(self, boolean) -> None:
        '''Takes boolean as input. Sets self.legend to boolean, if boolean has type boolean'''
        eh.check_bool(boolean, 'legend')
        self.legend = boolean
        
    def set_mode(self, mode) -> None:
        '''Takes mode as input. Sets self.mode to mode, if mode is either "lines", "markers" 
        or "lines+markers"'''
        eh.check_mode(mode)
        self.mode = mode

    # ------------------------------------------------------------------------------------------
    # --------------------------------- Init Figure --------------------------------------------
    # ------------------------------------------------------------------------------------------
    def __figure(self) -> go.Figure:
        '''Creates a figure with default layout and returns it'''
        fig = go.Figure()

        for col in self.data.columns:
            fig.add_trace(
                go.Scatter(
                    x = self.data.index,
                    y = self.data[col],
                    name=col,
                    mode=self.mode
                )
            )

        return fig

    # ------------------------------------------------------------------------------------------
    # ------------------------------------ Layout ----------------------------------------------
    # ------------------------------------------------------------------------------------------
    def __add_layout(self, fig) -> None:
        '''Adds layout config to figure'''
        fig.update_layout(
            title=self.title,
            xaxis_title=self.xlabel,
            yaxis_title=self.ylabel,
            showlegend=self.legend
        )

        if self.dropdown:
            self.__add_dropdown(fig)

    def __add_dropdown(self, fig) -> None:
        '''If dropdown is set to True -> adds dropdown menu to figure'''

        # Create a list of all dropdown buttons. Every column in DataFrame will have its 
        # own button in dropdown 
        buttons = list() 

        # Append all button
        buttons.append(
            dict(
                label='All', 
                method='update', 
                args=[{
                    'visible': [True] * len(self.data.columns), 
                    'Title': 'All',
                    'showlegend': False
                }]
            )
        )

        # Append button for every column in DataFrame
        for idx, col in enumerate(self.data.columns):
            visible = [False] * len(self.data.columns)
            visible[idx] = True
            buttons.append(
                dict(
                    label=col, 
                    method='update', 
                    args=[{
                        'visible': visible, 
                        'Title': col,
                        'showlegend': False
                    }]
                )
            )

        # Add dropdown items to figure
        fig.update_layout(
            updatemenus=[
                go.layout.Updatemenu(
                    active=0,
                    buttons=buttons
                )
            ]
        )

    # ------------------------------------------------------------------------------------------
    # -------------------------------------- Show ----------------------------------------------
    # ------------------------------------------------------------------------------------------
    def show(self) -> None:
        '''Creates a figure with the selected config'''
        fig = self.__figure() # intializes figure
        self.__add_layout(fig) # adds layout config
        fig.show() # shows figure