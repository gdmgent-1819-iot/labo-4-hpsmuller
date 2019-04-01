<h1>De micro:bits gebruiken als lichtsensoren (via Raspberry Pi)</h1>

Eerst en vooral willen we graag de bluetooth communicatie mogelijk maken tussen beide apparaten.
De bluetooth in werking zetten op de Raspberry Pi kunnen we eenvoudig doen door BlueZ te installeren. Dit is de bluetooth stack voor linux. Hierna kan bluetooth gebruikt worden op je Pi.

Om de Micro:bit te koppelen via bluetooth maken we best gebruik van "passkey pairing". We installeren een hex file waarin we passkey pairing activeren. Dit proces is compleet wanneer we de 6 cijfers invoeren die getoond worden op de display van de Micro:bit

Workflow to enable pairing between Micro & Pi
Deze commando set kan je terugvinden in pair-devices.md

We kunnen nu de data van onze sensoren gaan monitoren en via de raspberry pi gaan verwerken.

Zo kunnen we in javascript code schrijven die de invoer van de lichtsensor op de micro:bit kan evalueren en door enkele voorwaarden signalen via bluetooth naar de raspberry pi stuurt.

Dit script kan op de micro:bit zelfstandig draaien waardoor meerdere micro:bits tegelijk dit script draaien en is het makkelijk om extra micro:bits toe te voegen en/of verwijderen uit het systeem. Na het ontvangen van bepaalde signalen van de micro:bit(s) kan de raspberry pi deze gebruiken om bepaalde outpot te genereren.

Dit kan in de vorm van bijvoorbeeld een log bijhouden, een melding naar de administrator sturen, visuele signalen terugsturen naar desbetreffende micro:bit, ...

<h2>Concrete aanpak</h2>

1. <h3>Installatie</h3>
De microbit kan plug and play gebruikt worden op de raspberry pi net zoals op een desktop OS. Voor hem te gebruiken in Python code moet moet een import gebruikt worden:
`from microbit import *`