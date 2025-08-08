import time
import math
import mpu6050
from machine import Pin, SoftI2C, ADC, TouchPad
#from hid_services import Keyboard
import network
import espnow

print()
print('*********************************')

def send_charPs(abckey, stt, peer):
    msg = '%s;%s' % (abckey,stt)
    #e.send(peer, msg, True)
    e.send(peer, msg)

def vibrar(n_pulsos, step=None):
    for _ in range(n_pulsos):
        pino_vibracao.on()
        if step == 0:
            time.sleep_ms(200)
        else:
            #time.sleep_ms(70)
            time.sleep_ms(100)        
        #time.sleep_ms(200)
        pino_vibracao.off()
        time.sleep_ms(70)

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

def run(tsleep,tclear,samples,e,peer):

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

    abcR = abc[0]
    abclevel = abcR[0]

    vibrar(2)
    while True:

        #host, msg = e.recv()

        gyro, accl = media(buffer)
        #print(gyro[0],gyro[1],gyro[2])
        #print(accl[0],accl[1],accl[2])
        #print(gyro[0],gyro[1],gyro[2],accl[0],accl[1],accl[2])

        #--------------------------------------------
        if not evntTriggeredXP and not holdclick and gyro[gy1] > threshXP:
            if gy1 == 0: stepX += 1
            if gy1 == 1: stepX -= 1
            vibrar(1,stepX)
            evntTriggeredXP = True
            wait2Zero = False
            cycle = 0

        elif evntTriggeredXP and gyro[gy1] <= threshXP:
            evntTriggeredXP = False
            wait2Zero = True


        if not evntTriggeredXN and not holdclick and gyro[gy1] < threshXN:
            if gy1 == 0: stepX -= 1
            if gy1 == 1: stepX += 1
            vibrar(1,stepX)
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
            vibrar(1,stepX)

        if evntTriggeredXN: stepWaitXN += 1
        else: stepWaitXN = 0
        if stepWaitXN >= 5:
            if gy1 == 0: stepX -= 1
            if gy1 == 1: stepX += 1
            stepWaitXN = 0
            vibrar(1,stepX)
        #--------------------------------------------



        #--------------------------------------------
        if not evntTriggeredYP and not holdclick and gyro[gy2] > threshP:
            if gy2 == 0: stepY -= 1
            if gy2 == 1: stepY += 1
            vibrar(1,stepY)
            evntTriggeredYP = True
            wait2Zero = False
            cycle = 0

        elif evntTriggeredYP and gyro[gy2] <= threshP:
            evntTriggeredYP = False
            wait2Zero = True

        if not evntTriggeredYN and not holdclick and gyro[gy2] < threshN:
            if gy2 == 0: stepY += 1
            if gy2 == 1: stepY -= 1
            vibrar(1,stepY)
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
            if gy1 == 0: stepY += 1
            if gy1 == 1: stepY -= 1
            stepWaitYP = 0
            vibrar(1,stepY)

        if evntTriggeredYN: stepWaitYN += 1
        else: stepWaitYN = 0
        if stepWaitYN >= 5:
            if gy1 == 0: stepY -= 1
            if gy1 == 1: stepY += 1
            stepWaitYN = 0
            vibrar(1,stepY)
        #--------------------------------------------

        #print(stepY,stepX,stepWaitXP,stepWaitXN)


        #--------------------------------------------
        #maxCalibratePots
        pval = [pot.read() for pot in [pot1, pot2, pot3, pot4, pot5]]
        #print(pval[0],pval[1],pval[2],pval[3],pval[4])

        for i in range(len(pval)):
            pval[i] = pval[i]-maxCalibratePots[i]

        #print(pval[0],pval[1],pval[2],pval[3],pval[4])
        #pval = [pot.read() for pot in [pot1]]
        #print (pval[0])

        '''
        if num == 0: startlim(limpot, [pval[0],pval[1],pval[2],pval[3]])
        calclim(limpot[0],pval[0])
        calclim(limpot[1],pval[1])
        calclim(limpot[2],pval[2])
        calclim(limpot[3],pval[3])
        print(limpot[0][0],limpot[1][0],limpot[2][0],limpot[3][0])
        '''

        #if num == 0: startlimpot(limpot, [4050, 2800, 2800])

        if stepY == 2 and stepX == -1: abclevel = abcR[0][0]
        elif stepY == 1 and stepX == -1: abclevel = abcR[0][1]
        elif stepY == 0 and stepX == -1: abclevel = abcR[0][2]
        elif stepY == -1 and stepX == -1: abclevel = abcR[0][3]
        elif stepY == -2 and stepX == -1: abclevel = abcR[0][4]

        elif stepY == 2 and stepX == 0: abclevel = abcR[1][0]
        elif stepY == 1 and stepX == 0: abclevel = abcR[1][1]
        elif stepY == 0 and stepX == 0: abclevel = abcR[1][2]
        elif stepY == -1 and stepX == 0: abclevel = abcR[1][3]
        elif stepY == -2 and stepX == 0: abclevel = abcR[1][4]

        elif stepY == 2 and stepX == 1: abclevel = abcR[2][0]
        elif stepY == 1 and stepX == 1: abclevel = abcR[2][1]
        elif stepY == 0 and stepX == 1: abclevel = abcR[2][2]
        elif stepY == -1 and stepX == 1: abclevel = abcR[2][3]
        elif stepY == -2 and stepX == 1: abclevel = abcR[2][4]


        for i in range(5):
            if not triggerPot[i] and pval[i] < threshPot[i]:

                # >>> evento
                #print(i)
                print(stepY,stepX,'\t',abclevel[i],cycle)
                #print(stepY,stepX,'\t',abclevel[i],threshPot[i],pval[i],cycle)

                #send_charPs(abclevel[i], kb)
                send_charPs(abclevel[i], 1, peer)
                triggerPot[i] = True
                holdclick = True
                wait2Zero = False
                cycle = 0

            elif triggerPot[i] and pval[i] >= threshPot[i]:
                #send_charRl(kb)
                send_charPs(abclevel[i], 0, peer)
                triggerPot[i] = False
                holdclick = False
                wait2Zero = True

            #if triggerPot[i]:
            #   print(triggerPot[i])
        
        #--------------------------------------------
        #if msg:
        #    print(msg)


        if wait2Zero: cycle += 1
        if cycle == 20:
            stepY = 0
            stepX = 0
            vibrar(2)

        if num % tclear == 0: num = 0

        num+=1
        time.sleep_ms(tsleep)

