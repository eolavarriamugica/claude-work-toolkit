---
name: contacts-crm
description: "Builds or refreshes a personal contacts spreadsheet from the user's own Gmail and Google Calendar: one row per real person, with company, title, first and last contact, reason for contact, category, status and next step. Use when the user says \"build my contacts list\", \"update my CRM\", \"add my new contacts\", \"who have I been talking to\" or \"run the contacts sheet again\"."
---

# Contacts CRM

Turns the user's connected Gmail and Google Calendar into a contacts spreadsheet: one row per real person,
with who they are, why the user was in touch, when, and what to do next. Two modes:

- **Build**: first run, or the user asks to start over.
- **Refresh**: the spreadsheet already exists. Add new people, update existing rows, keep the user's manual edits.

## Step 0: Load the profile (always first)

1. Look for `contacts-profile.md` in this order, and use the first one found:
   1. the user's project files (a claude.ai Project, or a Cowork project);
   2. the working folder, including a `my-profile/` subfolder;
   3. `${CLAUDE_PLUGIN_ROOT}/profile/contacts-profile.md` (the blank template).
2. Check the three **Required** fields. If any is blank (`____`) or missing, stop. Tell the user which
   fields are missing and offer to run the `contacts-crm-setup` skill. Never guess them.
3. Optional fields that are blank use the default written in brackets in the profile. The one exception is
   **Categories**: if blank, show the user a short proposed list once, before the first build, and wait for
   their answer. Do not write rows with categories they have not accepted.

## Step 1: Check which account is connected

Call Google Calendar `list_calendars` and read the primary calendar id. That is the connected Google account;
Gmail is usually the same one.

If it is not the account in the profile, stop. Tell the user which account is connected and that they must
reconnect Gmail and Calendar in their connector settings. Never build from the wrong mailbox.

A second mailbox (optional profile field) is a separate run: the user reconnects the connectors to that account,
and every contact found there gets the category written in the profile and Source = "Gmail <that address>".

## Step 2: Pull Gmail correspondents

- **Query**: `search_threads` with `in:sent`, metadata-only view, page size 50. Follow `nextPageToken` until it
  runs out. A sent thread means the user actually wrote, which removes most noise.
- **Refresh mode**: add `after:YYYY/MM/DD`, using the latest "Last contact" date in the spreadsheet.
- **Large mailboxes**: results get cut after a couple of pages in one context. Hand the remaining pages to a
  subagent with the starting page token. It writes a CSV (`email,first_date,last_date,n_messages,thread_ids`)
  and returns only row counts and the date range.
- **Per address**: for every sender, to and cc address, record the first date, the last date and the message count.
- **Always exclude**: no-reply addresses; unsubscribe addresses; mailer-daemon and postmaster; calendar
  notifications; support-ticket and marketing platforms (for example Intercom, Mailchimp, applicant-tracking
  systems); privacy@ and support@ system inboxes; placeholder addresses; anything listed in the profile's
  "Extra addresses or domains to ignore".
- **Keep**: recruiting or HR inboxes staffed by people (for example hr@, recruiting@). Title = "Recruiting inbox".
- **Search results show at most a few messages per thread.** Never state how a thread ended from search
  results alone. Call `get_thread` first.

## Step 3: Pull calendar attendees

Call `list_events` on the primary calendar with local start and end times (no `Z` suffix), page size 250,
newest first. If the result is too large to read inline, it is saved to a file: parse it with Python.

- **Take**: attendee email, display name (the best source of real names), event date and event title.
- **Skip**:
  - meeting rooms and other resources;
  - personal-domain attendees (gmail, outlook, hotmail, student or alumni domains) at group events such as
    webinars or assessment days — keep only company-domain attendees there;
  - reminder events with a single attendee that show only a first name.

## Step 4: Merge and enrich

Merge everything by lowercase email. Drop every address in the profile's "My email addresses".

Fill the columns:

- **Company**: from the email domain, using the profile's domain → company list first. Leave it blank for
  personal domains (gmail, outlook, hotmail, icloud, local internet providers). Never invent a company.
- **Name**: calendar display name first; otherwise split a `first.last` address. Blank for role inboxes.
- **Title**: only from an email signature, a calendar title or the thread itself. Otherwise blank.
- **Reason for contact**: a short factual phrase plus the subject or event title
  (for example "Hiring process – first interview").
- **Category**: from the profile's category rules. If no rule fits, use "To confirm".
  A shared surname or an unknown personal address is "To confirm", never a family label.
- **Status**: "Inactive" if the last contact is before the profile's inactive year.
- **Contacts from the recent window** (profile, default 12 months): open the thread with `get_thread`
  (full text for the latest message, minimal for the rest). Write the real status and a concrete next step
  with a date, for example "If no news by <date>, write again".
- **Label every guess** with "(to confirm)". A guess must never look like a fact.

## Step 5: Write the spreadsheet

The template `contacts-crm.xlsx` is in `${CLAUDE_PLUGIN_ROOT}/templates/`. If that path does not exist (for example
the skill was uploaded to claude.ai on its own), look for `contacts-crm.xlsx` in the project files or working folder.
If it is in neither place, build the same layout from the column list below.

Destination:
- **Google Sheets connector available**: find the spreadsheet by the ID in the profile, else search Drive for its
  name. If none exists (build mode), create it from the column layout in
  `${CLAUDE_PLUGIN_ROOT}/templates/contacts-crm.xlsx` and write the new ID into the user's profile copy.
- **No Sheets connector**: copy `${CLAUDE_PLUGIN_ROOT}/templates/contacts-crm.xlsx` into the working folder,
  fill it there and give the user the file.

Columns, in this order (A–N): Name | Email | Company | Title | First contact year | Last contact | Messages |
Reason for contact | Category | Status | Next step | Source | Notes | Days since last contact.
Column N is a formula; never type into it.

1. Save the rows to a JSON file first. For large uploads, hand the writing to a subagent in chunks of about 60 rows.
   Year and message count are numbers; Last contact is a date.
2. **Build mode**: clear `Contacts!A2:M` first. Keep the header and the formulas in column N.
3. **Refresh mode**: read the spreadsheet first and match rows by email.
   - Existing rows: update only Last contact, Messages and Source.
   - Update Status and Next step only if the user has not edited them.
   - Never overwrite Name, Title, Reason, Notes or anything else the user typed.
   - New people become new rows.
4. **Formatting**: bold header with a grey background, row 1 frozen, a filter over the whole table, wrapped text
   in columns H, K and M, sorted by Last contact (newest first).
5. **Verify**: read back the first 3 and last 3 rows and confirm they match the JSON file.
6. Write today's date into the profile's "Date of the last refresh".

## Step 6: Report back

One short paragraph, in the language the user wrote in:
- total contacts and the date range covered;
- how many are new or updated;
- the 1–3 people who need action now, and why;
- the gaps: sources not connected (for example a work mailbox), and which fields are guesses.

Put the link (or the file) in the reply.

## Rules

- **Read only.** Never send, reply to, forward, label or delete email. Never accept or change calendar events.
  Follow-ups go only into "Next step". If the user asks for a follow-up email, write a draft and wait for approval.
- **No sensitive columns.** Never record health, family matters, religion, politics, salary or similar details
  about a contact, even if an email mentions them.
- **Never delete rows.** If a contact is wrong, say so in Notes and let the user remove it.
- **Confirm the account before the first run.** If a different mailbox is connected, say so before anything else.
- **Never guess a required profile field.** Stop and ask.
- The spreadsheet holds other people's personal data. Never publish, share or upload it anywhere unless the user asks.
