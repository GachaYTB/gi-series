import gislib
app = gislib.GiS('Test App', (23, 35, 233), (255, 255, 255), 'Test GiS Libary', (32, 122, 79))
app.print('Hello World!', 10, 10, (255, 255, 255))
app.print('Hello World But Colorful!', 10, 35, (42, 122, 0))
app.export('./testapp.gisapp')