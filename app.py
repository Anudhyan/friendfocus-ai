import gradio as gr
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_ID = "Qwen/Qwen2.5-0.5B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float32,
)
model.eval()

SYSTEM_PROMPT = """You are FriendFocus, a practical planning assistant.
Your job is to turn a person's messy goals and obligations into a realistic plan.
Be encouraging but not overly cheerful. Do not invent appointments or commitments.
Prefer small, achievable actions and visible priorities.
Return:
1. TODAY'S FOCUS
2. PRIORITY ORDER
3. SCHEDULE
4. LOW-ENERGY FALLBACK
5. ONE MESSAGE TO THE FRIEND
Keep it concise and actionable.
"""

def build_plan(friend_name, goal, tasks, hours, session_length, constraints):
    friend_name = friend_name.strip() or "my friend"
    goal = goal.strip()
    tasks = tasks.strip()
    constraints = constraints.strip() or "No extra constraints."

    if not goal or not tasks:
        return "Please enter the main goal and at least one task."

    user_prompt = f"""Plan for {friend_name}.

Main goal:
{goal}

Tasks / obligations:
{tasks}

Available focused time today:
{hours} hours

Preferred focus-session length:
{session_length} minutes

Constraints:
{constraints}
"""

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )
    inputs = tokenizer(text, return_tensors="pt")

    with torch.inference_mode():
        output = model.generate(
            **inputs,
            max_new_tokens=450,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.05,
        )

    generated = output[0][inputs["input_ids"].shape[1]:]
    return tokenizer.decode(generated, skip_special_tokens=True).strip()

with gr.Blocks(title="FriendFocus AI") as demo:
    gr.Markdown(
        """
        # FriendFocus AI
        ### A private planning buddy built for a friend

        Turn a messy list of obligations into a realistic plan without sending
        the friend's personal details to a closed AI API.
        """
    )

    with gr.Row():
        with gr.Column():
            friend_name = gr.Textbox(
                label="Friend's first name",
                placeholder="e.g. Alex",
            )
            goal = gr.Textbox(
                label="Main goal",
                placeholder="e.g. Prepare for next week's database exam",
                lines=2,
            )
            tasks = gr.Textbox(
                label="Tasks / obligations",
                placeholder="One task per line",
                lines=7,
            )
        with gr.Column():
            hours = gr.Slider(
                minimum=0.5,
                maximum=12,
                value=3,
                step=0.5,
                label="Available focused time today (hours)",
            )
            session_length = gr.Slider(
                minimum=15,
                maximum=120,
                value=45,
                step=15,
                label="Preferred focus-session length (minutes)",
            )
            constraints = gr.Textbox(
                label="Constraints",
                placeholder="e.g. Class 2–4 PM, low energy after 8 PM",
                lines=4,
            )

    run = gr.Button("Build my plan")
    output = gr.Markdown(label="Plan")

    run.click(
        fn=build_plan,
        inputs=[friend_name, goal, tasks, hours, session_length, constraints],
        outputs=output,
    )

    gr.Markdown(
        """
        ---
        **Open AI core:** Qwen2.5-0.5B-Instruct (Apache-2.0), running in this app
        through the open-source Hugging Face Transformers stack.

        **Privacy note:** This app is designed so the planning prompt goes to the
        model running with the app, rather than a proprietary chatbot API.
        """
    )

if __name__ == "__main__":
    demo.launch()