'''
def advertising(kb):
    print('\n.......................start_advertising')
    kb.start_advertising()
    while True:
        if kb.get_state() == 3:
            print('tf2kb connected!')
            kb.stop_advertising()
            break
        time.sleep_ms(1000)
        print('...')
'''

#---------------------------------------------------------------
print('\n.......................')
#kb = Keyboard("tf2kb")
#kb.set_state_change_callback(None)
#kb.start()

#advertising(kb)
#kb.get_state()
#1 si kb.get_state() DEVICE_IDLE = desconectado
#2 si kb.get_state() DEVICE_ADVERTISING = disponibilidade
#3 si kb.get_state() DEVICE_CONNECTED = conectaado

#---------------------------------------------------------------
print('\n.......................')
#if kb.get_state() == 3:

from hidcodes import hidcodes, abc 

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
mpuSensor = mpu6050.accel(i2c)

pino_vibracao = Pin(32, Pin.OUT)

vibrar(4)


'''
pot1 = ADC(Pin(34))
pot2 = ADC(Pin(35))
pot3 = ADC(Pin(32))
pot4 = ADC(Pin(33))
#pot5 = ADC(Pin(39))

pot1.atten(ADC.ATTN_11DB)
pot2.atten(ADC.ATTN_11DB)
pot3.atten(ADC.ATTN_11DB)
pot4.atten(ADC.ATTN_11DB)
#pot5.atten(ADC.ATTN_11DB)
'''

pot5 = TouchPad(Pin(33)) #
pot4 = TouchPad(Pin(13)) #
pot3 = TouchPad(Pin(15)) #
pot2 = TouchPad(Pin(04)) #
pot1 = TouchPad(Pin(27)) #

# ESPNOW - A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)
sta.active(True)
#sta.disconnect()   # Because ESP8266 auto-connects to last Access Point
e = espnow.ESPNow()
e.active(True)
peer = b'\xbb\xbb\xbb\xbb\xbb\xbb' # MAC address of peer's wifi interface
e.add_peer(peer) # Must add_peer() before send()

#---------------------------------------------------------------
TSLEEP=50
TCLEAR=10000
#TCLEAR=10000
SAMPLES = 5 

run(TSLEEP,TCLEAR,SAMPLES,e,peer)








