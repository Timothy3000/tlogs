import sys #IPORTANT
__version__='1-1-1'
#1-0-0+
def seti(p):
    sys.stdout.write("Setting "+str(p)+"...\n")
def st2(p):
    sys.stdout.write("Starting "+str(p)+"...\n")
def z(p1,p2):
    sys.stdout.write(str(p1)+" v"+str(p2)+" started\n")
def log(p):
    sys.stdout.write(str(p)+"\n")
def getv():
    return __version__
def er(e):
    sys.stderr.write("E: "+str(e)+"\n")
def warn(w):
    sys.stdout.write("W: "+str(w)+"\n")
def debug(m):
    sys.stdout.write("DEBUG: "+str(m)+"\n")
def d(fi):
    sys.stdout.write("file "+str(fi)+" deleted\n")
#1-1-1+
def info(p):
    log("INFO: "+str(p))