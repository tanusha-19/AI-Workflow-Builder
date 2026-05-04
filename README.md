# Smart Workflow Builder

An AI-powered logic architect that transforms text into professional, stylized workflow diagrams instantly.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

---

## ✨ Features
*   📂 **Instant Visualization** — Type your logic and see a real-time flowchart update.
*   🧠 **Smart Categorization** — Automatically assigns shapes (Diamonds for logic, Rounded for data).
*   🎨 **Premium Dark UI** — Sleek Glassmorphism design with a modern SaaS aesthetic.
*   ↔️ **Dual Orientation** — Switch between Horizontal and Vertical layouts.

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend** | **Streamlit** | Turning Python scripts into an interactive web interface. |
| **Styling** | **CSS3 / HTML5** | Custom Glassmorphism UI and SaaS aesthetic. |
| **Core Logic** | **Python 3** | String parsing and automated shape categorization. |
| **Visualization** | **Mermaid.js** | JavaScript-based diagramming and charting tool. |

---

## 📁 Project Structure

AI-Workflow-Builder/
├── app.py              # Main application logic & Streamlit entry point.
├── style.py            # Modular CSS definitions for the Professional UI.
├── requirements.txt    # List of external libraries required for execution.
├── .gitignore          # Rules for Git to ignore sensitive/cache files.
├── README.md           # Technical documentation and project overview.
└── workflow_log.txt    # Local storage for generated workflow history.
---

## 🚀 Getting Started

### Prerequisites

* **Python** v3.9 or higher
* **Streamlit** for the web interface

### Installation

```bash
# 1. Clone the repository
git clone [https://github.com/tanusha-19/AI-Workflow-Builder.git](https://github.com/tanusha-19/AI-Workflow-Builder.git)
cd AI-Workflow-Builder

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up your environment variables
# Create a .env file in the root directory
 ```

## Run
```# Start the Streamlit server
streamlit run app.py
```
---

## 🔒 Security & Best Practices

*   **Environment Isolation**: Uses a `.gitignore` file to ensure that local configuration files (like `.env`) are never pushed to the public repository.
*   **Input Sanitization**: The logic cleans and formats user text (replacing `/` with `<br/>`) to prevent diagram breakage.
*   **Modular Architecture**: By separating the CSS (`style.py`) from the logic (`app.py`), the project follows the **Single Responsibility Principle (SRP)**.
*   **Local Logic Fallback**: The system is designed to work locally without requiring heavy cloud dependencies, ensuring data privacy for the user's logic.

---

**Tanusha Sahu**  
