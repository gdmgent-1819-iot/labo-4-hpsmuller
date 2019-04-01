<h1>De micro:bits gebruiken als lichtsensoren (via Raspberry Pi)</h1>

1. Eerst en vooral willen we graag de bluetooth communicatie mogelijk maken tussen beide apparaten.
   De bluetooth in werking zetten op de Raspberry Pi kunnen we eenvoudig doen door BlueZ te installeren. Dit is de bluetooth stack voor linux. Hierna kan bluetooth gebruikt worden op je Pi.

2. Om de Micro:bit te koppelen via bluetooth maken we best gebruik van "passkey pairing". We installeren een hex file waarin we passkey pairing activeren. Dit proces is compleet wanneer we de 6 cijfers invoeren die getoond worden op de display van de Micro:bit

Workflow to enable pairing between Micro & Pi
Deze commando set kan je terugvinden in pair-devices.md

3. We kunnen nu de data van onze sensoren gaan monitoren en via de raspberry pi gaan verwerken.
   Zo kunnen we in javascript code schrijven die de invoer van de lichtsensor op de micro:bit kan evalueren en door enkele voorwaarden signalen via bluetooth naar de raspberry pi stuurt.

Dit script kan op de micro:bit zelfstandig draaien waardoor meerdere micro:bits tegelijk dit script draaien en is het makkelijk om extra micro:bits toe te voegen en/of verwijderen uit het systeem. Na het ontvangen van bepaalde signalen van de micro:bit(s) kan de raspberry pi deze gebruiken om bepaalde outpot te genereren.

Dit kan in de vorm van bijvoorbeeld een log bijhouden, een melding naar de administrator sturen, visuele signalen terugsturen naar desbetreffende micro:bit, ...

<h2>Concrete aanpak</h2>

1. <h3>Installatie</h3>
   De microbit kan plug and play gebruikt worden op de raspberry pi net zoals op een desktop OS. Om hem te gebruiken in Python code moet moet een import gebruikt worden:
   `from microbit import *`



<h1>De micro:bit gebruiken als tracker voor je huisdier</h1>

De micro:bit sensoren voorzien ook de mogelijkheid om oriëntatie en beweging te registreren.
Dit deed ons denken in de richting van een tracker voor huisdieren.

   <h3>Aanpak</h3>

1. Als eerste maken we een oneindige loop aan, daar binnen zal alle code voor de tracking zich bevinden.

2. Vervolgens maken we 3 variabelen aan die de waarden van de accelerometer bijhouden.

   <h4>Declaring the variables that will hold the changes in movement</h4>
   Xdirection
   Ydirection
   Zdirection

3. Hierna zorgen we ervoor dat de variabelen de waarden bevatten conform de beweging van de accelerometer.
   De code zal er ongeveer uit zien als volgt

   <h4>Variables holding the new coordinates</h4>
   set Xmovement to acceleration (mg) X
   set Ymovement to acceleration (mg) Y
   set Zmovement to acceleration (mg) Z

4. Om verandering te registreren zullen we ook data moeten bijhouden die de huidige locatie vastlegt. Deze data wordt dan vergeleken met de nieuwe data. Deze logica kunnen we als volgt uitbouwen.

   <h4>Variables holding the old coordinates</h4>
   Xold <br>
   Yold <br>
   Zold <br>

   <h4>Logical operation, detect movement</h4>
   if Xmovement ≠ OldX ...

5. We stellen een threshold in die het programma pas activeert wanneer voldoende beweging wordt geregistreerd

   <h4>Declaring and initiate the threshold variables</h4>
   set Xdirection to 300 <br>
   set Ydirection to 300  --> Deze waarde kan worden ingesteld naar eigen voorkeur <br>
   set Zdirection to 300 <br>

   Ook hier zullen we een conditie schrijven die kijkt of de waarde van de treshold wordt overschreden
   (opnieuw gebruik van if statement)

6. Vervolgens gaan we de bluetooth feature activeren.
   - Onze micro:bit zal communiceren via een Android smartphone. <br>
   - Communicatie via 'Bluetooth Eddystone URL' <br>
   - Principe is dat de applicatie op ieder moment in staat is om de micro:bit te tracken volgens deze 'Bluetooth Eddystone URL' <br>


