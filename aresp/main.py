import time
import math
from hw import init_i2c, init_mpu, init_vibrator, init_pots
from actions import vibrar, send_charPs
from pots import add_pot_samples, calc_calibrate
from gyro import append_gyro, average_and_slide

i2c = init_i2c()
mpuSensor = init_mpu(i2c)
pino_vibracao = init_vibrator()
pot_list = init_pots()
pot1, pot2, pot3, pot4, pot5 = pot_list

print()
print('*********************************')

def startlim(arrlim,vals):
    for i in range(len(arrlim)):
        arrlim[i] = [vals[i]] * 3
    return arrlim

def startlimpot(arrlim,vals):
    for i in range(len(arrlim)):
        arrlim[i] = vals
    return arrlim

def start(tsleep, tclear, samples, i2c=None, mpu=None, pots=None, vib=None):
    # inicializa hardware se não passado
    if i2c is None: i2c = init_i2c()
    if mpu is None: mpu = init_mpu(i2c)
    if vib is None: vib = init_vibrator()
    if pots is None: pots = init_pots()

    # --- calibracao de pots (40 amostras)
    bufferPot = [[] for _ in pots]
    for _ in range(40):
        pval = [pot.read() for pot in pots]
        print("pot sample:", pval)
        add_pot_samples(bufferPot, pval)
        time.sleep_ms(70)
    maxCalibratePots = calc_calibrate(bufferPot)
    print("maxCalibratePots:", maxCalibratePots)

    # --- prepara buffer do gyro
    buffer = [[] for _ in range(6)]
    for _ in range(samples-1):
        append_gyro(buffer, mpu)
        time.sleep_ms(70)
    gyro, accl = average_and_slide(buffer, mpu)

    num = 0
    holdclick = False
    limpot = [[],[],[],[]]
    triggerPot = [False] * 5
    threshPot = [-120] * 5
    #clickTrigger = threshPot - (threshPot*percentpot)
    #percentpot = 0.1

    # calibrar calibrar
    poragora = 14000

    stepY = 0
    evntTriggeredYP = False
    evntTriggeredYN = False
    thresPercentY = 0.1
    limthresholdYP = poragora 
    limthresholdYN = -poragora
    #limthresholdYP = 14000
    #limthresholdN = -14000
    threshP = limthresholdYP - (limthresholdYP * thresPercentY)
    threshN = limthresholdYN - (limthresholdYN * thresPercentY)

    stepX = 0
    evntTriggeredXP = False
    evntTriggeredXN = False
    thresPercentX = 0.1
    limthresholdXP  = poragora 
    limthresholdXN  = -poragora
    #limthresholdXP = 14000
    #limthresholdXN = -14000
    threshXP = limthresholdXP - (limthresholdXP * thresPercentX)
    threshXN = limthresholdXN - (limthresholdXN * thresPercentX)

    wait2Zero = True
    cycle = 0
    stepWaitXP = 0
    stepWaitXN = 0
    stepWaitYP = 0
    stepWaitYN = 0

    gy1, gy2 = 0, 1 # normal
    #gy1, gy2 = 1, 0 # invertido

    vibrar(vib, 2)
    while True:

        gyro, accl = average_and_slide(buffer, mpu)

        #--------------------------------------------
        if not evntTriggeredXP and not holdclick and gyro[gy1] > threshXP:
            if gy1 == 0: stepX += 1
            if gy1 == 1: stepX -= 1
            vibrar(vib, 1, stepX)
            evntTriggeredXP = True
            wait2Zero = False
            cycle = 0

        elif evntTriggeredXP and gyro[gy1] <= threshXP:
            evntTriggeredXP = False
            wait2Zero = True


        if not evntTriggeredXN and not holdclick and gyro[gy1] < threshXN:
            if gy1 == 0: stepX -= 1
            if gy1 == 1: stepX += 1
            vibrar(vib, 1, stepX)
            evntTriggeredXN = True
            wait2Zero = False
            cycle = 0

        elif evntTriggeredXN and gyro[gy1] >= threshXN:
            evntTriggeredXN = False
            wait2Zero = True

        if evntTriggeredXP: stepWaitXP += 1
        else: stepWaitXP = 0
        if stepWaitXP >= 5:
            if gy1 == 0: stepX += 1
            if gy1 == 1: stepX -= 1
            stepWaitXP = 0
            vibrar(vib, 1, stepX)

        if evntTriggeredXN: stepWaitXN += 1
        else: stepWaitXN = 0
        if stepWaitXN >= 5:
            if gy1 == 0: stepX -= 1
            if gy1 == 1: stepX += 1
            stepWaitXN = 0
            vibrar(vib, 1, stepX)


        #--------------------------------------------
        if not evntTriggeredYP and not holdclick and gyro[gy2] > threshP:
            if gy2 == 0: stepY += 1
            if gy2 == 1: stepY -= 1
            vibrar(vib, 1, stepY)
            evntTriggeredYP = True
            wait2Zero = False
            cycle = 0

        elif evntTriggeredYP and gyro[gy2] <= threshP:
            evntTriggeredYP = False
            wait2Zero = True

        if not evntTriggeredYN and not holdclick and gyro[gy2] < threshN:
            if gy2 == 0: stepY -= 1
            if gy2 == 1: stepY += 1
            vibrar(vib, 1, stepY)
            evntTriggeredYN = True
            wait2Zero = False
            cycle = 0

        elif evntTriggeredYN and gyro[gy2] >= threshN:
            evntTriggeredYN = False
            wait2Zero = True
        #--------------------------------------------
        if evntTriggeredYP: stepWaitYP += 1
        else: stepWaitYP = 0
        if stepWaitYP >= 5:
            if gy1 == 0: stepY -= 1
            if gy1 == 1: stepY += 1
            stepWaitYP = 0
            vibrar(vib, 1, stepY)

        if evntTriggeredYN: stepWaitYN += 1
        else: stepWaitYN = 0
        if stepWaitYN >= 5:
            if gy1 == 0: stepY += 1
            if gy1 == 1: stepY -= 1
            stepWaitYN = 0
            vibrar(vib, 1, stepY)

        #--------------------------------------------
        #maxCalibratePots
        pval = [pot.read() for pot in [pot1, pot2, pot3, pot4, pot5]]

        for i in range(len(pval)):
            pval[i] = pval[i]-maxCalibratePots[i]

        if -1 <= stepX <= 1 and -2 <= stepY <= 2:
            abclevel = [stepX + 1, 2 - stepY]
        else:
            abclevel = None  # ou algum valor padrão


        for i in range(5):
            if not triggerPot[i] and pval[i] < threshPot[i]:

                # >>> evento
                #print(i)
                # print(stepY,stepX,'\t',abclevel,cycle)
                # print(stepY,stepX,'\t',abclevel,i,threshPot[i],pval[i],cycle)

                send_charPs(abclevel,i,1)
                triggerPot[i] = True
                holdclick = True
                wait2Zero = False
                cycle = 0

            elif triggerPot[i] and pval[i] >= threshPot[i]:
                send_charPs(abclevel,i,0)
                triggerPot[i] = False
                holdclick = False
                wait2Zero = True

            #if triggerPot[i]:
            #   print(triggerPot[i])
        
        #--------------------------------------------

        if wait2Zero: cycle += 1
        if cycle == 20:
            stepY = 0
            stepX = 0
            vibrar(vib, 2)

        if num % tclear == 0: num = 0

        num+=1
        time.sleep_ms(tsleep)


#---------------------------------------------------------------

def run():
    vibrar(init_vibrator(), 4)
    TSLEEP = 50
    TCLEAR = 10000
    SAMPLES = 5
    start(TSLEEP, TCLEAR, SAMPLES)











