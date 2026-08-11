# GravityRealEstate 🏡🤖

An AI-powered rental property and real estate discovery web application built with the **Google Agent Development Kit (ADK)**, **Gemini 3.6 Flash**, **Vertex AI Memory Bank**, and **FastAPI**.

[![GitHub Repository](https://img.shields.io/badge/GitHub-GravityRealEstate-blue?logo=github)](https://github.com/silpa-das-analytics/buildwithgemini-gravity-real-estate)
[![Framework](https://img.shields.io/badge/Framework-Google%20ADK-red)](https://adk.dev/)
[![Deployment](https://img.shields.io/badge/Deployment-Vertex%20AI%20Agent%20Runtime-green)](https://cloud.google.com/vertex-ai)

---

## 📖 Overview

**GravityRealEstate** simplifies rental search by replacing complex filters with a conversational, location-aware AI Assistant. It remembers user budget preferences across sessions using Vertex AI Memory Bank, calculates exact workplace commute times, breaks down itemized monthly housing expenses, and dynamically renders visual property cards with direct clickable links.

---

## ✨ Features

- 📍 **Location-Customized Search**: Tailors all follow-up questions, amenity suggestions, and neighborhood details around the user's requested city.
- 🧠 **Vertex AI Memory Bank**: Persists user preferences (max budget, required bedrooms, commute destinations) across sessions.
- 🖼️ **Visual Property Cards & Thumbnail Previews**: Renders high-resolution rental photography and clickable listing links directly inside the chat drawer.
- 🚗 **Commute & Expense Tools**: Includes custom function tools for transit/drive time estimation (`calculate_commute`) and total housing cost calculations (`calculate_monthly_cost`).
- 🎨 **Redfin-Inspired Modern UI**: Dynamic property cards grid, hero search bar with Enter key submit support, quick filter pills, and slide-out AI Assistant drawer.

---

## 🛠️ Project Structure

```
gravity-real-estate/
├── app/                        # Core agent logic
│   ├── agent.py                # Tools (search_listings, calculate_commute, calculate_monthly_cost) & instruction
│   ├── fast_api_app.py         # ADK FastAPI App runner
│   └── app_utils/
│       └── services.py         # Vertex AI Memory Bank Service registration
├── frontend/                   # Web Application
│   ├── main.py                 # FastAPI A2A Proxy server
│   └── static/
│       ├── index.html          # Redfin-inspired UI with A2UI Card renderer & Markdown parser
│       ├── apartment_hero.jpg   # High-resolution property photography
│       └── apartment_interior.jpg
├── agents-cli-manifest.yaml    # Deployment manifest
├── pyproject.toml              # Project dependencies & package config
└── README.md
```

---

## 🚀 Local Quickstart

### 1. Install Dependencies
```bash
uv sync
```

### 2. Run the Web Application
```bash
export AGENT_ENGINE_RESOURCE_NAME="projects/496623271873/locations/us-east1/reasoningEngines/254682077365010432"
export AGENT_DIRECTORY="app"
export PORT=8086

cd frontend
uv run python main.py
```
Open **`http://localhost:8086`** in your web browser.

---

## ☁️ Deployment

Deploy the agent to **Vertex AI Agent Runtime** using `agents-cli`:

```bash
agents-cli deploy --no-confirm-project
```

---

## 🔗 Public Repository

Published on GitHub:
👉 **[github.com/silpa-das-analytics/buildwithgemini-gravity-real-estate](https://github.com/silpa-das-analytics/buildwithgemini-gravity-real-estate)**
