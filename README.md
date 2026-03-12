# AutoHub – Webová aplikace pro správu a hodnocení aut

## O projektu
Cílem projektu **_AutoHub_** je vytvořit interaktivní webovou aplikaci pro správu a hodnocení _aut_ a souvisejících entit, jako jsou _značky_, _modely_, _motorizace_ a _recenze_. Aplikace umožňuje různé role _uživatelů_: anonymní návštěvníky, registrované uživatele a administrátory.

Anonymní návštěvník může prohlížet seznam _aut_, filtrovat je podle _značky_, _modelu_ nebo _roku výroby_ a číst existující _hodnocení_ a _komentáře_ registrovaných uživatelů. Registrovaný uživatel má navíc možnost přidávat _recenze_, udělovat _hodnocení_ jednotlivým _autům_ a komentovat _recenze_ ostatních uživatelů. Administrátor má plnou kontrolu nad databází – může přidávat nové _auta_, spravovat _značky_, _modely_, mazat nevhodné _komentáře_ a monitorovat _aktivitu uživatelů_.

Databázová struktura je navržena tak, aby podporovala složité vazby: každé _auto_ je propojeno s konkrétní _značkou_ a _modelem_, a může mít jednu nebo více variant _motorizace_. _Hodnocení_ a _recenze_ jsou přiřazeny konkrétnímu _autu_ a _uživateli_, přičemž jeden _uživatel_ může hodnotit jedno _auto_ pouze jednou. _Komentáře_ mohou být vnořené a vztahovat se k recenzi nebo přímo k _autu_.

Rozhraní aplikace je koncipováno podle principu _mobile first_, aby bylo použitelné i na menších zařízeních. Klíčové prvky _UI_ zahrnují navigační panel, seznam _aut_ s obrázky, formuláře pro _hodnocení_ a _recenze_ a administrační _dashboard_ pro správu obsahu.

Cílem aplikace je poskytnout komplexní přehled o _aut_ a jejich parametrech, umožnit uživatelům sdílet zkušenosti, objevovat nové _značky_ a _modely_ a zajistit bezpečné prostředí pro _hodnocení_ a _komentáře_.

**Klíčové odborné termíny**: _auto, značka, model, motorizace, hodnocení, recenze, komentář, uživatel, administrátor, databázová struktura, entita, vazba, UI, UX, mobile first, dashboard_.

---

## User Flow
Diagram **User Flow** znázorňuje přechody mezi stránkami pro jednotlivé role uživatelů:

- **Homepage** – seznam doporučených aut, vyhledávání podle značky, modelu nebo roku výroby  
  → **Detail auta** – informace o autě, hodnocení, recenze  
  → **Přidat recenzi / hodnocení** (pouze registrovaní uživatelé)

- **Registrace / Přihlášení** – formuláře pro nové a stávající uživatele  
  → po úspěšném přihlášení přesměrování na **Homepage**

- **Uživatelský profil** – přehled vlastních recenzí a hodnocení, možnost editace  
  → odkaz na **Detail auta**

- **Admin dashboard** – správa aut, značek, modelů, motorizací, komentářů a uživatelů

Navigace mezi stránkami:
- Homepage ↔ Detail auta  
- Homepage ↔ Registrace / Přihlášení  
- Homepage ↔ Uživatelský profil  
- Admin dashboard ↔ všechny entity (auta, značky, modely, motorizace, uživatelé, komentáře)

---

## Wireframes
Níže jsou popsané wireframes jednotlivých stránek (mobile first):

### Homepage
- Hlavička: Logo | Menu: Home, Přihlášení, Registrace, Profil  
- Seznam aut: obrázek + značka + model + rok + hodnocení  
- Filtry: značka, model, rok, vyhledávání  
- Footer: kontakty, informace

### Detail auta
- Nadpis: Značka + Model + Rok  
- Obrázek auta, motorizace, výkon, spotřeba, parametry  
- Hodnocení (hvězdičky)  
- Recenze, možnost přidat vlastní  
- Tlačítko „Přidat recenzi“ (pouze registrovaní uživatelé)

### Registrace / Přihlášení
- Formulář: jméno, email, heslo, potvrzení hesla  
- Tlačítko Registrovat / Přihlásit  
- Odkaz: Zapomenuté heslo

### Uživatelský profil
- Přehled vlastních recenzí a hodnocení  
- Možnost editace / smazání  
- Odkaz na detail auta

### Admin Dashboard
- Menu: Auta, Značky, Modely, Motorizace, Uživatelé, Komentáře  
- Tabulky s entity + akce (edit, delete, add)  
- Statistiky aktivity uživatelů

### Images
- ![e-r diagram](e-r diagram.jpeg)
- ![diagram](diagram.jpeg)
- ![admin](admin.jpeg)
- ![wireframes](wireframes.jpeg)
