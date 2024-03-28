import gislib
gisapp = gislib.GiS("test", (0, 127, 255), (255, 255, 255), "test!!!", (255, 0, 0))
gisapp.print("hehehe", 0, 0, (255, 255, 255))
gisapp.export("./exportedGisApp.gisapp")