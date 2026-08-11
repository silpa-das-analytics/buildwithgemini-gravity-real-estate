# Project Brief: GravityRealEstate

## Executive Summary
**GravityRealEstate** is an AI-powered rental property and real estate discovery web platform built using the Google Agent Development Kit (ADK), Gemini 3.6 Flash, Vertex AI Memory Bank, and FastAPI. It combines location-aware AI search, real-time commute calculations, itemized monthly housing cost breakdowns, and persistent cross-session user memory in a modern Redfin-style web interface.

---

## 🌟 Core Features & Capabilities

1. **Location-Customized AI Assistant**
   - Dynamically adapts all follow-up questions, amenity suggestions, and neighborhood recommendations specifically around the user's target city (e.g., Seattle, San Francisco, New York).
   - Enforces bedroom count, budget parameters, and feature preferences before executing searches.

2. **Vertex AI Memory Bank Integration**
   - Powered by a managed Vertex AI Memory Bank instance (`753596473584648192` in `us-east1`).
   - Automatically retains user budget constraints, workplace commute destinations, and pet/amenity preferences across multiple turns and sessions.

3. **Visual Property Cards & Interactive Links**
   - Automatically renders preview thumbnail photography (`/apartment_hero.jpg`, `/apartment_interior.jpg`) and direct clickable listing links (`🔗 View Property on Home Page`) inside chat drawer bubbles.

4. **Commute & Financial Tools**
   - `search_listings`: Queries verified property databases filtered by location, bedrooms, max rent, and amenities.
   - `calculate_commute`: Estimates driving and public transit times between rental properties and target work addresses.
   - `calculate_monthly_cost`: Calculates total estimated monthly expenses including base rent, utilities, and parking fees.

5. **Redfin-Inspired Modern Web UI**
   - Clean navigation header, hero search bar with Enter key submit support, interactive quick filter pills, dynamic property grid updates, and a slide-out AI Assistant drawer with built-in A2UI card renderer.

---

## 🏗️ Technical Architecture

- **Agent Framework:** Google ADK (Agent Development Kit) & Gemini 3.6 Flash (`MODEL = "gemini-3.6-flash"`).
- **Long-Term Memory:** Vertex AI Memory Bank (`VertexAiMemoryBankService` with `PreloadMemoryTool` & `generate_memories_callback`).
- **Protocol:** Agent-to-Agent (A2A) protocol over HTTP passthrough.
- **Frontend Proxy:** FastAPI proxy server (`frontend/main.py`) forwarding browser requests authenticated via Application Default Credentials (ADC).
- **Deployment Target:** Vertex AI Agent Runtime (`projects/496623271873/locations/us-east1/reasoningEngines/254682077365010432`).
- **GitHub Repository:** `https://github.com/silpa-das-analytics/buildwithgemini-gravity-real-estate`

---

## 🚀 Getting Started

### Local Development Server
```bash
# Launch the web application locally on port 8086
cd frontend
AGENT_ENGINE_RESOURCE_NAME="projects/496623271873/locations/us-east1/reasoningEngines/254682077365010432" AGENT_DIRECTORY="app" PORT=8086 uv run python main.py
```
Open **`http://localhost:8086`** in your browser.

### Agent Deployment
```bash
# Deploy updated agent code to Vertex AI Agent Runtime
agents-cli deploy --no-confirm-project
```
