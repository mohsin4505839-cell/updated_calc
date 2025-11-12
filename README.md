<!-- PROJECT LOGO -->
<p align="center">
  <img src="https://img.icons8.com/external-flat-icons-inmotus-design/67/external-carbon-footprint-ecology-flat-icons-inmotus-design.png" width="80" alt="logo" />
</p>

<h1 align="center">🌍 NED University Carbon Footprint Calculator</h1>

<p align="center">
  <b>A full-featured Streamlit web app to calculate, visualize, and export NED University’s institutional & individual CO₂e emissions.</b>  
  <br />
  Built using clean Python + Pandas + Streamlit • PakWheels verified dataset  
  <br /><br />
  <a href="#-features">Features</a> •
  <a href="#-installation--usage">Installation</a> •
  <a href="#-data--calculation-methods">Calculations</a> •
  <a href="#-author">Author</a>
  <br /><br />
  <img src="https://img.shields.io/badge/Framework-Streamlit-%23FF4B4B?logo=streamlit" />
  <img src="https://img.shields.io/badge/Language-Python_3.12-blue?logo=python" />
  <img src="https://img.shields.io/badge/Status-Full%20Feature%20Port-success?style=flat-square" />
</p>

---

## 🚀 Features

### 🏛️ Institutional Emissions
- Calculates total **employee commuting** and **bus fleet** CO₂e
- Adjustable assumptions: commute distance, traffic factor, operating days
- **PakWheels-verified** emission factors
- Export **executive summary (TXT)** + **vehicle breakdown (CSV)**

### 🚗 Individual Calculator
- Multi-entry per-user vehicle emissions  
- Auto-semester academic weeks for students  
- Add or remove vehicles dynamically  
- Instant results with **trees & equivalent cars** estimations  
- Download TXT or CSV summaries  

### 🔄 Combined Report
- Merge institutional and personal results  
- One-click combined report generator  

### 📊 Vehicle Database
- Full dataset of 20+ vehicles (cars, bikes, hybrid, EV, diesel SUV)  
- Technical specs, efficiency, emission factors  
- CSV export + expandable detail viewer  

---

## 🧱 Project Structure
```bash
updated_calc/
├── streamlit_app.py       # main Streamlit web app
└── requirements.txt       # dependencies
