# FriendFocus AI

FriendFocus AI is a small planning assistant built for a real friend who struggles to turn a long, messy list of study/work obligations into a realistic plan.

The app accepts a goal, tasks, available time, preferred focus-session length, and constraints. An open-weight model then turns that information into a practical plan with priorities, a schedule, a low-energy fallback, and a short message the friend can send to themselves.

## Why this fits Hacktoberfest 2026

This is a brand-new project for the **Hacktoberfest 2026 Weekend Challenge: Build for a Friend**.

The project uses **Qwen2.5-0.5B-Instruct** with the open-source **Hugging Face Transformers** stack. The model is part of the application logic: it is not a decorative AI feature layered over a closed API.

The project also keeps the architecture easy to modify. The model can be swapped later, and the prompt can be changed without rewriting the UI.

## Features

- Turns unstructured tasks into a prioritized plan.
- Respects available time and preferred session length.
- Includes a low-energy fallback plan.
- Generates a one-line message for the friend.
- Uses an open-weight model instead of a proprietary chatbot API.

## Run locally

Install Python 3.10+.

```bash
git clone <YOUR-REPO-URL>
cd friendfocus-ai
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python app.py
```

The first run downloads the model. Later runs can use the local Hugging Face cache.

## Deploy as a demo

The easiest public demo is a Hugging Face Space using the Gradio app.

1. Create a new Hugging Face Space.
2. Choose **Gradio**.
3. Upload `app.py` and `requirements.txt`.
4. Wait for the Space to build.
5. Add the public Space URL to the DEV submission.

For the challenge, the DEV rules require a demo (deployed link or video) and a link to the project's code.

## Friend story

Replace this paragraph with the truth about your friend:

> I built FriendFocus for [FRIEND'S FIRST NAME], a friend who [REAL PROBLEM]. They already had a notes app and a calendar, but the problem was deciding what to do next when everything felt important. I wanted to build a tiny tool that reduced that decision-making overhead instead of adding another complicated productivity system.

Do not invent a quote or claim that your friend tested it unless they actually did.

## Technical architecture

```text
Friend's inputs
      |
      v
Gradio UI
      |
      v
Prompt + constraints
      |
      v
Qwen2.5-0.5B-Instruct
      |
      v
Actionable plan
```

## Why open innovation mattered

Using an open-weight model makes the project easier to inspect, adapt, and replace. The application is not locked into a single proprietary model provider or API contract.

For a tool dealing with personal schedules and frustrations, having the option to run the model locally is also useful. The same prompt and UI can be kept while the model is swapped for another compatible open model.

## Limitations

The model is intentionally small so the project stays approachable. A larger model may produce more polished plans but requires more memory and compute.

FriendFocus is a planning aid, not a medical, financial, or professional decision-making system.
