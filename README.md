# Pygame-Clicker-Game
a simple clicker game made with the module pygame from python, 288 lines, score saving is missing.
if you have some problems loading the sprites try changing the directory code to your workspace.
if you have this error or something like this : FileNotFoundError: No file found in working directory

try changing :
normalBeanImage=pygame.image.load(os.path.join("assets","cofbean.png"))
to:
normalBeanImage=pygame.image.load("youWorkspace\\clickerGame\\assets\\cofbean.png")
and do it for all the sprites and mp3 files.
