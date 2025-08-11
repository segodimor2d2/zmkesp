import webrepl
'''
import network
import time

print("\nBoot...")
station = network.WLAN(network.STA_IF)

red = [
    ["r2d2rep", "3e4r5t6y7u"],
    ["wff5", "3e4r5t6y7u"],
    ["reno12", "3e4r5t6y7u"],
    ["R2D2", "3e4r5t6y7u"],
    ["wfesp32a", "5t6y7u8i9o"]
]

for i in red:
    station.active(True)
    print(f'Connecting to WiFi {i[0]}...')
    station.connect(i[0], i[1])
    time.sleep_ms(10000)

    if station.isconnected():
        print(f'\nConnected to {i[0]} with success.')
        print(f'Config: {station.ifconfig()}')
        time.sleep_ms(3000)
        break
    else:
        station.active(False)
    
if not station.isconnected():
    print('xxxxxx Error WiFi Connected xxxxxx')
    station.active(False)
'''
print("\n*****************************")
webrepl.start()
