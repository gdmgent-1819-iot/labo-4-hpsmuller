// Workflow to enable pairing between Micro & Pi
// Linux terminal session

$ sudo hciconfig hci0 down
$ sudo hciconfig hci0 up
$ sudo bluetoothctl
    [NEW] Controller B8:27:EB:C5:E9:31 raspberrypi [default]
    [NEW] Device D0:F5:DF:C0:AE:95 BBC micro:bit
    [NEW] Device 90:03:B7:C9:9C:D8 Flower power 9CD8

[bluetooth]# scan on
    Discovery started
    [CHG] Controller B8:27:EB:C5:E9:31 Discovering: yes
    [CHG] Device D0:F5:DF:C0:AE:95 Name: BBC micro:bit
    [CHG] Device D0:F5:DF:C0:AE:95 Alias: BBC micro:bit

[bluetooth]# paired-devices
    Device D0:F5:DF:C0:AE:95 BBC micro:bit

[bluetooth]# remove D0:F5:DF:C0:AE:95
    [DEL] Device D0:F5:DF:C0:AE:95 BBC micro:bit
    Device has been removed

[bluetooth]# agent KeyboardDisplay
    Agent registered
    [NEW] Device D0:F5:DF:C0:AE:95 BBC micro:bit
    [CHG] Device 90:03:B7:C9:9C:D8 RSSI: -89

[bluetooth]# pair D0:F5:DF:C0:AE:95
    Attempting to pair with D0:F5:DF:C0:AE:95
    [CHG] Device D0:F5:DF:C0:AE:95 Connected: yes
    Request passkey
    [CHG] Device D0:F5:DF:C0:AE:95 UUIDs: 00001800-0000-1000-8000-00805f9b34fb
    [CHG] Device D0:F5:DF:C0:AE:95 UUIDs: 00001801-0000-1000-8000-00805f9b34fb
    [CHG] Device D0:F5:DF:C0:AE:95 UUIDs: 0000180a-0000-1000-8000-00805f9b34fb
    [CHG] Device D0:F5:DF:C0:AE:95 UUIDs: e95d93af-251d-470a-a062-fa1922dfa9a8
    [CHG] Device D0:F5:DF:C0:AE:95 UUIDs: e95d93b0-251d-470a-a062-fa1922dfa9a8
    [CHG] Device D0:F5:DF:C0:AE:95 Appearance: 0x0200

[agent] Enter passkey (number in 0-999999): 959145
    [CHG] Device D0:F5:DF:C0:AE:95 Paired: yes
    Pairing successful
    [CHG] Device D0:F5:DF:C0:AE:95 Connected: no
