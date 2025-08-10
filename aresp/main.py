import time
import math
from hw import init_i2c, init_mpu, init_vibrator, init_pots
from actions import vibrar, send_charPs

i2c = init_i2c()
mpuSensor = init_mpu(i2c)
pino_vibracao = init_vibrator()
pot_list = init_pots()
pot1, pot2, pot3, pot4, pot5 = pot_list

print()
print('*********************************')

def calclim(lim,val):
    lst = (lim[0],lim[1],val)
    lim[0] = max(lst)
    lim[1] = min(lst)
    lim[2] = val
    return lim 

def getPots(bufferPot,pval):
    bufferPot[0].append(pval[0])
    bufferPot[1].append(pval[1])
    bufferPot[2].append(pval[2])
    bufferPot[3].append(pval[3])
    bufferPot[4].append(pval[4])
    return bufferPot

def calcCalibrate(bufferPot):
    maxCalc = [] 
    for potList in bufferPot:
        maxCalc.append(max(potList))
    return maxCalc


def getGyro(buffer):
    mpuData = mpuSensor.get_values()
    buffer[0].append(mpuData['GyX'])
    buffer[1].append(mpuData['GyY'])
    buffer[2].append(mpuData['GyZ'])
    buffer[3].append(mpuData['AcX'])
    buffer[4].append(mpuData['AcY'])
    buffer[5].append(mpuData['AcZ'])
    return buffer

def media(buffer):
    getGyro(buffer)
    xgyro = sum(buffer[0])/len(buffer[0])
    ygyro = sum(buffer[1])/len(buffer[1])
    zgyro = sum(buffer[2])/len(buffer[2])
    xaccl = sum(buffer[3])/len(buffer[3])
    yaccl = sum(buffer[4])/len(buffer[4])
    zaccl = sum(buffer[5])/len(buffer[5])
    gyro = [xgyro,ygyro,zgyro]
    accl = [xaccl,yaccl,zaccl]
    buffer[0].pop(0)
    buffer[1].pop(0)
    buffer[2].pop(0)
    buffer[3].pop(0)
    buffer[4].pop(0)
    buffer[5].pop(0)
    return gyro,accl

def startlim(arrlim,vals):
    for i in range(len(arrlim)):
        arrlim[i] = [vals[i]] * 3
    return arrlim

def startlimpot(arrlim,vals):
    for i in range(len(arrlim)):
        arrlim[i] = vals
    return arrlim

def start(tsleep, tclear, samples,
          i2c=None, mpu=None, pots=None, vib=None):
    # inicializa hardware se não passado
    if i2c is None:
        i2c = init_i2c()
    if mpu is None:
        mpu = init_mpu(i2c)
    if vib is None:
        vib = init_vibrator()
    if pots is None:
        pots = init_pots()

    bufferPot = [[],[],[],[],[]]
    for i in range(40):
        pval = [pot.read() for pot in [pot1, pot2, pot3, pot4, pot5]]
        print(pval[0],pval[1],pval[2],pval[3],pval[4])
        getPots(bufferPot,pval)
        time.sleep_ms(70)

    maxCalibratePots = calcCalibrate(bufferPot)
    print(maxCalibratePots)

    num = 0

    buffer = [[],[],[],[],[],[]]

    for i in range(samples-1):
        getGyro(buffer)
        time.sleep_ms(70)

    gyro, accl = media(buffer)

    limgyro = [[],[],[]]

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

        gyro, accl = media(buffer)

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











