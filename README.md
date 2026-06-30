# 📖 AI Dungeon Story Generator

An AI-powered Story Generator built using **Python**, **Streamlit**, and **Hugging Face Transformers**. This application generates creative stories based on user prompts using pretrained language models such as **GPT-2** or **GPT-Neo**.

The project provides an interactive web interface where users can choose different genres, control story creativity and length, generate multiple story continuations, save stories locally, and download them as text files.

---

## ✨ Features

- 🤖 AI-powered story generation using GPT-2 / GPT-Neo
- 📝 Prompt-based story generation
- 📚 Multiple genres
  - Fantasy
  - Adventure
  - Mystery
  - Horror
  - Sci-Fi
  - Romance
- 📖 Generate up to 3 story continuations
- 📏 Story Length Selection
  - Short
  - Medium
  - Long
- 🎨 Creativity Level Slider
- 💾 Save generated stories to a local folder
- 📥 Download stories as a `.txt` file
- 🎈 Interactive Streamlit web interface
- 🎨 Modern and responsive UI
- ⚡ Fast loading using Streamlit cache

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- GPT-2 / GPT-Neo
- PyTorch

---

## 📂 Project Structure

```
AI_Dungeon_Story_Generator/
│
├── app.py                 # Main Streamlit application
├── story_generator.py     # AI model loading and story generation
├── utils.py               # Save story utility
├── requirements.txt
├── README.md
├── .gitignore
│
└── stories/               # Saved stories
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI_Dungeon_Story_Generator.git
```

### 2. Navigate to the project

```bash
cd AI_Dungeon_Story_Generator
```

### 3. Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

## 📖 How to Use

1. Select your preferred genre.
2. Choose the number of stories.
3. Select the story length.
4. Adjust the creativity level.
5. Enter your story prompt.
6. Click **Generate AI Story**.
7. Read the generated stories.
8. Save stories to the **stories** folder.
9. Download stories as a text file if required.

---

## ⚙️ Model Information

This project supports pretrained transformer models from Hugging Face.

Examples:

- GPT-2
- GPT-2 Medium
- GPT-Neo 125M

Model loading is handled inside **story_generator.py**.

---

## ⚠️ Limitations

The quality of generated stories depends on the selected language model.

Smaller models such as GPT-2 and GPT-Neo 125M may occasionally:
- Generate repetitive text
- Produce incomplete endings
- Drift away from the original prompt

Larger models generally produce higher-quality stories but require more computational resources.

---

## 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

- Generative AI
- Transformer Models
- Hugging Face Transformers
- Prompt Engineering
- Streamlit Development
- Python Programming
- AI Model Integration
- Interactive Web Application Development

---

## 👨‍💻 Author

**Krupa Manani**


---

## 📄 License

This project is intended for educational and learning purposes.