# 🛠️ Data Project Bootstrapper

A Python script that **automatically sets up your data science project** by cloning a GitHub repo, scaffolding the folder structure, initializing a virtual environment, installing standard packages, and committing the setup back to GitHub — all in one go!

Perfect for data analysts, data scientists, and developers who want a consistent, automated setup across all their projects.

---

## 🚀 Features

- ✅ Clone any GitHub repo (public or private with access)
- ✅ Create a structured project layout:
  - `data/` – raw or processed datasets
  - `notebooks/` – Jupyter notebooks
  - `visuals/` – charts and plots
  - `outputs/` – models, predictions, reports
- ✅ Generate `README.md` and `requirements.txt`
- ✅ Set up a Python virtual environment
- ✅ Install essential packages:
  - `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `jupyter`
- ✅ Save environment dependencies to `requirements.txt`
- ✅ Auto-commit and push initial project structure

---

## 📁 Folder Structure

```
project-name/
│
├— data/          # For raw and processed data
├— notebooks/     # Jupyter notebooks (EDA, modeling, etc.)
├— visuals/       # Data visualizations and plots
├— outputs/       # Exported results, models, etc.
├— README.md      # Project overview
├— requirements.txt
└— venv/          # Python virtual environment
```

---

## 🧑‍💻 How to Use

### 1⃣ Requirements

- Python 3.10+
- Git installed and accessible from the terminal
- Internet access to install packages and clone repos

---

### 2⃣ Clone This Script (or Copy to Your System)

Place the script `setup_data_project.py` in any directory where you organize your data science projects.

---

### 3⃣ Run It (Two Modes)

#### 🔸 Option A: Use Current Script Directory as Project Root

```bash
python setup_data_project.py https://github.com/your-username/your-repo.git
```

The new project folder will be created inside the same directory where the script is located.

---

#### 🔸 Option B: Use a Custom Path

```bash
python setup_data_project.py https://github.com/your-username/your-repo.git "C:\Users\yourname\Documents\Data Projects"
```

The project will be created in the custom path provided.

---

## ✨ Example

```bash
python setup_data_project.py https://github.com/jbgabreal/loan-default-prediction.git
```

---

## 💡 Tips

- You can reuse this script for every new data science project.
- Store it in a central location or add it to your PATH for global use.
- Extend it to include more tools like `black`, `pre-commit`, `pytest`, `MLflow`, or `Docker`.

---

## 🔧 Customization Ideas

- Add conda support
- Auto-create `.gitignore` and `.env` templates
- Configure VS Code settings and Jupyter kernel
- Install extra packages like `xgboost`, `lightgbm`, or `plotly`

---

## 🤝 Contributing

Feel free to fork this repo and suggest improvements, or submit a pull request!

---

## 📄 License

MIT License – do whatever you want, but attribution is appreciated!

---

## 🙌 Acknowledgements

Inspired by real-world frustration with repeating project setups. Automate once, use forever!

