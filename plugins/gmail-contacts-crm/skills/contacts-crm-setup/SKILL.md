---
name: contacts-crm-setup
description: "Sets up the contacts-crm skill for a new user: interviews them, reads any documents they point to, and fills their own copy of contacts-profile.md. Never invents a value. Use on first install, when contacts-crm reports a missing profile field, or when the user says \"set up my contacts CRM\" or \"update my contacts profile\"."
---

# Contacts CRM setup

Creates or updates the user's own `contacts-profile.md`. The rule that matters most: **every value comes from
the user or from a source they pointed to. Never invent, guess or fill a value "as an example".**

## Step 1: Find or create the user's copy

1. Look for an existing `contacts-profile.md` in the user's project files, then in the working folder
   (including `my-profile/`). If found, use it and fill only what is blank or what the user wants changed.
2. If none exists, copy the blank template `${CLAUDE_PLUGIN_ROOT}/profile/contacts-profile.md` (if that path does
   not exist, ask the user to add the blank `contacts-profile.md` from the plugin's repository to the project) to:
   - `my-profile/contacts-profile.md` in the working folder (Claude Code or Cowork), or
   - the user's claude.ai Project files, if the session is attached to a Project and the user agrees.
3. Never write the user's values into `${CLAUDE_PLUGIN_ROOT}/profile/` — that is the blank template
   that ships with the plugin, and it may be inside a folder the user publishes.

## Step 2: Read what the user offers

Ask once: "Do you have anything I can read to fill this faster? For example your email signature, a list of your
email addresses, or an old contacts spreadsheet." Read only what they point to. If a connector is available and
the user agrees, you may also:
- call Google Calendar `list_calendars` to read which account is connected (show it, and ask the user to confirm
  it is the right one);
- search Drive for a spreadsheet name the user gives, to find its ID.

Do not read the mailbox to "discover" addresses or categories. Building the list is the main skill's job.

## Step 3: Interview for the gaps

Ask only for fields that are still blank. Use AskUserQuestion when it is available (up to 4 questions at a time);
otherwise ask in plain text. Order:
1. All of the user's own email addresses (work, personal, old ones). These are never added as contacts.
2. The Google account the connectors should read.
3. The spreadsheet name.
4. Then, optional: language, categories and their rules, domain → company names, addresses to ignore,
   inactive year, a second mailbox, months of threads to open.

For categories, the user may ask you to propose a list. You may suggest generic ones (for example "Work",
"Former colleagues", "Personal", "To confirm"), but write only the ones the user accepts.

If the user says "skip" or "I don't know", leave the field as `____`. Never fill it with a guess.

## Step 4: Save and confirm

1. Write the file. Keep the table layout of the template.
2. Show the user a short summary: fields filled, fields still blank, and whether the three required fields are
   complete.
3. Remind them in one line where the file is and that it holds personal data: keep it out of any repository
   they publish (the plugin's `.gitignore` already ignores `my-profile/`).
4. If the required fields are complete, offer to run `contacts-crm` in build mode.
