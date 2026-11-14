# claude-work-toolkit

Small, independent plugins for Claude. Install only the ones you need.

More plugins are added here over the coming weeks.

| Plugin | Skill | What it does | Needs setup? |
|---|---|---|---|
| `plain-writing` | `de-ai-writer` | Rewrites text to remove "AI writing" patterns, then simplifies it. | No |
| `plain-writing` | `ste-simplifier` | Rewrites text with Simplified Technical English rules (short sentences, one idea each, plain words), in any language. Has an executive-summary mode. | No |
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

Nothing to fill in. The plugins here work right after install.

## Install

### Claude Code

```
/plugin marketplace add eolavarriamugica/claude-work-toolkit
/plugin install plain-writing@claude-work-toolkit
/plugin install financial-model-builder@claude-work-toolkit
```

Install only the plugins you want. To get updates later: `/plugin marketplace update claude-work-toolkit`.

### Cowork

Add the marketplace `eolavarriamugica/claude-work-toolkit` from the plugin settings, then install the plugins you want. The plugins are the same as in Claude Code.

### Claude.ai (web, desktop and mobile apps)

1. Download this repo as a ZIP and unzip it.
2. Zip each skill folder on its own (for example `plugins/plain-writing/skills/de-ai-writer/`) and upload it in the Skills section of your Settings.
3. For `financial-model-builder`, the error check script needs a code environment with LibreOffice. If it is not available, the skill tells you the check did not run.

## Connectors and tools needed

| Plugin | Needs | Why |
|---|---|---|
| `plain-writing` | Nothing | Text in, text out |
| `financial-model-builder` | Python with `openpyxl` | Builds the Excel file |
| `financial-model-builder` | LibreOffice (`soffice`) | Recalculates formulas for the error check |

## Warnings

- **Check the result.** The writing skills keep your facts, numbers and names, but read the output before you send it.
- **Not financial advice.** `financial-model-builder` builds calculation tools. The decisions are yours.
- **No terms-of-use risks found.** None of these skills scrape websites or drive logged-in browser accounts. They use only your text, your own connected Google data and local files.

## Rules the skills follow

- Never invent a fact or value. When something needed is missing, stop and ask.
- Never send anything. Drafts only, and only when asked.
- Same language as your input.
- Plain language, no unexplained acronyms.
- Zero formula errors before an Excel model is delivered; the error count is always reported.

## Licence

MIT. See `LICENSE`.
