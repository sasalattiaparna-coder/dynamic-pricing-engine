# Dynamic Pricing Engine

## Overview
AI-based pricing system that adjusts product prices dynamically using demand, inventory, competitor pricing, and seasonal factors.

## Features
- Machine Learning (XGBoost)
- Real-time pricing API (FastAPI)
- Interactive dashboard (Streamlit)
- Competitor price simulation

## How to Run

### Step 1: Install dependencies
pip install -r requirements.txt

### Step 2: Train model
python model.py

### Step 3: Run dashboard
streamlit run app.py

### Step 4: Run API
uvicorn api:app --reload
