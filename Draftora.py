import tkinter as tk
from tkinter import scrolledtext
import wikipedia
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# -------- Wikipedia Fetch -------- #
def get_wikipedia_content(query):
    try:
        page = wikipedia.page(query)
        return page.title, page.summary, page.url
    except:
        return None, "No data found", None

# -------- Generate Answer -------- #
def generate_answer():
    question = entry.get()
    
    title, content, url = get_wikipedia_content(question)
    
    if content == "No data found":
        output.delete(1.0, tk.END)
        output.insert(tk.END, "❌ No data found. Try another topic.")
        return
    
    final_text = f"""
📘 Topic: {title}

🧠 Answer:
{content}

🔗 Reference:
{url}

⚠️ Note: This answer is generated using Wikipedia for educational purposes.
"""
    
    output.delete(1.0, tk.END)
    output.insert(tk.END, final_text)

# -------- Save PDF -------- #
def save_pdf():
    text = output.get(1.0, tk.END)
    
    doc = SimpleDocTemplate("assignment.pdf")
    styles = getSampleStyleSheet()
    
    story = []
    story.append(Paragraph(text, styles["Normal"]))
    
    doc.build(story)

# -------- UI -------- #
root = tk.Tk()
root.title("AI Assignment Assistant")
root.geometry("700x500")

title_label = tk.Label(root, text="AI Assignment Assistant", font=("Arial", 16))
title_label.pack(pady=10)

entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=10)

generate_btn = tk.Button(root, text="Generate Answer", command=generate_answer)
generate_btn.pack(pady=5)

save_btn = tk.Button(root, text="Save as PDF", command=save_pdf)
save_btn.pack(pady=5)

output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
output.pack(pady=10)

root.mainloop()
