# Contacts profile

Fill this in once (or run the `contacts-crm-setup` skill, which asks you and fills it for you).
Keep your filled copy OUTSIDE this plugin folder — see "Where to keep your filled files" in the README.
Leave a field as ____ if it does not apply; the skills stop and ask when a REQUIRED field is blank.

## Required (the contacts-crm skill will not run without these)

| Field | Value |
|---|---|
| My email addresses (all of them; one per line or comma-separated; these are never added as contacts) | ____ |
| Google account the Gmail and Calendar connectors should read | ____ |
| Spreadsheet name for the contacts list | ____ |

## Filled in by the skill after the first build (leave blank)

| Field | Value |
|---|---|
| Spreadsheet ID (Google Sheets) or file path (.xlsx) | ____ |
| Date of the last refresh (YYYY-MM-DD) | ____ |

## Optional (blank = the default in brackets)

| Field | Value |
|---|---|
| Language of the spreadsheet content [same as the language you write to Claude in] | ____ |
| Categories for the "Category" column, one per line [the skill asks you before the first build] | ____ |
| Rules to assign a category (e.g. "domain example.com → Former colleagues") | ____ |
| Email domain → company name, when the domain does not show the name clearly | ____ |
| Extra addresses or domains to ignore (newsletters, tools you use) | ____ |
| Year before which a contact is marked Inactive [two calendar years before this year] | ____ |
| Second mailbox to include, and the category its contacts always get | ____ |
| How many months back to open threads and write a real next step [12] | ____ |
