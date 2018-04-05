import bluetooth, subprocess

target_name = "HC-05"
target_address = '98:D3:31:FD:73:A6'
'''
nearby_devices = bluetooth.discover_devices()

for b in nearby_devices:
    print(bluetooth.lookup_name(b))
    if target_name == bluetooth.lookup_name(b):
        target_address = b
        break
    
if target_address is not None:
    print("found target bluetooth device with address ", target_address)
else:
    print("could not find target bluetooth device nearby")
'''
if target_address is not None:
	port=1
	sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	sock.connect((target_address, port))
	print("connected")
	sock.send("<hello!!>")
	count=0
	
	#sock.settimeout(15)
	while(count<10):
		data=sock.recv(32)
		print("reveived: %s"%data)
		count=count+1
	sock.close()
else:
	print("Nope")
