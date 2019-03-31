**oi**
// De mirco:bits gebruiken als lichtsensoren (via Raspberry Pi) //

Eerst en vooral willen we graag de bluetooth communicatie mogelijk maken tussen beide apparaten.
De bluetooth in werking zetten op de Raspberry Pi kunnen we eenvoudig doen door BlueZ te installeren. Dit is de bluetooth stack voor linux. Hierna kan bluetooth gebruikt worden op je Pi.

Om de Micro:bit te koppelen via bluetooth maken we best gebruik van "passkey pairing". We installeren een hex file waarin we passkey pairing activeren. Dit proces is compleet wanneer we de 6 cijfers invoeren die getoond worden op de display van de Micro:bit

// Workflow to enable pairing between Micro & Pi
Deze commando set kan je terugvinden in pair-devices.md

We kunnen nu de data van onze sensoren gaan monitoren en via de raspberry pi gaan verwerken.


