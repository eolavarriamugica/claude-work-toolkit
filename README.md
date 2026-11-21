# claude-work-toolkit

Small, independent plugins for Claude. Install only the ones you need.

| Plugin | Skill | What it does | Needs setup? |
|---|---|---|---|
| `plain-writing` | `de-ai-writer` | Rewrites text to remove "AI writing" patterns, then simplifies it. | No |
| `plain-writing` | `ste-simplifier` | Rewrites text with Simplified Technical English rules (short sentences, one idea each, plain words), in any language. Has an executive-summary mode. | No |
| `gmail-contacts-crm` | `contacts-crm` | Builds and refreshes a contacts spreadsheet from your own Gmail and Google Calendar: one row per real person, with company, title, reason for contact, status and next step. Read only. | **Yes** |
| `gmail-contacts-crm` | `contacts-crm-setup` | Interviews you and fills your contacts profile. Never invents a value. | Runs the setup |
| `financial-model-builder` | `financial-model-builder` | Builds Excel models (loans, comparators, breakeven, project costs) with blue inputs, formula-only outputs, schedules, scenarios and a formula error check. | No |

## Folder tree

```
claude-work-toolkit/
├── .claude-plugin/
│   └── marketplace.json            # lists the plugins
├── plugins/
│   ├── plain-writing/
│   │   ├── .claude-plugin/plugin.json
│   │   └── skills/
│   │       ├── de-ai-writer/SKILL.md
│   │       └── ste-simplifier/SKILL.md
│   ├── gmail-contacts-crm/
│   │   ├── .claude-plugin/plugin.json
│   │   ├── profile/contacts-profile.md     # BLANK template — fill your own copy, not this one
│   │   ├── templates/contacts-crm.xlsx     # BLANK spreadsheet: headers, formulas, dropdowns, no data
│   │   └── skills/
│   │       ├── contacts-crm/SKILL.md
│   │       └── contacts-crm-setup/SKILL.md
│   └── financial-model-builder/
│       ├── .claude-plugin/plugin.json
│       └── skills/financial-model-builder/
│           ├── SKILL.md
│           └── scripts/recalc_check.py     # recalculates with LibreOffice and lists formula errors
├── README.md
├── LICENSE                          # MIT
└── .gitignore                       # ignores my-profile/ and filled spreadsheets
```

## Before it works

`plain-writing` and `financial-model-builder` work right after install. Only `gmail-contacts-crm` needs a profile.

The easiest way is to say **"set up my contacts CRM"**: the `contacts-crm-setup` skill asks you each question and writes the file. Or fill it by hand:

**File: `contacts-profile.md`** (copy of `plugins/gmail-contacts-crm/profile/contacts-profile.md`)

| Field | Required? | Blocks |
|---|---|---|
| **My email addresses** (all of them) | **Required** | `contacts-crm` (it uses them to leave you out of your own list) |
| **Google account the connectors should read** | **Required** | `contacts-crm` (it stops if a different account is connected) |
| **Spreadsheet name** | **Required** | `contacts-crm` (it needs to know which sheet to create or update) |
| Spreadsheet ID or file path | Filled by the skill | — |
| Date of the last refresh | Filled by the skill | — |
| Language of the sheet | Optional | — (default: the language you write in) |
| Categories | Optional | First build waits until you accept a list |
| Category rules, domain → company names, addresses to ignore | Optional | — |
| Inactive year, second mailbox, months of threads to open | Optional | — (defaults in the template) |

When a required field is blank, the skill stops and asks. It never guesses.

## Where to keep your filled files

Your filled profile and your contacts spreadsheet hold personal data — yours and other people's. **Never commit them.**

