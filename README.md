# Databáze aut

Databáze aut je lehká webová aplikace v Djangu, která slouží jako osobní portál pro správu a prohlížení automobilů. Aplikace umožňuje ukládat informace o různých vozidlech, filtrovat je, zobrazovat detailní data a mít vlastní přehledný katalog aut. Veškerá data jsou ukládána v databázi, žádné lokální soubory ani složité servery nejsou potřeba.

Cílem je vytvořit jednoduché, čisté a přehledné prostředí, kde si uživatel spravuje svůj vlastní seznam automobilů a má možnost snadno sledovat a třídit vozidla podle různých parametrů.

## Hlavní funkce
- **Správa katalogu aut:** Přidávání, editace a mazání aut s informacemi o značce, modelu, roku výroby, typu motoru, výkonu a ceně.
- **Filtrování a vyhledávání:** Snadné vyhledávání aut podle značky, modelu, roku nebo ceny.
- **Detailní informace:** Zobrazení všech parametrů auta na detailní stránce.
- **Označení oblíbených aut:** Možnost označit auta, která vás zajímají, pro rychlý přehled.
- **Responzivní web:** Moderní a přehledné prostředí díky Bootstrapu.

## Databázový návrh
- **Car**
  - `brand` – značka auta
  - `model` – model auta
  - `year` – rok výroby
  - `engine` – typ motoru
  - `horsepower` – výkon
  - `price` – cena
- **User** (Django standardní model)
  - `username`
  - `password`
  - další standardní pole pro autentizaci

## Architektura
1. Uživatel přistoupí na webovou stránku a vybere auto ze seznamu.
2. Django načte data z databáze a zobrazí je pomocí šablon (`home.html`, `about.html`, `detail.html`).
3. Pro přidání nebo úpravu auta se použije Django admin nebo vlastní formulář.
4. Data jsou uložena v SQLite (pro jednoduchost) nebo jiné databázi.

## Použité technologie
- **Python / Django** – backend a správa databáze
- **HTML5, CSS, Bootstrap 5** – responzivní frontend
- **JavaScript** – interaktivní prvky (např. filtrování a vyhledávání)
- **SQLite** – jednoduchá databáze pro lokální vývoj

## Budoucí rozšíření
- Možnost přidávat fotografie aut
- Filtry podle více parametrů (např. typ karoserie)
- Export seznamu aut do PDF nebo Excelu
- Uživatelské hodnocení aut a komentáře
