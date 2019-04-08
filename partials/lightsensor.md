<h1>De micro:bits gebruiken als lichtsensoren (via Raspberry Pi)</h1>


**1..** Eerst en vooral willen we graag de bluetooth communicatie mogelijk maken tussen beide apparaten.
   De bluetooth in werking zetten op de Raspberry Pi kunnen we eenvoudig doen door Bluezero te installeren. Dit is de bluetooth stack voor linux. Hierna kan bluetooth gebruikt worden op je Pi.

**2..** Om de Micro:bit te koppelen via bluetooth maken we best gebruik van "passkey pairing". We installeren een hex file waarin we passkey pairing activeren. Dit proces is compleet wanneer we de 6 cijfers invoeren die getoond worden op de display van de Micro:bit

**3..** We kunnen nu de data van onze sensoren gaan monitoren en via de raspberry pi gaan verwerken.
   Zo kunnen we in javascript code schrijven die de invoer van de lichtsensor op de micro:bit kan evalueren en door enkele voorwaarden signalen via bluetooth naar de raspberry pi stuurt.

   **Dit script kan op de micro:bit zelfstandig draaien waardoor meerdere micro:bits tegelijk dit script draaien. Bovendien is het makkelijk om extra micro:bits toe te voegen en/of te verwijderen uit het systeem. Na het ontvangen van bepaalde signalen van de micro:bit(s) kan de raspberry pi deze gebruiken om bepaalde output te genereren.**

   **Dit kan in de vorm van bijvoorbeeld een log bijhouden, een melding naar de administrator sturen, visuele signalen terugsturen naar desbetreffende micro:bit ...**

<h2>Setup</h2>

**1.. Dependencies installeren**
Eerst en vooral moet bluezero worden geinstalleerd, dit kan eenvoudig door volgend commando:

    sudo pip3 install bluezero
    sudo reboot

**2.. Bluetooth instellen**
Met volgende commando activeer je de bluetooth tool:

    sudo bluetoothctl

Nu moet je controleren of de bluezero toestemming heeft om de bluetooth adapter te gebruiken door volgend commando:

    show

Als resultaat krijg je iets gelijkaardig aan dit:

    Controller B8:27:EB:B1:DC:13
            Name: raspberry-arvellon
            Alias: raspberry-arvellon
            Class: 0x480000
            Powered: yes
            Discoverable: no
            Pairable: yes
            UUID: Headset AG                (00001112-0000-1000-8000-00805f9b34fb)
            UUID: Generic Attribute Profile (00001801-0000-1000-8000-00805f9b34fb)
            UUID: A/V Remote Control        (0000110e-0000-1000-8000-00805f9b34fb)
            UUID: Generic Access Profile    (00001800-0000-1000-8000-00805f9b34fb)
            UUID: PnP Information           (00001200-0000-1000-8000-00805f9b34fb)
            UUID: A/V Remote Control Target (0000110c-0000-1000-8000-00805f9b34fb)
            UUID: Audio Source              (0000110a-0000-1000-8000-00805f9b34fb)
            UUID: Handsfree Audio Gateway   (0000111f-0000-1000-8000-00805f9b34fb)
            Modalias: usb:v1D6Bp0246d052B
            Discovering: no

Indien er 'Powered: yes' staat is alles in orde anders moet je eesrst nog de adapter activeren:

    power on

Normaal zou dit commando de adapter moeten activeren. Hoewel het mogelijk is dat bluezero geen toestemming heeft en dan krijg je volgende error:

    Failed to set power on: org.bluez.Error.Blocked

Dit kan je oplossen door bluezero toestemming te geven:

    exit
    rfkill unblock all

Nu kan je nogmaals proberen om de adapter te activeren:

    power on

En dan kan de de scan starten

    scan on

Wanneer de microbit in de lijst staat dien je het adres te kopieren (heeft volgende structuur: yy:yy:yy:yy:yy:yy)

**3.. De Micro:Bit pairen**
Nu moeten we de micro:bit pairen aan de raspberry pi door eerst de micro:bit in pairing modus te brengen. Dit gebeurd door beide buttons ingedrukt te houden en kort op de reset button te drukken. Houd de buttons (behalve de reset button) tot het bluetooth logo op de led matrix verschijnt, dan mag je alle buttons los laten. Nu kan je pairen door volgend commando:

    pair yy:yy:yy:yy:yy:yy
    (vervang yy:yy:yy:yy:yy:yy door het gekopieerde adres)

En nu ben je gepaired

