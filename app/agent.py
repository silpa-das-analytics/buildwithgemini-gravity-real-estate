# ruff: noqa
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
from zoneinfo import ZoneInfo

from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.apps import App
from google.adk.models import Gemini
from google.adk.tools.preload_memory_tool import PreloadMemoryTool
from google.genai import types


MODEL = "gemini-3.6-flash"


async def generate_memories_callback(callback_context: CallbackContext):
    """WRITE: After each turn, send the session to Memory Bank for extraction."""
    await callback_context.add_session_to_memory()
    return None


def search_listings(location: str, bedrooms: int, max_rent: int = 0, features: str = "") -> str:
    """Searches available rental property listings based on location, bedrooms, max rent, and features.

    Args:
        location: The city, neighborhood, or ZIP code to search in (e.g. '95136', 'Downtown Seattle', 'San Francisco', 'New York').
        bedrooms: The required number of bedrooms (must be specified).
        max_rent: Optional maximum monthly budget in USD.
        features: Optional comma-separated list of desired features/amenities (e.g. 'pet friendly, in-unit laundry, balcony').

    Returns:
        A structured string with matching property listings, including thumbnail images and individual listing URLs.
    """
    if not location or location.strip().lower() in ["apartment", "rent", "search"]:
        return "ERROR: Location is required. Please specify a location, city, or ZIP code."
    if bedrooms <= 0:
        return "ERROR: Number of bedrooms is required. Please specify how many bedrooms you need."

    feat_str = f" with features ({features})" if features else ""
    budget_str = f" under ${max_rent}/mo" if max_rent > 0 else ""
    loc_clean = location.strip()
    loc_lower = loc_clean.lower()

    if "95136" in loc_lower or "san jose" in loc_lower:
        return (
            f"Found 2 matching {bedrooms}-bedroom listing(s) in ZIP {loc_clean} (San Jose, CA):\n\n"
            f"### 1. 🏢 Almaden Valley Residence\n"
            f"![Almaden Valley Residence Preview](/apartment_hero.jpg)\n"
            f"- **Details:** {bedrooms} Bed / 2 Bath | Rent: $2,950/mo | Location: San Jose, CA 95136\n"
            f"- **Amenities:** Swimming Pool, In-Unit Laundry, Covered Parking, Pet Friendly\n"
            f"- 🔗 [View Apartment Details](http://localhost:8086/listing.html?id=pinnacle-heights)\n\n"
            f"### 2. 🌿 Silicon Valley Tech Loft\n"
            f"![Silicon Valley Tech Loft Preview](/apartment_interior.jpg)\n"
            f"- **Details:** {bedrooms} Bed / 1 Bath | Rent: $2,650/mo | Location: San Jose, CA 95136\n"
            f"- **Amenities:** High-Speed Fiber, EV Charging, Balcony, Fitness Center\n"
            f"- 🔗 [View Apartment Details](http://localhost:8086/listing.html?id=urban-oak)\n"
        )
    elif "san francisco" in loc_lower or "sf" in loc_lower or "sfo" in loc_lower or "941" in loc_lower:
        return (
            f"Found 2 matching {bedrooms}-bedroom listing(s) in {loc_clean}{budget_str}{feat_str}:\n\n"
            f"### 1. 🏢 Pacific Bay Highrise\n"
            f"![Pacific Bay Highrise Preview](/apartment_hero.jpg)\n"
            f"- **Details:** {bedrooms} Bed / 2 Bath | Rent: $3,400/mo | Location: SoMa, San Francisco, CA\n"
            f"- **Amenities:** Skyline Views, Heated Pool, Smart Home Tech, Concierge, Pet Spa\n"
            f"- 🔗 [View Apartment Details](http://localhost:8086/listing.html?id=pacific-bay)\n\n"
            f"### 2. 🌿 Mission Loft Studios\n"
            f"![Mission Loft Studios Preview](/apartment_interior.jpg)\n"
            f"- **Details:** {bedrooms} Bed / 1 Bath | Rent: $2,850/mo | Location: Mission District, San Francisco, CA\n"
            f"- **Amenities:** Exposed Brick, High Ceilings, Gas Stove, Washer/Dryer, Courtyard\n"
            f"- 🔗 [View Apartment Details](http://localhost:8086/listing.html?id=mission-loft)\n"
        )
    elif "new york" in loc_lower or "ny" in loc_lower or "nyc" in loc_lower or "100" in loc_lower:
        return (
            f"Found 2 matching {bedrooms}-bedroom listing(s) in {loc_clean}{budget_str}{feat_str}:\n\n"
            f"### 1. 🏢 Manhattan Sky Suites\n"
            f"![Manhattan Sky Suites Preview](/apartment_hero.jpg)\n"
            f"- **Details:** {bedrooms} Bed / 2 Bath | Rent: $3,800/mo | Location: Midtown, New York, NY\n"
            f"- **Amenities:** Doorman 24/7, Central Park View, Fitness Club, Wine Storage\n"
            f"- 🔗 [View Apartment Details](http://localhost:8086/listing.html?id=manhattan-sky)\n\n"
            f"### 2. 🌿 Brooklyn Brick Loft\n"
            f"![Brooklyn Brick Loft Preview](/apartment_interior.jpg)\n"
            f"- **Details:** {bedrooms} Bed / 1 Bath | Rent: $3,100/mo | Location: Williamsburg, New York, NY\n"
            f"- **Amenities:** Private Balcony, Rooftop Grill, Dishwasher, Pet Friendly\n"
            f"- 🔗 [View Apartment Details](http://localhost:8086/listing.html?id=brooklyn-brick)\n"
        )
    else:
        return (
            f"Found 2 matching {bedrooms}-bedroom listing(s) in {loc_clean}{budget_str}{feat_str}:\n\n"
            f"### 1. 🏢 {loc_clean} Grand Plaza Apartments\n"
            f"![Grand Plaza Preview](/apartment_hero.jpg)\n"
            f"- **Details:** {bedrooms} Bed / 2 Bath | Rent: $2,450/mo | Location: {loc_clean}\n"
            f"- **Amenities:** Pet Friendly, In-Unit Laundry, Fitness Center, Garage Parking\n"
            f"- 🔗 [View Apartment Details](http://localhost:8086/listing.html?id=pinnacle-heights)\n\n"
            f"### 2. 🌿 {loc_clean} Terrace Residence\n"
            f"![Terrace Residence Preview](/apartment_interior.jpg)\n"
            f"- **Details:** {bedrooms} Bed / 1.5 Bath | Rent: $2,150/mo | Location: {loc_clean}\n"
            f"- **Amenities:** Balcony, Washer/Dryer, Pet Friendly, Storage Unit\n"
            f"- 🔗 [View Apartment Details](http://localhost:8086/listing.html?id=urban-oak)\n"
        )


