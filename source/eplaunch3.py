#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.0a8 on Thu Jan 18 10:24:54 2018
#

import wx
import images

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class mainApplicationFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: mainApplicationFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.window_1 = wx.SplitterWindow(self, wx.ID_ANY)
        self.window_1_pane_1 = wx.Panel(self.window_1, wx.ID_ANY)
        self.dir_ctrl_1 = wx.GenericDirCtrl(self.window_1_pane_1, -1, size=(200,225), style=wx.DIRCTRL_DIR_ONLY)

        self.window_1_pane_2 = wx.Panel(self.window_1, wx.ID_ANY)
        self.list_ctrl_files = wx.ListCtrl(self.window_1_pane_2, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)


        self.statusbar = self.CreateStatusBar(1)
        self.statusbar.SetStatusText('Status bar - reports on simulations in progress')



#        tb = self.CreateToolBar( wx.TB_HORIZONTAL | wx.NO_BORDER | wx.TB_FLAT | wx.TB_TEXT )
        self.tb = wx.ToolBar( self, style=wx.TB_HORIZONTAL | wx.NO_BORDER | wx.TB_FLAT | wx.TB_TEXT )

        tsize = (24,24)
        new_bmp =  wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR, tsize)
        open_bmp = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, tsize)
        copy_bmp = wx.ArtProvider.GetBitmap(wx.ART_COPY, wx.ART_TOOLBAR, tsize)
        paste_bmp= wx.ArtProvider.GetBitmap(wx.ART_PASTE, wx.ART_TOOLBAR, tsize)
        forward_bmp = wx.ArtProvider.GetBitmap(wx.ART_GO_FORWARD, wx.ART_TOOLBAR, tsize)
        error_bmp = wx.ArtProvider.GetBitmap(wx.ART_ERROR, wx.ART_TOOLBAR, tsize)

        file_open_bmp = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, tsize)
        exe_bmp = wx.ArtProvider.GetBitmap(wx.ART_EXECUTABLE_FILE, wx.ART_TOOLBAR, tsize)
        up_bmp = wx.ArtProvider.GetBitmap(wx.ART_GO_UP, wx.ART_TOOLBAR, tsize)
        folder_bmp = wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_TOOLBAR, tsize)
        page_bmp = wx.ArtProvider.GetBitmap(wx.ART_HELP_PAGE, wx.ART_TOOLBAR, tsize)
        help_bmp = wx.ArtProvider.GetBitmap(wx.ART_HELP, wx.ART_TOOLBAR, tsize)

        self.tb.SetToolBitmapSize(tsize)

        chID = wx.NewId()
        workflow_choice = wx.Choice(self.tb,chID,choices=["EnergyPlus SI (*.IDF)", "EnergyPlus IP (*.IDF)", "AppGPostProcess (*.HTML)", "CalcSoilSurfTemp", "CoeffCheck", "CoeffConv", "Basement", "Slab", "File Operations"])
        workflow_choice.SetSelection(0)
        self.tb.AddControl(workflow_choice)

        self.tb.AddTool(10, "Weather", file_open_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Weather", "Long help for 'Weather'", None)
        self.tb.AddTool(20, "Run", forward_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Run", "Long help for 'Run'", None)
        self.tb.AddTool(30, "Cancel", error_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Cancel", "Long help for 'Cancel'", None)
        self.tb.AddSeparator()
        self.tb.AddTool(40, "IDF Editor", exe_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "IDF Editor", "Long help for 'IDF Editor'", None)
        self.tb.AddTool(50, "Text Editor", exe_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Text Editor", "Long help for 'Text Editor'", None)
        self.tb.AddSeparator()
        self.tb.AddTool(80, "Explorer", folder_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Explorer", "Long help for 'Explorer'", None)
        self.tb.AddTool(80, "Update", up_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Update", "Long help for 'Update'", None)
        self.tb.AddTool(80, "Settings", page_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Settings", "Long help for 'Settings'", None)
        self.tb.AddTool(90, "Help", help_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Help", "Long help for 'Help'", None)

        self.tb.Realize()


        #outtb = self.CreateToolBar( wx.TB_BOTTOM | wx.NO_BORDER | wx.TB_FLAT | wx.TB_TEXT )
        self.outtb = wx.ToolBar( self, style=wx.TB_HORIZONTAL | wx.NO_BORDER | wx.TB_FLAT | wx.TB_TEXT )
        outtbsize = (16,16)
        self.outtb.SetToolBitmapSize(outtbsize)

        norm_bmp = wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_TOOLBAR, tsize)


        self.outtb.AddTool(10, "Tables", norm_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Help", "Long help for 'Help'", None)
        self.outtb.AddTool(10, "Meters", norm_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Help", "Long help for 'Help'", None)
        self.outtb.AddTool(10, "Variables", norm_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Help", "Long help for 'Help'", None)
        self.outtb.AddTool(10, "Errors", norm_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Help", "Long help for 'Help'", None)
        self.outtb.AddTool(10, "RDD", norm_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Help", "Long help for 'Help'", None)
        self.outtb.AddTool(10, "MDD", norm_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Help", "Long help for 'Help'", None)
        self.outtb.AddSeparator()
        self.outtb.AddTool(10, "EIO", norm_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Help", "Long help for 'Help'", None)
        self.outtb.AddTool(10, "SVG", norm_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Help", "Long help for 'Help'", None)
        self.outtb.AddTool(10, "DXF", norm_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Help", "Long help for 'Help'", None)
        self.outtb.AddTool(10, "MTD", norm_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Help", "Long help for 'Help'", None)
        self.outtb.AddTool(10, "ZSZ", norm_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Help", "Long help for 'Help'", None)
        self.outtb.AddTool(10, "SSZ", norm_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Help", "Long help for 'Help'", None)
        self.outtb.Realize()



        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileMenu.Append(10,"Run File", "Run currently selected file for selected workflow")
        fileMenu.Append(11,"Cancel Selected", "Cancel selected files")
        fileMenu.Append(13,"Cancel All", "Cancel all queued files")
        fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')

        editMenu = wx.Menu()
        editMenu.Append(20,"Undo")
        editMenu.AppendSeparator()
        editMenu.Append(21,"Cut")
        editMenu.Append(22,"Copy")
        editMenu.Append(23,"Paste")
        menubar.Append(editMenu, "&Edit")

        folderMenu = wx.Menu()
        folderMenu.Append(31, "Recent")
        folderMenu.AppendSeparator()
        folderMenu.Append(32, "c:\\EnergyPlus8-8-0")
        folderMenu.Append(33, "c:\\documents")
        folderMenu.Append(34, "c:\\projectX\\working\\task1")
        folderMenu.Append(35, "c:\\projectY\\dev\\task2")
        folderMenu.AppendSeparator()
        folderMenu.Append(36, "Favorites")
        folderMenu.AppendSeparator()
        folderMenu.Append(37, "c:\\EnergyPlus8-8-0\Examples")
        folderMenu.Append(38, "c:\\documents\\about")
        folderMenu.Append(39, "c:\\projectZ\\do")
        folderMenu.AppendSeparator()
        folderMenu.Append(310, "Add Current Folder to Favorites")
        folderMenu.Append(311, "Remove Current Folder from Favorites")
        menubar.Append(folderMenu, "F&older")

        weatherMenu = wx.Menu()
        weatherMenu.Append(41, "Select..")
        weatherMenu.AppendSeparator()
        weatherMenu.Append(42, "Recent")
        weatherMenu.AppendSeparator()
        weatherMenu.Append(43, "Chicago.TMY")
        weatherMenu.Append(44, "Boston.TMY")
        weatherMenu.Append(45, "Philadelphia.TMY")
        weatherMenu.Append(46, "Austin.TMY")
        weatherMenu.AppendSeparator()
        weatherMenu.Append(47, "Favorites")
        weatherMenu.AppendSeparator()
        weatherMenu.Append(48, "Detroit.TMY")
        weatherMenu.Append(49, "Denver.TMY")
        weatherMenu.Append(410, "San Francisco.TMY")
        weatherMenu.AppendSeparator()
        weatherMenu.Append(411, "Add Weather to Favorites")
        weatherMenu.Append(412, "Remove Weather from Favorites")
        menubar.Append(weatherMenu, "&Weather")

        outputMenu = wx.Menu()
        outputMenu.Append(501, "Table.csv")
        outputMenu.Append(502, "Table.tab")
        outputMenu.Append(503, "Table.txt")
        outputMenu.Append(504, "Table.html")
        outputMenu.Append(505, "Table.xml")
        outputMenu.Append(506, ".csv")
        outputMenu.Append(507, ".tab")
        outputMenu.Append(508, ".txt")
        outputMenu.Append(509, "Meter.csv")
        outputMenu.Append(510, "Meter.tab")
        outputMenu.Append(511, "Meter.txt")
        outputMenu.Append(512, "Variables")
        outputMenu.Append(513, ".err")
        outputMenu.Append(514, ".end")
        outputMenu.Append(515, ".rdd")
        outputMenu.Append(516, ".mdd")
        outputMenu.Append(517, ".eio")
        outputMenu.Append(518, ".svg")
        outputMenu.Append(519, ".dxf")
        outputMenu.Append(520, ".mtd")
        outputMenu.Append(521, "Zsz.csv")
        outputMenu.Append(522, "Zsz.tab")
        outputMenu.Append(523, "Zsz.txt")
        outputMenu.Append(524, "Ssz.csv")
        outputMenu.Append(525, "Ssz.tab")
        outputMenu.Append(526, "Ssz.txt")
        outputMenu.Append(527, "DElight.in")
        outputMenu.Append(528, "DElight.out")
        outputMenu.Append(529, "DElight.eldmp")
        outputMenu.Append(530, "DElight.dfdmp")
        outputMenu.Append(531, "Map.csv")
        outputMenu.Append(532, "Map.tab")
        outputMenu.Append(533, "Map.txt")
        outputMenu.Append(534, "Screen.csv")
        outputMenu.Append(535, ".expidf")
        outputMenu.Append(536, ".epmidf")
        outputMenu.Append(537, ".epmdet")
        outputMenu.Append(538, ".shd")
        outputMenu.Append(539, ".wrl")
        outputMenu.Append(540, ".audit")
        outputMenu.Append(541, ".bnd")
        outputMenu.Append(542, ".dbg")
        outputMenu.Append(543, ".sln")
        outputMenu.Append(544, ".edd")
        outputMenu.Append(545, ".eso")
        outputMenu.Append(546, ".mtr")
        outputMenu.Append(547, "Proc.csv")
        outputMenu.Append(548, ".sci")
        outputMenu.Append(549, ".rvaudit")
        outputMenu.Append(550, ".sql")
        outputMenu.Append(551, ".log")
        outputMenu.Append(552, ".bsmt")
        outputMenu.Append(553, "_bsmt.out")
        outputMenu.Append(554, "_bsmt.audit")
        outputMenu.Append(555, "_bsmt.csv")
        outputMenu.Append(556, ".slab")
        outputMenu.Append(557, "_slab.out")
        outputMenu.Append(558, "_slab.ger")
        menubar.Append(outputMenu, "&Output")

        helpMenu = wx.Menu()
        helpMenu.Append(61, "EnergyPlus Getting Started")
        helpMenu.Append(62, "EnergyPlus Input Output Reference")
        helpMenu.Append(63, "EnergyPlus Output Details and Examples")
        helpMenu.Append(64, "EnergyPlus Engineering Reference")
        helpMenu.Append(65, "EnergyPlus Auxiliar Programs")
        helpMenu.Append(66, "Application Guide for Plant Loops")
        helpMenu.Append(67, "Application Guide for EMS")
        helpMenu.Append(68, "Using EnergyPlus for Compliance")
        helpMenu.Append(69, "External Interface Application Guide")
        helpMenu.Append(610, "Tips and Tricks Using EnergyPlus")
        helpMenu.Append(611, "EnergyPlus Acknowledgments")
        helpMenu.AppendSeparator()
        helpMenu.Append(612, "Check for Updates..")
        helpMenu.Append(613, "View Entire Update List on Web..")
        helpMenu.AppendSeparator()
        helpMenu.Append(614, "Using EP-Launch Help")
        helpMenu.Append(615, "About EP-Launch")
        menubar.Append(helpMenu, "&Help")


        self.SetMenuBar(menubar)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: mainApplicationFrame.__set_properties
        self.SetTitle(_("EP-Launch 3"))
        self.list_ctrl_files.AppendColumn(_("Status"), format=wx.LIST_FORMAT_LEFT, width=-1)
        self.list_ctrl_files.AppendColumn(_("File Name"), format=wx.LIST_FORMAT_LEFT, width=-1)
        self.list_ctrl_files.AppendColumn(_("Weather File"), format=wx.LIST_FORMAT_LEFT, width=-1)
        self.list_ctrl_files.AppendColumn(_("Size"), format=wx.LIST_FORMAT_LEFT, width=-1)
        self.list_ctrl_files.AppendColumn(_("Errors"), format=wx.LIST_FORMAT_LEFT, width=-1)
        self.list_ctrl_files.AppendColumn(_("EUI"), format=wx.LIST_FORMAT_LEFT, width=-1)
        self.list_ctrl_files.AppendColumn(_("Floor Area"), format=wx.LIST_FORMAT_LEFT, width=-1)


        rows = [["Running","5Zone.idf", "Chicago.TMY", "8172","-","-","-"],
            ["Complete","6Zone.idf", "Chicago.TMY", "9847","0","1.58","765"],
            ["Old","7Zone.idf", "Chicago.TMY", "8172","-","-","-"],
            ["Queued","8Zone.idf", "Chicago.TMY", "8172","-","-","-"]]

        index = 0
        for row in rows:
            self.list_ctrl_files.InsertItem(index,row[0])
            self.list_ctrl_files.SetItem(index, 1, row[1])
            self.list_ctrl_files.SetItem(index, 2, row[2])
            self.list_ctrl_files.SetItem(index, 3, row[3])
            self.list_ctrl_files.SetItem(index, 4, row[4])
            self.list_ctrl_files.SetItem(index, 5, row[5])
            self.list_ctrl_files.SetItem(index, 6, row[6])
            index = index + 1


        self.window_1.SetMinimumPaneSize(20)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: mainApplicationFrame.__do_layout
        sizerMainAppVert = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_5.Add(self.dir_ctrl_1, 1, wx.EXPAND, 0)
        self.window_1_pane_1.SetSizer(sizer_5)
        sizer_3.Add(self.list_ctrl_files, 1, wx.EXPAND, 0)
        self.window_1_pane_2.SetSizer(sizer_3)
        self.window_1.SplitVertically(self.window_1_pane_1, self.window_1_pane_2)
        sizerMainAppVert.Add(self.tb, 0, wx.EXPAND, 0)
        sizerMainAppVert.Add(self.outtb, 0, wx.EXPAND, 0)
        sizerMainAppVert.Add(self.window_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizerMainAppVert)
        sizerMainAppVert.Fit(self)
        self.Layout()
        # end wxGlade

# end of class mainApplicationFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame_eplaunch = mainApplicationFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame_eplaunch)
        self.frame_eplaunch.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = MyApp(0)
    app.MainLoop()