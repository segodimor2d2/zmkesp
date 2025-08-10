from utils import vibrar, getGyro
from sensors import start

def run():
    vibrar(4)
    TSLEEP = 50
    TCLEAR = 10000
    SAMPLES = 5
    start(TSLEEP, TCLEAR, SAMPLES, getGyro)

if __name__ == "__main__":
    run()
