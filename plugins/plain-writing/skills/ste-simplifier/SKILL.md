---
name: "ste-simplifier"
description: "Rewrites text with Simplified Technical English (ASD-STE100) rules, in any language. Use when asked to simplify, shorten, or make text brief, concise, executive or plain (also: simplifica, breve, ejecutivo)."
---

# STE Simplifier

Rewrites text with the rules of ASD-STE100 Simplified Technical English (STE), adapted to work in any language. Goal: text that a reader cannot misread, with nothing extra.

Trigger words (any language): simplify, shorten, brief, concise, executive, plain, tighten, "make it clearer", executive summary. Spanish: simplifica, acorta, breve, conciso, ejecutivo, resumen ejecutivo, más claro.

## Scope and language

- Write the output in the same language as the input. Never translate unless the user asks.
- The official STE dictionary (about 900 approved words) is English-only. Do not call the output "STE-compliant". If asked, call it "STE-based".
- For languages other than English, apply each rule below with the closest natural equivalent in that language.
- Keep all original meaning, facts, numbers, names, dates and commitments. Never add facts.
- If the user also asks to remove AI writing tells, run de-ai-writer Pass 1 first, then this skill.

## Step 1: Classify the text

Classify each sentence:
- **Instruction**: tells the reader to do something. Use the procedure rules.
- **Description**: explains, informs or argues. Use the description rules.
- **Warning or caution**: a risk to people or equipment. Use the safety rules.

## Step 2: Words

1. **Use the most common word that is still exact.**

| Avoid (EN) | Use | Avoid (ES) | Use |
|---|---|---|---|
| utilize | use | llevar a cabo / realizar | hacer |
| commence | start | proceder a + verbo | the verb alone |
| facilitate | help | con el objetivo de | para |
| prior to | before | con anterioridad a | antes de |
| in order to | to | en el caso de que | si |
| accomplish | do | en relación con | sobre |
| subsequently | then | resulta necesario | hay que |

2. **One word, one meaning.** Do not use the same word with two different meanings in one text.
3. **One name per thing.** Once you name something, use that same name every time. Never switch to a synonym for variety.
4. **No acronyms or jargon.** Replace with plain words. If a technical name is necessary (a product, part, system or process with no plain equivalent), keep it and spell out any acronym on first use.
5. **Max 3 nouns stacked together.** "Customer data platform migration plan" becomes "the plan to migrate the customer data platform". Spanish: max 3 chained "de" complements. "El plan de migración de la plataforma de datos de clientes" becomes "el plan para migrar la plataforma de datos de clientes".
6. **Keep articles and short linking words** (the, a, this; el, la, este). No telegraphic style.
7. **Use the direct verb, not a noun built from it.** "Make a decision" → "decide". "Realizar la verificación" → "verificar".

## Step 3: Verbs

1. Use simple forms only: present, simple past, simple future, command, infinitive, and past participle used as an adjective ("the damaged part").
2. No complex tenses or stacked helper verbs. "Could potentially be able to" → "can". Spanish: "se estaría procediendo a revisar" → "revisamos".
3. English: no -ing forms except inside a technical name. Spanish: avoid gerunds that show a later action ("firmó el contrato, cerrando el acuerdo").
4. Active voice. Name who does the action. Spanish: avoid "fue aprobado por" and the impersonal "se" when the actor is known and matters.

## Step 4: Sentences

1. **Length caps:** instructions max 20 words; descriptions max 25 words. Count each word, number or hyphenated word as one.
2. **One idea per sentence.** One instruction per sentence, unless two actions must happen at the same time.
3. **Instructions are commands.** "Remove the cover." / "Quite la tapa."
4. **Condition before action.** "If the light comes on, stop the engine."
5. **Key information first.**
6. **No semicolons.** Split into two sentences.
7. **Use lists:** numbered for steps in sequence; bullets for 3 or more parallel items.
8. **Notes only give information.** Never hide an instruction inside a note.

## Step 5: Paragraphs

- One topic per paragraph.
- Max 6 sentences per paragraph.
- First sentence carries the main point.

## Step 6: Safety text (only if the text contains a real risk)

- Start with a short command: "Do not touch the hot surface."
- Then state the risk in one short sentence.
- Warning = risk of injury or death. Caution = risk of damage to equipment.

## Step 7: Cut

- Remove filler, throat-clearing, transitions, restated context and hedges that do not change meaning.
- Keep hedges that carry real uncertainty (an estimate, a forecast).
- Keep the shortest version that holds all the original meaning.

## Executive or brief mode

Apply when the user asks for "executive", "brief", "short", "summary" or similar:
1. Lead with the conclusion, or the decision the reader must take.
2. Then only the facts that support it.
3. Cut anything the reader does not need to decide or act.
4. Use labels like "Decision:" / "Decisión:" or "Reason:" / "Motivo:" when they make the text faster to scan.

## Check before output

- [ ] Every sentence within its cap (20 instructions / 25 descriptions)
- [ ] Max 6 sentences per paragraph
- [ ] No semicolons
- [ ] No noun stacks over 3
- [ ] Same name for the same thing throughout
- [ ] Active voice; actor named
- [ ] No unexplained acronyms or jargon
- [ ] Meaning, numbers, names and dates unchanged
- [ ] Same language as input

If a cap cannot be met without losing meaning (for example, a long official name), keep the meaning and accept the longer sentence.

## Output

The rewritten text only. No preamble, no explanation of changes unless the user asks.

## Examples

**English input (instruction with risk):**
"Prior to commencing the installation process, it is imperative that the technician ensures that all power sources have been disconnected, as failure to do so may result in serious injury; furthermore, the device should be inspected for damage."

**Output:**
"WARNING: Disconnect all power sources before you start the installation. Electrical power can cause serious injury.

Examine the device for damage."

**Spanish input (executive):**
"En relación con el proyecto de migración de la plataforma de gestión de datos de clientes, cabe destacar que, tras llevar a cabo un exhaustivo análisis, se ha procedido a determinar que el equipo actual resulta insuficiente; por consiguiente, se requiere la aprobación de la incorporación de dos personas más antes del 15 de noviembre."

**Output:**
"Decisión: aprobar dos personas más para el equipo antes del 15 de noviembre.
Motivo: el análisis muestra que el equipo actual no basta para migrar la plataforma de datos de clientes."