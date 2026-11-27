# Groep 5 – Plaagdetectie

## Doel
Een online databron voor automatische plaagdetectie, risicoanalyse en biologische bestrijding in de glastuinbouw.

## Beschikbare data
- 1.800 fictieve vangplaatmetingen.
- Drie kassen met ieder vijf vakken.
- Historische gegevens over 30 dagen.
- Trips, witte vlieg, mineervlieg en bladluis.
- Risicoscores en plaagalarmen.
- Adviezen voor biologische bestrijding.

## API-endpoints

- `/vangsten` – Historische vangplaatmetingen.
- `/risico` – Risicoanalyse op basis van plaagdruk, temperatuur en luchtvochtigheid.
- `/alarmen` – Actuele plaagalarmen.
- `/bestrijding` – Kennisdatabase biologische bestrijding.
- `/docs` – Interactieve API-documentatie.

## Technologie

Python, FastAPI, Uvicorn en Render.

## Samenwerking

De API is bedoeld voor samenwerking met andere AI-agents, waaronder klimaat- en gewasagents.

## Veiligheid

Alle gegevens zijn fictief. Er worden geen persoonsgegevens, wachtwoorden of bedrijfsgegevens gebruikt. De risicomodellen zijn uitsluitend bedoeld voor demonstratiedoeleinden.
