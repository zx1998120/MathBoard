# 🧠 MathBoard: Symbolic Computation and Multi-objective Optimization Platform

MathBoard is a lightweight full-stack application that allows users to perform symbolic mathematics and multi-objective optimization through a web interface. It provides RESTful APIs powered by Python (FastAPI) on the backend and an interactive frontend built with React.

---

## Features

### Symbolic Computation (Powered by SymPy)
- Simplify algebraic expressions
- Differentiate with respect to a given variable
- Perform indefinite integration
- Generate Taylor series expansions

### Multi-objective Optimization (Powered by Platypus/NSGA-II)
- Solve synthetic ZDT-like problems with user-defined bounds
- Configure population size, variable count, and generations
- Visualize Pareto front in real time

---

## Tech Stack

### Backend
- FastAPI
- SymPy (symbolic math)
- Platypus (NSGA-II optimization)
- SciPy

### Frontend
- React
- Axios (API communication)
- Plotly.js (data visualization)
- React-KaTeX (math rendering)

---

## Getting Started

### 1. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install fastapi uvicorn sympy platypus-opt
uvicorn main:app --reload --port 8000
```

### 2. Frontend Setup
```bash
cd frontend
npm install
npm install axios react-plotly.js plotly.js react-katex katex
npm start
```

### App will run at:
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:8000`

---

## Example Use Cases

### 1. Symbolic Computation
Input: `x^2 + sin(x)` with operation `diff`
Output: `2x + cos(x)` (displayed with math formatting)

### 2. Multi-objective Optimization
- Input: 2-variable bounded optimization with 50 population and 100 generations
- Output: Pareto front scatter plot (objective1 vs. objective2)

---

## ScreenShot
<img width="1050" height="787" alt="Screenshot 2025-07-25 at 15 35 39" src="https://github.com/user-attachments/assets/e98c3968-1af7-4424-b325-a42c368359d8" />


---

## 📜 License
This project is released under the MIT License.
