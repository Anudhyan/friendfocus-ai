# FriendFocus AI: I Built a Tiny Local Planning Buddy for a Friend

> Hacktoberfest 2026 Weekend Challenge — Build for a Friend

A friend of mine was dealing with a surprisingly common problem: having too many things to do and not knowing what to tackle first.

The problem was not a lack of motivation or a lack of productivity apps. The real issue was decision overload. When several assignments, study sessions, personal tasks, and deadlines appeared at the same time, even deciding where to start became stressful.

So I built **FriendFocus AI**, a small planning assistant designed to turn a messy list of responsibilities into a realistic plan.

## The problem

For this prototype, I imagined a friend preparing for an upcoming database exam while also managing regular coursework and personal commitments. They had a long list of tasks, but no simple way to decide which ones deserved attention first.

They did not need another complicated productivity dashboard. They needed an answer to a much simpler question:

**“What should I actually do next?”**

That became the idea behind FriendFocus.

## What I built

FriendFocus takes five pieces of information:

- the friend's main goal
- their tasks and obligations
- the amount of focused time available
- their preferred focus-session length
- constraints such as classes, meetings, commuting, or low-energy periods

The AI then produces:

1. today's main focus
2. a prioritized task order
3. a realistic schedule
4. a low-energy fallback plan
5. a short motivational message

I intentionally kept the interface small. The goal was not to create another productivity platform. The goal was to make planning easier.

## Why open-source AI was important

I used **Qwen2.5-0.5B-Instruct** with the open-source **Hugging Face Transformers** ecosystem.

This was a deliberate choice.

Planning often involves personal information such as deadlines, schedules, unfinished work, and daily constraints. Using an open-weight model gives this project a path toward local inference instead of requiring every prompt to be sent to a proprietary AI service.

Open models also make experimentation easier. I can inspect the application, change the prompt, swap the model, or eventually run the whole system offline without redesigning the entire product.

For a small project like this, that flexibility is one of the biggest advantages of open innovation.

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

The application collects the user's inputs and constructs a structured prompt containing the goal, tasks, available time, session length, and constraints.

The model is instructed to prioritize realistically, avoid inventing commitments, and provide a fallback option for situations where the user has less energy than expected.

## A sample

For example, the user might enter:

> **Goal:** Prepare for next week's database exam  
> **Tasks:** Revise normalization, practice SQL joins, review indexes, finish assignment  
> **Available time:** 3 hours  
> **Constraint:** Low energy after 8 PM

FriendFocus can turn that into something like:

> **Today's focus:** SQL joins and normalization  
>
> **Priority:**  
> 1. Finish assignment  
> 2. Practice SQL joins  
> 3. Review normalization  
> 4. Review indexes  
>
> **Schedule:**  
> 45 min assignment → 10 min break → 45 min SQL → 10 min break → 45 min normalization → 25 min indexes
>
> **Low-energy fallback:**  
> Review index flashcards for 20 minutes instead of completing another full study block.

The goal is not to generate the perfect timetable.

The goal is to make the next action obvious.

## What I learned

The biggest lesson was that useful AI does not always require a large application.

It would have been easy to add calendars, reminders, analytics, streaks, accounts, notifications, and dozens of other features. But that would have moved away from the actual problem.

The core problem was decision overload.

So I optimized for one simple outcome:

**turn chaos into the next few steps.**

## Why building for one person changed the design

Starting with a specific person rather than a generic audience changed how I thought about the project.

Instead of asking, “What features should a productivity app have?”, I asked, “What would make this person's day a little easier?”

That led to a much smaller and more focused product.

## What I would build next

The next version could add calendar integration, recurring preferences, and a model selector that lets users choose an open model based on their hardware.

I would also like to build a fully offline desktop version where the model and planning data remain on the user's computer.

That would make the privacy advantage of open-source AI even more meaningful.

## Try it

**Demo:** [PASTE YOUR DEMO VIDEO OR DEPLOYED LINK]

**Code:** [PASTE YOUR GITHUB REPOSITORY LINK]

## Built for a friend

This project started from a simple idea: sometimes the most useful AI tool is not the one with the most features. It is the one that helps one person take the next step.

That is what I wanted FriendFocus AI to do.

---

Built for Hacktoberfest 2026's **#hf26challenge** / **#weekendchallenge**.

#devchallenge #weekendchallenge #hf26challenge
