# MASTER PROMPT — League Rulebook Builder
(Naye Claude chat me yeh poora message paste karen, saath me apni league ki files upload karen)

---

Bhai, mujhe is league ka **real, verified data** se ek "Master Rulebook" system banana hai. Neeche poora tareeqa likha hai — isay exactly follow karna.

## STEP 1 — DATA VERIFY KARO (kisi bhi table/rule banane se PEHLE)

Jo bhi files main upload karoon, unhe pehle yeh check karo:

1. **Season dates sahi hain?** — season shuru hone ki asal tareekh se match check karo (web search karo agar zaroorat ho). Agar koi match season shuru hone se pehle ki date par hai, yeh fake hai.
2. **Fixture ka structure real hai?** — asal league schedule me har hafte 8-10 alag matches hote hain, mix teams ke sath. Agar file me ek team ke saare home matches pehle grouped hain (alphabetical round-robin), yeh generated/fake data hai.
3. **Final table verify karo** — is data se points table banao (win=3, draw=1) aur us season ke asal champion/standings se compare karo (web search karo). Agar match nahi hota, yeh fake hai — ROOK JAO, aage mat badho.
4. **Malformed fields check karo** — ghalat date format (jaise "01/010/2024"), truncated text fields (fixed length par cut), ya har row me exactly same missing values — yeh generation ki nishaniyan hain.
5. Agar data fake nikle: seedha bata do "yeh data fake hai" aur wajah batao. Us par koi rulebook mat banao.
6. Agar real nikle: confirm karo "X real data hai, verify ho gaya (Y standings match hue)" — phir aage badho.

## STEP 2 — DATA MERGE KARO (agar multiple files hain)

Agar match results, goal-minutes, xG/stats, aur odds alag-alag files me hain:

- Merge hamesha **season + home_team + away_team + score** ko key bana kar karo — sirf team+score use karna KHATARNAK hai (do seasons me same scoreline repeat ho sakti hai aur duplicate rows ban jayengi).
- Team names normalize karo (jaise "Manchester City" = "Man City" = "Man. City") — ek dictionary banao dono sources ke naam ke liye.
- Merge ke baad **row count check karo** — total rows season ke asal match count se zyada nahi honi chahiye (EPL = 380/season, La Liga = 380/season, wagera). Agar zyada hai, duplicate bug hai — dhoondh kar theek karo.
- Jahan bhi data missing ho (kisi source me match nahi mila), woh field **khaali (blank/NaN) rakho** — kabhi bhi andaza laga kar number mat daalo.

## STEP 3 — SIRF 2 FILES BANAO (har league ke liye, is se zyada KABHI nahi)

1. **`[league]_MASTER_data.xlsx`** — ek hi Excel file, seasons ki alag alag sheets me (Sheet 1 = 2023-24, Sheet 2 = 2024-25, Sheet 3 = 2025-26, Sheet 4 = 2026-27). Column order: season, Date, HomeTeam, AwayTeam, **Score** (FT score jaise "2-1"), **Goal_Minutes** (Score ke turant baad; "Team:minute, Team:minute" format), phir baaki columns (HT score, shots/corners/cards, odds, xG). Goal_Minutes column wrap-text par ho aur row height itni ho ke lambi line usi box me neeche wrap ho jaye.
2. **`[league]_MASTER_rulebook.md`** — neeche diye gaye sections ke sath.

**CSV, alag season files, ya koi extra file output me mat rakho.** Sirf yeh 2 files. Agar league pehle se maujood hai to unhe replace/update karo.

**Zaroori:** isi ek `.xlsx` databook me, processed season-sheets (2023-24, 2024-25, wagera) ke BAAD, har original upload ki hui file bhi ek alag sheet ki soorat me 'RAW_' prefix ke saath rakho (jaise RAW_api_matches, RAW_api_goals, RAW_fd_2324). Isse: (a) koi bhi doosra AI chat samajh sake ke final data kis raw source se bana hai, (b) agar merge me koi ghalti mile to original raw sheet dekh kar theek ki ja sake.

## STEP 4 — RULEBOOK KE ZAROORI SECTIONS

1. **Source aur verification note** — kahan se data aya, kitne matches, verify kaise hua
2. **Result & Goals** — home/draw/away %, over/under 0.5 se 5.5, BTTS
3. **Half-time → Full-time** — HT lead kitni baar hold hui (overall aur 2+ lead alag se)
4. **Goal ka minute** — last-10-minute goals ka %, aur kya woh sirf margin badalte hain ya result ka type bhi
5. **xG team profiles** — kaunsi team apni xG se zyada/kam goal kar rahi hai (jahan xG data mile)
6. **Real Odds Calibration** — sirf tab jab asli bookmaker odds mile ho (fake mat banao). Bookmaker ka overround/margin nikalo, aur agar sample bara ho to implied-probability vs actual-result table banao
7. **Team-specific HT lead-hold aur comeback-rate table** — har team ka: jab aage thi kitni baar jeeti (%), jab peeche thi kitni baar haari nahi (%) — sample size (n) bhi likho
8. **Rules — honest limits** — 5-6 numbered rules, har ek me percentage aur caveat
9. **Confidence Scale** (neeche diya hua) — poori tarah copy karo
10. **Total rules/lessons ka summary table** — har rule ka ek-line punchline

## STEP 5 — CONFIDENCE SCALE (yeh section rulebook me EXACTLY yeh likhna)

```
| Percentage | Score | Zone naam |
|---|---|---|
| 90-99% | 9/10 | Strong Zone |
| 80-89% | 8/10 | Strong Zone |
| 70-79% | 7/10 | Good Zone |
| 60-69% | 6/10 | Lean Zone |
| 50-59% | 5/10 | Coin-flip — bet na karen |
| <50% | 4/10 ya kam | Weak / opposite side dekhen |
```
10/10 KABHI nahi milega — kisi bhi real football data me koi cheez 100% nahi hoti.

## HARD RULES (yeh kabhi mat tोड़ना)

1. **"Pakka" ya "guarantee" lafz kabhi mat bolo.** Sirf percentage + /10 score + zone naam.
2. **Chhote sample (n<15-20) par bhara confidence mat do** — sample size hamesha likho.
3. **Live-match "lessons" jo sirf 1-5 matches dekh kar bani hon** — unhe "verified rule" mat kaho. Sirf poore-season (300+ match) data se nikle patterns hi rulebook me jayen.
4. **Kabhi fake/invented odds ya stats mat banao** agar woh file me nahi hain — khaali chhodo, "data available nahi" likho.
5. **Har numerical claim khud calculate/verify karo** (code chala kar), kisi doosri file/chat se number copy-paste mat karo bina verify kiye.
6. Money-management ya staking "rules" mat banao — yeh sirf data-analysis hai, betting-behavior instructions nahi.

## STEP 6 — AAGE KA ISTEMAAL

Jab bhi main future me live match ka screenshot ya sawal bhejoon:
- Rulebook ke relevant rules dhoondo, unka percentage + /10 score + zone naam batao
- Sample size ka zikar karo
- Kabhi "pakka" mat kaho

---

**Ab yeh sawal mera poochna:** kaunsi league ka data hai, aur kaunsi files upload kar raha hoon? (finished matches / goals-minutes / stats-xG / odds — jo bhi maujood hain)