| Where you use Claude | Put your filled `contacts-profile.md` here |
|---|---|
| Claude Code or Cowork | `my-profile/contacts-profile.md` in your working folder (this repo's `.gitignore` already ignores `my-profile/`) |
| Claude.ai | The files of a Project you use for this |

The skills look for the profile in this order: your project files → your working folder (including `my-profile/`) → the blank template in the plugin. Never type your values into the template inside the plugin folder: if you fork or republish this repo, they would go with it.

If you fork this repo, keep the `.gitignore` and check `git status` before each commit.

## Install

### Claude Code

```
/plugin marketplace add eolavarriamugica/claude-work-toolkit
/plugin install plain-writing@claude-work-toolkit
/plugin install gmail-contacts-crm@claude-work-toolkit
/plugin install financial-model-builder@claude-work-toolkit
```

Install only the plugins you want. To get updates later: `/plugin marketplace update claude-work-toolkit`.

### Cowork

Add the marketplace `eolavarriamugica/claude-work-toolkit` from the plugin settings, then install the plugins you want. The plugins are the same as in Claude Code.

### Claude.ai (web, desktop and mobile apps)

1. Download this repo as a ZIP and unzip it.
2. Zip each skill folder on its own (for example `plugins/plain-writing/skills/de-ai-writer/`) and upload it in the Skills section of your Settings.
3. For the contacts skills, also create a Project and add two files to it: your filled `contacts-profile.md` and the blank `templates/contacts-crm.xlsx`. Run the skills inside that Project.
4. For `financial-model-builder`, the error check script needs a code environment with LibreOffice. If it is not available, the skill tells you the check did not run.

## Connectors and tools needed

| Plugin | Needs | Why |
|---|---|---|
| `plain-writing` | Nothing | Text in, text out |
| `gmail-contacts-crm` | **Gmail** connector | Reads your sent threads (read only) |
| `gmail-contacts-crm` | **Google Calendar** connector | Reads meeting attendees and confirms which account is connected |
| `gmail-contacts-crm` | Google Sheets + Google Drive connectors (recommended) | Creates and updates the sheet. Without them, the skill fills a local `.xlsx` copy of the template |
| `financial-model-builder` | Python with `openpyxl` | Builds the Excel file |
| `financial-model-builder` | LibreOffice (`soffice`) | Recalculates formulas for the error check |

## Warnings

- **The contacts sheet holds other people's personal data.** Depending on where you live, data protection law (for example the EU's GDPR) may apply even to a personal list. Keep the sheet private, record only what you need, and never add sensitive details (health, family, religion, politics, salary). The skill refuses to add such columns.
- **Read only, by design.** `contacts-crm` never sends, replies to, forwards, labels or deletes email, and never changes calendar events. Follow-ups only go into the "Next step" column. If you ask for a follow-up email, it writes a draft and waits for you.
- **Connector access.** The Gmail and Calendar connectors can read your whole mailbox and calendar. Check which account is connected before the first run. The skill also checks and stops on a mismatch.
- **Guesses are labelled.** Anything the skill infers (a company from a domain, a category) is marked "(to confirm)" or left blank. Check those rows.
- **Check the result.** The writing skills keep your facts, numbers and names, but read the output before you send it.
- **Not financial advice.** `financial-model-builder` builds calculation tools. The decisions are yours.
- **No terms-of-use risks found.** None of these skills scrape websites or drive logged-in browser accounts. They use only your text, your own connected Google data and local files.

## Suggested recurring prompt

For `gmail-contacts-crm`, a weekly scheduled task (or just paste it when you want a refresh):

> Run the contacts-crm skill in refresh mode. Load my contacts profile first. Do not send or draft any email. Report in one short paragraph: new and updated contacts, the 1–3 people I should follow up with this week and why, and anything you could not read.

## Rules the skills follow

- Never invent a fact or value. When something needed is missing, stop and ask.
- Never send anything. Drafts only, and only when asked.
- Never overwrite what you typed by hand in the contacts sheet. Never delete rows.
- Same language as your input.
- Plain language, no unexplained acronyms.
- Zero formula errors before an Excel model is delivered; the error count is always reported.

## Licence

MIT. See `LICENSE`.
