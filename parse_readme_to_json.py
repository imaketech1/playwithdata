import json

def parse_readme_to_json(readme_path):
    with open(readme_path, 'r') as file:
        lines = file.readlines()

    data = []
    current_question = None
    collecting_answer = False
    current_answer = []

    for line in lines:
        stripped = line.strip()

        if stripped.startswith('#####'):
            if current_question and current_answer:
                data.append({
                    "question": current_question,
                    "answer": "\n".join(current_answer).strip()
                })
                current_answer = []

            current_question = stripped.replace('#####', '').strip()
            collecting_answer = False

        elif stripped.startswith("```"):
            if not collecting_answer:
                collecting_answer = True
                current_answer = []
            else:
                collecting_answer = False
        elif collecting_answer:
            current_answer.append(line.rstrip())

    if current_question and current_answer:
        data.append({
            "question": current_question,
            "answer": "\n".join(current_answer).strip()
        })

    return data

qa_data = parse_readme_to_json("gitcheats.md")

with open("git_qa.json", "w") as outfile:
    json.dump(qa_data, outfile, indent=2)

print("Extracted", len(qa_data), "Q&A pairs.")
