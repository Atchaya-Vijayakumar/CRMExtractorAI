import openai
import json

def load_prompt():
    with open("prompts/crm_extraction_prompt.txt", "r", encoding="utf-8") as file:
        return file.read()

def extract_crm_fields(text):
    prompt_template = load_prompt()
    prompt = prompt_template.replace("[PASTE TRANSCRIPT OR EMAIL HERE]", text)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a CRM assistant AI."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2  # Optional: Controls randomness
        )

        # Extract content from the response
        content = response["choices"][0]["message"]["content"]

        # Try parsing the content as JSON
        return json.loads(content)

    except json.JSONDecodeError:
        return {"error": "❌ Could not parse response as JSON."}
    except Exception as e:
        return {"error": f"❌ OpenAI API Error:," }