def calculate_commute(property_address: str, work_address: str) -> str:
    """Calculates estimated commute time between a rental property and a work location.

    Args:
        property_address: The rental property address or neighborhood.
        work_address: The work address or destination.

    Returns:
        A string with estimated transit and drive times.
    """
    return (
        f"Commute estimate from '{property_address}' to '{work_address}':\n"
        f"- 🚗 By car: ~18-25 mins (light/moderate traffic)\n"
        f"- 🚆 By transit: ~30 mins (direct line)\n"
        f"- 🔗 [View Map on Home Page](http://localhost:8086/)"
    )


def calculate_monthly_cost(rent: int, utilities: int = 150, parking: int = 100) -> str:
    """Calculates the total estimated monthly housing cost including rent, utilities, and parking.

    Args:
        rent: Base monthly rent amount in USD.
        utilities: Estimated monthly utility cost (electricity, water, internet). Default $150.
        parking: Monthly parking fee if applicable. Default $100.

    Returns:
        A breakdown of total estimated monthly expenses.
    """
    total = rent + utilities + parking
    return (
        f"Monthly Housing Cost Breakdown:\n"
        f"- Base Rent: ${rent}\n"
        f"- Estimated Utilities: ${utilities}\n"
        f"- Parking Fee: ${parking}\n"
        f"-----------------------------\n"
        f"Total Estimated Monthly Cost: ${total}\n"
        f"- 🔗 [View Financial Calculator on Home Page](http://localhost:8086/)"
    )


root_agent = Agent(
    name="root_agent",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=(
        "You are an expert Real Estate & Apartment Finder AI Assistant for GravityRealEstate.\n"
        "Your mission is to help users find, compare, and evaluate rental properties.\n"
        "You remember the user's stated preferences, location, budget, and facts across turns and memory to personalize every response.\n\n"
        "CRITICAL RULES:\n"
        "1. ALWAYS verify that the user has provided a SPECIFIC LOCATION/CITY. If not, ask the user to specify their location FIRST.\n"
        "2. ONCE THE USER PROVIDES A LOCATION, CUSTOMIZE EVERY SUBSEQUENT QUESTION AND RESPONSE SPECIFICALLY AROUND THAT LOCATION.\n"
        "3. ALWAYS ensure the user specifies HOW MANY BEDROOMS they need. If they haven't specified the number of bedrooms, ASK them before calling search_listings.\n"
        "4. REQUIRED FOR EVERY RESPONSE WITH PROPERTY SUGGESTIONS OR CALCULATIONS: You MUST include clickable markdown links like `[View Home Page Listing](http://localhost:8086/)` and image thumbnails like `![Preview](/apartment_hero.jpg)` as provided by the tools. NEVER omit or remove the links or images from your output.\n"
        "5. Use the provided tools (search_listings, calculate_commute, calculate_monthly_cost) to answer user requests once required details (location & bedrooms) are known."
    ),
    tools=[PreloadMemoryTool(), search_listings, calculate_commute, calculate_monthly_cost],
    after_agent_callback=generate_memories_callback,
)

app = App(
    root_agent=root_agent,
    name="app",
)
