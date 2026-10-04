# FriendFocus AI: I Built a Tiny Local Planning Buddy for a Friend

> Hacktoberfest 2026 Weekend Challenge — Build for a Friend

My friend has a problem that looked simple from the outside: they had plenty of tasks, but when everything became urgent, deciding what to do first became the hardest part.

So I built **FriendFocus AI**.

It is a small planning assistant that takes a goal, a messy task list, available time, and real-world constraints and turns them into an actionable plan.

## The problem

[WRITE 2–4 TRUE SENTENCES ABOUT YOUR FRIEND'S ACTUAL PROBLEM HERE.]

The important part was that I did not want to build another giant productivity dashboard. My friend did not need more buttons. They needed help answering one question:

**“What should I actually do next?”**

## What I built

FriendFocus has five inputs:

- the friend's goal
- their tasks and obligations
- how much focused time they have
- their preferred focus-session length
- constraints such as classes, meetings, commuting, or low-energy periods

The model returns:

1. today's focus
2. priority order
3. a realistic schedule
4. a low-energy fallback
5. a short message for the friend

The interface is intentionally small because the product is the plan, not the dashboard.

## Why open-source AI was important

I used **Qwen2.5-0.5B-Instruct** through the open-source Hugging Face Transformers stack.

That choice was deliberate.

This app processes the kind of information people often keep in notes: deadlines, schedules, unfinished work, and personal constraints. I wanted the project to have a path toward local inference rather than requiring every prompt to be sent to a proprietary chatbot API.

Open models also make the architecture easier to change. The UI and prompt design can stay the same while the underlying model changes.

That matters because this project is small enough to be a learning experiment. I want to be able to inspect it, modify it, and replace the model without redesigning the whole application.

## How it works

```text
Friend's situation
       |
       v
   Gradio UI
       |
       v
  Structured prompt
       |
       v
Qwen2.5-0.5B-Instruct
       |
       v
 Actionable plan
```

The prompt explicitly asks for realistic prioritization and a fallback plan. It also tells the model not to invent commitments.

## A sample

Input:

> Goal: Prepare for next week's database exam  
> Tasks: revise normalization, practice SQL joins, review indexes, finish assignment  
> Time: 3 hours  
> Constraint: low energy after 8 PM

Output:

> **Today's focus:** SQL joins + normalization  
> **Priority:** 1) finish assignment 2) SQL practice 3) normalization review 4) indexes  
> **Schedule:** 45 min assignment → 10 min break → 45 min SQL → 10 min break → 45 min normalization → 25 min indexes  
> **Low-energy fallback:** do 20 minutes of index flashcards instead of a full study block

The goal is not to create the “perfect” timetable. The goal is to make starting easier.

## What I learned

The most useful design decision was keeping the scope narrow.

It is tempting to build reminders, calendars, analytics, streaks, accounts, and ten other features. But the friend's actual pain point was decision overload.

So I optimized for one useful action:

**turn chaos into the next few steps.**

## What I would build next

The next version could add calendar integration, a memory layer for recurring preferences, and a model selector so users can choose among different open models depending on their hardware.

I would also like to make a fully offline desktop version where the model and all planning data stay on the user's machine.

## Try it

**Demo:** [PASTE HUGGING FACE SPACE OR VIDEO LINK]

**Code:** [PASTE GITHUB REPOSITORY LINK]

## Built for a friend

[ADD ONE TRUE SENTENCE ABOUT WHAT YOUR FRIEND SAID AFTER SEEING/USING IT.]

That was the point of this challenge for me: not building an AI demo for everyone, but building one small thing that is useful to one person I know.

---

Built for Hacktoberfest 2026's **#hf26challenge** / **#weekendchallenge**.

#devchallenge #weekendchallenge #hf26challenge
