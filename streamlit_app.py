# streamlit_app.py — Full Feature Port of Cleaned v2 (CLI → Web)
# ---------------------------------------------------------------------------------
# COMPLETE parity with your cleaned CLI version, modern Streamlit UI.

import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="NED Carbon Footprint Calculator",
    page_icon="🌍",
    layout="wide",
)

# ============================== Data & Config =============================== #

VEHICLE_DATABASE = {
    # Motorcycles (4 models)
    "honda_cd70": {
        "category": "motorcycle",
        "name": "Honda CD 70",
        "engine_cc": 72,
        "fuel_type": "petrol",
        "fuel_efficiency_kmpl": 60,
        "emission_factor": 0.085,
        "manufacturer": "Honda",
        "verification": "PakWheels Verified: 72cc engine with 60 km/l efficiency",
        "specifications": {
            "engine": "72cc, 4-stroke, air-cooled",
            "fuel_tank": "8.5 liters",
            "power": "6.0 hp @ 8000 RPM",
            "torque": "7.5 Nm @ 5000 RPM",
            "weight": "82 kg"
        }
    },
    "honda_cg125": {
        "category": "motorcycle",
        "name": "Honda CG 125",
        "engine_cc": 124,
        "fuel_type": "petrol",
        "fuel_efficiency_kmpl": 50,
        "emission_factor": 0.105,
        "manufacturer": "Honda",
        "verification": "PakWheels Verified: 124cc engine with 50 km/l efficiency",
        "specifications": {
            "engine": "124cc, 4-stroke, air-cooled",
            "fuel_tank": "10.5 liters",
            "power": "11 hp @ 9000 RPM",
            "torque": "9.8 Nm @ 7000 RPM",
            "weight": "108 kg"
        }
    },
    "yamaha_ybr125": {
        "category": "motorcycle",
        "name": "Yamaha YBR 125",
        "engine_cc": 124,
        "fuel_type": "petrol",
        "fuel_efficiency_kmpl": 55,
        "emission_factor": 0.105,
        "manufacturer": "Yamaha",
        "verification": "PakWheels Verified: 124cc engine with 55 km/l efficiency",
        "specifications": {
            "engine": "124cc, 4-stroke, air-cooled",
            "fuel_tank": "13 liters",
            "power": "9.5 hp @ 8000 RPM",
            "torque": "9.6 Nm @ 6500 RPM",
            "weight": "112 kg"
        }
    },
    "suzuki_gs150": {
        "category": "motorcycle",
        "name": "Suzuki GS 150",
        "engine_cc": 147,
        "fuel_type": "petrol",
        "fuel_efficiency_kmpl": 45,
        "emission_factor": 0.125,
        "manufacturer": "Suzuki",
        "verification": "PakWheels Verified: 147cc engine with 45 km/l efficiency",
        "specifications": {
            "engine": "147cc, 4-stroke, air-cooled",
            "fuel_tank": "11 liters",
            "power": "13.5 hp @ 8500 RPM",
            "torque": "13.4 Nm @ 6000 RPM",
            "weight": "135 kg"
        }
    },

    # Cars - Petrol (7 models)
    "suzuki_mehran": {
        "category": "car",
        "name": "Suzuki Mehran",
        "engine_cc": 796,
        "fuel_type": "petrol",
        "fuel_efficiency_kmpl": 18,
        "emission_factor": 0.152,
        "manufacturer": "Suzuki",
        "verification": "PakWheels Verified: 796cc engine with 18 km/l efficiency",
        "specifications": {
            "engine": "796cc, 3-cylinder, petrol",
            "fuel_tank": "30 liters",
            "power": "38 hp @ 5500 RPM",
            "torque": "59 Nm @ 3000 RPM",
            "weight": "645 kg",
            "seating": "4-5 persons"
        }
    },
    "suzuki_alto": {
        "category": "car",
        "name": "Suzuki Alto",
        "engine_cc": 996,
        "fuel_type": "petrol",
        "fuel_efficiency_kmpl": 20,
        "emission_factor": 0.168,
        "manufacturer": "Suzuki",
        "verification": "PakWheels Verified: 996cc engine with 20 km/l efficiency",
        "specifications": {
            "engine": "996cc, 3-cylinder, petrol",
            "fuel_tank": "35 liters",
            "power": "67 hp @ 6000 RPM",
            "torque": "90 Nm @ 3400 RPM",
            "weight": "750 kg",
            "seating": "5 persons"
        }
    },
    "suzuki_cultus": {
        "category": "car",
        "name": "Suzuki Cultus",
        "engine_cc": 998,
        "fuel_type": "petrol",
        "fuel_efficiency_kmpl": 19,
        "emission_factor": 0.168,
        "manufacturer": "Suzuki",
        "verification": "PakWheels Verified: 998cc engine with 19 km/l efficiency",
        "specifications": {
            "engine": "998cc, 3-cylinder, petrol",
            "fuel_tank": "35 liters",
            "power": "67 hp @ 6000 RPM",
            "torque": "90 Nm @ 3500 RPM",
            "weight": "810 kg",
            "seating": "5 persons"
        }
    },
    "toyota_corolla_1.3": {
        "category": "car",
        "name": "Toyota Corolla 1.3L",
        "engine_cc": 1298,
        "fuel_type": "petrol",
        "fuel_efficiency_kmpl": 15,
        "emission_factor": 0.192,
        "manufacturer": "Toyota",
        "verification": "PakWheels Verified: 1298cc engine with 15 km/l efficiency",
        "specifications": {
            "engine": "1298cc, 4-cylinder, petrol",
            "fuel_tank": "55 liters",
            "power": "88 hp @ 6000 RPM",
            "torque": "121 Nm @ 3200 RPM",
            "weight": "1080 kg",
            "seating": "5 persons"
        }
    },
    "honda_civic_1.8": {
        "category": "car",
        "name": "Honda Civic 1.8L",
        "engine_cc": 1799,
        "fuel_type": "petrol",
        "fuel_efficiency_kmpl": 13,
        "emission_factor": 0.238,
        "manufacturer": "Honda",
        "verification": "PakWheels Verified: 1799cc engine with 13 km/l efficiency",
        "specifications": {
            "engine": "1799cc, 4-cylinder, petrol",
            "fuel_tank": "50 liters",
            "power": "140 hp @ 6300 RPM",
            "torque": "174 Nm @ 4300 RPM",
            "weight": "1250 kg",
            "seating": "5 persons"
        }
    },
    "toyota_corolla_1.6": {
        "category": "car",
        "name": "Toyota Corolla 1.6L",
        "engine_cc": 1598,
        "fuel_type": "petrol",
        "fuel_efficiency_kmpl": 14,
        "emission_factor": 0.215,
        "manufacturer": "Toyota",
        "verification": "PakWheels Verified: 1598cc engine with 14 km/l efficiency",
        "specifications": {
            "engine": "1598cc, 4-cylinder, petrol",
            "fuel_tank": "55 liters",
            "power": "130 hp @ 6000 RPM",
            "torque": "157 Nm @ 5200 RPM",
            "weight": "1230 kg",
            "seating": "5 persons"
        }
    },
    "toyota_camry": {
        "category": "car",
        "name": "Toyota Camry 2.0L",
        "engine_cc": 1998,
        "fuel_type": "petrol",
        "fuel_efficiency_kmpl": 12,
        "emission_factor": 0.258,
        "manufacturer": "Toyota",
        "verification": "PakWheels Verified: 1998cc engine with 12 km/l efficiency",
        "specifications": {
            "engine": "1998cc, 4-cylinder, petrol",
            "fuel_tank": "70 liters",
            "power": "178 hp @ 6000 RPM",
            "torque": "233 Nm @ 4100 RPM",
            "weight": "1490 kg",
            "seating": "5 persons"
        }
    },

    # Diesel Vehicles
    "toyota_fortuner": {
        "category": "suv",
        "name": "Toyota Fortuner",
        "engine_cc": 2755,
        "fuel_type": "diesel",
        "fuel_efficiency_kmpl": 10,
        "emission_factor": 0.245,
        "manufacturer": "Toyota",
        "verification": "PakWheels Verified: 2755cc diesel engine with 10 km/l efficiency",
        "specifications": {
            "engine": "2755cc, 4-cylinder turbo diesel",
            "fuel_tank": "80 liters",
            "power": "174 hp @ 3400 RPM",
            "torque": "450 Nm @ 1600-2400 RPM",
            "weight": "2010 kg",
            "seating": "7 persons"
        }
    },

    # Hybrid Vehicles (4 models including Aqua)
    "toyota_aqua": {
        "category": "hybrid",
        "name": "Toyota Aqua",
        "engine_cc": 1497,
        "fuel_type": "hybrid",
        "fuel_efficiency_kmpl": 28,
        "emission_factor": 0.095,
        "manufacturer": "Toyota",
        "verification": "PakWheels Verified: 1497cc hybrid with 28 km/l efficiency",
        "specifications": {
            "engine": "1497cc, 4-cylinder hybrid",
            "electric_motor": "45 kW permanent magnet",
            "battery": "0.9 kWh Ni-MH",
            "fuel_tank": "36 liters",
            "system_power": "100 hp",
            "weight": "1080 kg",
            "seating": "5 persons"
        }
    },
    "toyota_prius": {
        "category": "hybrid",
        "name": "Toyota Prius",
        "engine_cc": 1798,
        "fuel_type": "hybrid",
        "fuel_efficiency_kmpl": 25,
        "emission_factor": 0.135,
        "manufacturer": "Toyota",
        "verification": "PakWheels Verified: 1798cc hybrid with 25 km/l efficiency",
        "specifications": {
            "engine": "1798cc, 4-cylinder Atkinson cycle",
            "electric_motor": "60 kW permanent magnet",
            "battery": "1.3 kWh Ni-MH",
            "fuel_tank": "45 liters",
            "system_power": "134 hp",
            "weight": "1380 kg",
            "seating": "5 persons"
        }
    },
    "hyundai_santa_fe": {
        "category": "hybrid",
        "name": "Hyundai Santa Fe Hybrid",
        "engine_cc": 1600,
        "fuel_type": "hybrid",
        "fuel_efficiency_kmpl": 14,
        "emission_factor": 0.185,
        "manufacturer": "Hyundai",
        "verification": "Hyundai Santa Fe Hybrid with 14 km/l efficiency",
        "specifications": {
            "engine": "1600cc, 4-cylinder turbo hybrid",
            "electric_motor": "44 kW permanent magnet",
            "battery": "1.49 kWh lithium-ion",
            "fuel_tank": "67 liters",
            "system_power": "227 hp",
            "weight": "1885 kg",
            "seating": "7 persons"
        }
    },
    "toyota_corolla_cross": {
        "category": "hybrid",
        "name": "Toyota Corolla Cross Hybrid",
        "engine_cc": 1800,
        "fuel_type": "hybrid",
        "fuel_efficiency_kmpl": 22,
        "emission_factor": 0.115,
        "manufacturer": "Toyota",
        "verification": "Toyota Corolla Cross Hybrid with 22 km/l efficiency",
        "specifications": {
            "engine": "1800cc, 4-cylinder hybrid",
            "electric_motor": "70 kW permanent magnet",
            "battery": "1.6 kWh Ni-MH",
            "fuel_tank": "43 liters",
            "system_power": "121 hp",
            "weight": "1420 kg",
            "seating": "5 persons"
        }
    },

    # Electric Vehicles (2 models)
    "mg_zs_ev": {
        "category": "electric",
        "name": "MG ZS EV",
        "engine_cc": 0,
        "fuel_type": "electric",
        "fuel_efficiency_kmpl": 0,
        "emission_factor": 0.050,
        "manufacturer": "MG",
        "verification": "PakWheels Verified: Electric SUV with grid emission factor",
        "specifications": {
            "motor": "130 kW electric motor",
            "battery": "50.3 kWh lithium-ion",
            "range": "340 km per charge",
            "charging": "DC fast charging 0-80% in 40 min",
            "power": "174 hp",
            "torque": "280 Nm",
            "weight": "1585 kg",
            "seating": "5 persons"
        }
    },
    "nissan_leaf": {
        "category": "electric",
        "name": "Nissan Leaf",
        "engine_cc": 0,
        "fuel_type": "electric",
        "fuel_efficiency_kmpl": 0,
        "emission_factor": 0.055,
        "manufacturer": "Nissan",
        "verification": "Nissan Leaf with grid emission factor",
        "specifications": {
            "motor": "110 kW electric motor",
            "battery": "40 kWh lithium-ion",
            "range": "270 km per charge",
            "charging": "DC fast charging 0-80% in 60 min",
            "power": "147 hp",
            "torque": "320 Nm",
            "weight": "1580 kg",
            "seating": "5 persons"
        }
    }
}

NED_INSTITUTIONAL_DATA = {
    "employee_vehicles": 1300,
    "vehicle_distribution": {"cars": 70, "bikes": 30},
    "bus_fleet": {
        "count": 6,
        "type": "University Shuttle (Diesel)",
        "daily_operation_hours": 8,
        "average_speed_kmh": 25,
        "fuel_consumption_liter_hour": 12,
        "operating_days_per_year": 280,
    },
}

NED_EMPLOYEE_DISTRIBUTION = {
    "cars": {
        "suzuki_mehran": 25,
        "suzuki_alto": 30,
        "toyota_corolla_1.6": 25,
        "honda_civic_1.8": 15,
        "other_cars": 5,
    },
    "bikes": {
        "honda_cd70": 60,
        "honda_cg125": 25,
        "yamaha_ybr125": 10,
        "suzuki_gs150": 5,
    },
}

ACADEMIC_CALENDAR = {
    "fall_semester": {"weeks": 16, "months": ["September", "October", "November", "December"]},
    "spring_semester": {"weeks": 16, "months": ["January", "February", "March", "April"]},
    "summer_semester": {"weeks": 8, "months": ["May", "June", "July", "August"]},
}

# ============================== Helper Logic =============================== #

def calc_employee_emissions(avg_commute_km: float, working_days: int, traffic_factor: float):
    total_employees = NED_INSTITUTIONAL_DATA["employee_vehicles"]
    car_count = total_employees * NED_INSTITUTIONAL_DATA["vehicle_distribution"]["cars"] / 100
    bike_count = total_employees * NED_INSTITUTIONAL_DATA["vehicle_distribution"]["bikes"] / 100

    rows = []
    car_emissions = 0.0
    for car_type, percentage in NED_EMPLOYEE_DISTRIBUTION["cars"].items():
        if car_type == "other_cars":
            continue
        vehicle_count = car_count * percentage / 100
        v = VEHICLE_DATABASE[car_type]
        daily = avg_commute_km * v["emission_factor"] * traffic_factor
        annual = daily * working_days * vehicle_count
        car_emissions += annual
        rows.append({
            "Type": v["category"].title(),
            "Name": v["name"],
            "Count (est.)": round(vehicle_count),
            "Engine cc": v["engine_cc"],
            "Efficiency (km/l)": v["fuel_efficiency_kmpl"],
            "EF (kg/km)": v["emission_factor"],
            "Daily/vehicle (kg)": daily,
            "Annual total (kg)": annual,
        })

    # other cars via average factor of known cars
    other_pct = NED_EMPLOYEE_DISTRIBUTION["cars"].get("other_cars", 0)
    if other_pct > 0:
        vehicle_count = car_count * other_pct / 100
        keys = [k for k in NED_EMPLOYEE_DISTRIBUTION["cars"].keys() if k != "other_cars"]
        factors = [VEHICLE_DATABASE[k]["emission_factor"] for k in keys]
        avg_factor = sum(factors)/len(factors) if factors else 0.18
        daily = avg_commute_km * avg_factor * traffic_factor
        annual = daily * working_days * vehicle_count
        car_emissions += annual
        rows.append({
            "Type": "Car",
            "Name": "Other Cars (estimated)",
            "Count (est.)": round(vehicle_count),
            "Engine cc": "var",                   # <-- string to avoid Arrow int cast
            "Efficiency (km/l)": "var",           # <-- string to avoid Arrow float cast
            "EF (kg/km)": avg_factor,
            "Daily/vehicle (kg)": daily,
            "Annual total (kg)": annual,
        })

    bike_emissions = 0.0
    for bike_type, percentage in NED_EMPLOYEE_DISTRIBUTION["bikes"].items():
        vehicle_count = bike_count * percentage / 100
        v = VEHICLE_DATABASE[bike_type]
        daily = avg_commute_km * v["emission_factor"] * traffic_factor
        annual = daily * working_days * vehicle_count
        bike_emissions += annual
        rows.append({
            "Type": v["category"].title(),
            "Name": v["name"],
            "Count (est.)": round(vehicle_count),
            "Engine cc": v["engine_cc"],
            "Efficiency (km/l)": v["fuel_efficiency_kmpl"],
            "EF (kg/km)": v["emission_factor"],
            "Daily/vehicle (kg)": daily,
            "Annual total (kg)": annual,
        })

    df = pd.DataFrame(rows)
    total = car_emissions + bike_emissions
    return {
        "df": df,
        "car_count": car_count,
        "bike_count": bike_count,
        "total_employees": total_employees,
        "car_emissions": car_emissions,
        "bike_emissions": bike_emissions,
        "total_emissions": total,
    }


def calc_bus_emissions(daily_operation_hours: float, average_speed_kmh: float, fuel_consumption_liter_hour: float, operating_days_per_year: int):
    daily_distance_km = daily_operation_hours * average_speed_kmh
    daily_fuel = daily_operation_hours * fuel_consumption_liter_hour
    diesel_ef = 2.68  # kg CO2 per liter diesel
    daily_kg = daily_fuel * diesel_ef
    annual_per_bus = daily_kg * operating_days_per_year
    total = annual_per_bus * NED_INSTITUTIONAL_DATA["bus_fleet"]["count"]
    return {
        "bus_count": NED_INSTITUTIONAL_DATA["bus_fleet"]["count"],
        "daily_distance_km": daily_distance_km,
        "daily_fuel_liter": daily_fuel,
        "daily_emissions_kg": daily_kg,
        "annual_per_bus_kg": annual_per_bus,
        "total_annual_emissions_kg": total,
    }


def individual_calc(vehicle_key: str, daily_km: float, days_week: int, weeks_year: int, years: float):
    v = VEHICLE_DATABASE[vehicle_key]
    weekly_km = daily_km * days_week
    yearly_km = weekly_km * weeks_year
    total_km = yearly_km * years
    ef = v["emission_factor"]
    return {
        "vehicle_key": vehicle_key,
        "vehicle": v,
        "distances": {
            "daily_km": daily_km,
            "weekly_km": weekly_km,
            "yearly_km": yearly_km,
            "total_km": total_km
        },
        "emissions": {
            "daily_kg": daily_km * ef,
            "yearly_kg": yearly_km * ef,
            "total_kg": total_km * ef
        }
    }

# ---------------------------- Report Builders ----------------------------- #

def build_institutional_report(emp, bus, assumptions):
    total_emissions = emp["total_emissions"] + bus["total_annual_emissions_kg"]
    lines = []
    lines.append("\n" + "="*80)
    lines.append("🏛️ NED UNIVERSITY - INSTITUTIONAL CARBON FOOTPRINT")
    lines.append("="*80)
    lines.append(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("Data Source: PakWheels Database & NED Institutional Records")

    lines.append("\n🎯 EXECUTIVE SUMMARY")
    lines.append("-" * 50)
    lines.append(f"Total Employee Vehicles: {emp['total_employees']:,}")
    lines.append(f"University Buses: {bus['bus_count']}")
    lines.append(f"Total Annual Carbon Footprint: {total_emissions/1000:,.1f} tonnes CO₂e")
    lines.append(f"Employee Commuting: {emp['total_emissions']/1000:,.1f} tonnes CO₂e/year")
    lines.append(f"Bus Operations: {bus['total_annual_emissions_kg']/1000:,.1f} tonnes CO₂e/year")

    lines.append("\n👥 EMPLOYEE VEHICLES - PAKWHEELS VERIFIED")
    lines.append("=" * 55)
    lines.append("\nVehicle Distribution:")
    lines.append(f"  • Cars: {emp['car_count']:.0f} vehicles ({NED_INSTITUTIONAL_DATA['vehicle_distribution']['cars']}%)")
    lines.append(f"  • Motorcycles: {emp['bike_count']:.0f} vehicles ({NED_INSTITUTIONAL_DATA['vehicle_distribution']['bikes']}%)")

    lines.append("\nDetailed Breakdown:")
    df_sorted = emp["df"].sort_values("Annual total (kg)", ascending=False)
    for _, row in df_sorted.iterrows():
        lines.append(f"\n  {row['Name']}:")
        lines.append(f"    • Count: {row['Count (est.)']} vehicles")
        lines.append(f"    • Engine: {row['Engine cc']}cc")
        lines.append(f"    • Efficiency: {row['Efficiency (km/l)']} km/l")
        lines.append(f"    • Emission Factor: {row['EF (kg/km)']} kg CO₂e/km")
        lines.append(f"    • Daily Emissions: {row['Daily/vehicle (kg)']:.2f} kg CO₂e/vehicle")
        lines.append(f"    • Annual Total: {row['Annual total (kg)']/1000:.1f} tonnes CO₂e")

    lines.append("\n🚌 BUS FLEET OPERATIONS")
    lines.append("=" * 40)
    lines.append(f"Bus Type: {NED_INSTITUTIONAL_DATA['bus_fleet']['type']}")
    lines.append(f"Number of Buses: {bus['bus_count']}")
    lines.append(f"Daily Distance per Bus: {bus['daily_distance_km']:.1f} km")
    lines.append(f"Daily Fuel Consumption: {bus['daily_fuel_liter']:.1f} liters")
    lines.append(f"Daily Emissions per Bus: {bus['daily_emissions_kg']:.1f} kg CO₂e")
    lines.append(f"Annual Bus Fleet Emissions: {bus['total_annual_emissions_kg']/1000:.1f} tonnes CO₂e")

    total_tonnes = total_emissions / 1000
    trees_needed = total_tonnes * 6
    equivalent_cars = total_tonnes / 2.4

    lines.append("\n🌍 ENVIRONMENTAL IMPACT ASSESSMENT")
    lines.append("=" * 45)
    lines.append(f"Total Carbon Footprint: {total_tonnes:,.1f} tonnes CO₂e/year")
    lines.append("Equivalent Environmental Impact:")
    lines.append(f"  • Trees needed to absorb emissions: {trees_needed:,.0f} trees")
    lines.append(f"  • Equivalent to {equivalent_cars:.0f} average cars for one year")

    # Assumptions block
    lines.append("\nASSUMPTIONS")
    lines.append("-"*20)
    lines.append(f"Average commute (km round trip): {assumptions['avg_commute_km']}")
    lines.append(f"Working days / year: {assumptions['working_days']}")
    lines.append(f"Traffic factor (Karachi): {assumptions['traffic_factor']}")
    lines.append(f"Bus operating days / year: {assumptions['operating_days_per_year']}")

    return "\n".join(lines)


def build_individual_report(individuals_list):
    lines = []
    lines.append("\n" + "="*80)
    lines.append("🚗 INDIVIDUAL VEHICLE CALCULATIONS SUMMARY")
    lines.append("="*80)

    total_emissions = sum(item["calc"]["emissions"]["total_kg"] for item in individuals_list)
    lines.append(f"Total Individual Vehicles: {len(individuals_list)}")
    lines.append(f"Total Individual Emissions: {total_emissions/1000:.3f} tonnes CO₂e")

    # Breakdown by user type
    by_user_type = {}
    for item in individuals_list:
        utype = item["user"]["role"]
        by_user_type.setdefault(utype, []).append(item)

    lines.append("\n👥 BREAKDOWN BY USER TYPE:")
    for utype, arr in by_user_type.items():
        u_em = sum(x["calc"]["emissions"]["total_kg"] for x in arr)
        lines.append(f"  {utype}: {len(arr)} vehicles, {u_em/1000:.3f} tonnes CO₂e")

    lines.append("\n🔍 DETAILED VEHICLE ANALYSIS:")
    for i, item in enumerate(individuals_list, 1):
        v = item["calc"]["vehicle"]
        d = item["calc"]["distances"]
        e = item["calc"]["emissions"]
        user = item["user"]
        lines.append(f"\nVEHICLE {i}: {v['name']}")
        lines.append(f"  User: {user['name'] or 'Anonymous'} ({user['role']})")
        lines.append(f"  Period: {user['years']} year(s)")
        lines.append(f"  Total Distance: {d['total_km']:.1f} km")
        lines.append(f"  Total Emissions: {e['total_kg']/1000:.3f} tonnes CO₂e")

    return "\n".join(lines)


# ============================== UI Styling ================================ #

with st.sidebar:
    st.markdown("## 🌍 NED Carbon Calculator — Full Web App")
    st.caption("High-fidelity analysis • PakWheels-verified database")
    st.divider()

    st.markdown("### Appearance")
    theme = st.selectbox("Accent style", ["Lush", "Ocean", "Sunset", "Graphite"], index=0)
    accents = {"Lush": "#0FB77A", "Ocean": "#3E92CC", "Sunset": "#F2542D", "Graphite": "#5B5B5B"}
    accent = accents.get(theme, "#0FB77A")
    st.markdown(
        f"""
        <style>
        :root {{ --accent: {accent}; }}
        .stButton>button, .stDownloadButton>button {{
            background: var(--accent); color: white; border-radius: 12px; border: 0; padding: 0.6rem 1rem; font-weight:600;
        }}
        .stTabs [data-baseweb='tab'] {{ font-weight: 600; }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.divider()
    st.markdown("### Global Assumptions")
    avg_commute_km = st.number_input("Avg commute km (round trip)", min_value=1.0, value=22.0, step=1.0, help="Used for institutional employee commuting")
    working_days = st.number_input("Working days per year", min_value=1, max_value=366, value=230, step=1)
    traffic_factor = st.number_input("Traffic factor (Karachi)", min_value=1.0, value=1.15, step=0.05)

    st.markdown("### Bus Fleet Settings")
    bus_cfg = NED_INSTITUTIONAL_DATA["bus_fleet"].copy()
    daily_operation_hours = st.number_input("Daily operation hours", min_value=1.0, value=float(bus_cfg["daily_operation_hours"]), step=0.5)
    average_speed_kmh = st.number_input("Average speed (km/h)", min_value=1.0, value=float(bus_cfg["average_speed_kmh"]), step=1.0)
    fuel_consumption_liter_hour = st.number_input("Fuel cons. (L/hour)", min_value=0.1, value=float(bus_cfg["fuel_consumption_liter_hour"]), step=0.1)
    operating_days_per_year = st.number_input("Operating days / year", min_value=1, max_value=366, value=int(bus_cfg["operating_days_per_year"]), step=1)

st.title("🏛️ NED University Carbon Footprint Calculator — Full Feature UI")
st.caption("Institutional, Individual & Combined analysis • Cleaned v2 logic, 1:1 parity")

inst_tab, indiv_tab, combined_tab, db_tab = st.tabs([
    "Institutional Analysis",
    "Individual Calculator",
    "Combined Report",
    "Vehicle Database",
])

# =============================== Institutional ============================ #
with inst_tab:
    st.subheader("Institutional Analysis")
    emp = calc_employee_emissions(avg_commute_km, working_days, traffic_factor)
    bus_res = calc_bus_emissions(daily_operation_hours, average_speed_kmh, fuel_consumption_liter_hour, operating_days_per_year)
    total_inst_kg = emp["total_emissions"] + bus_res["total_annual_emissions_kg"]

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total vehicles (est.)", f"{emp['total_employees']:,}")
    c2.metric("Cars : Bikes", f"{int(emp['car_count']):,} : {int(emp['bike_count']):,}")
    c3.metric("Employee commuting (tCO₂e/y)", f"{emp['total_emissions']/1000:,.1f}")
    c4.metric("Buses (tCO₂e/y)", f"{bus_res['total_annual_emissions_kg']/1000:,.1f}")

    st.markdown("### Employee Breakdown (cars & bikes)")
    # Arrow-safe display copy
    df_emp_display = emp["df"].sort_values("Annual total (kg)", ascending=False).copy()
    for col in ["Engine cc", "Efficiency (km/l)"]:
        if col in df_emp_display.columns:
            df_emp_display[col] = df_emp_display[col].astype(str)
    st.dataframe(df_emp_display, width='stretch')

    with st.expander("Bus Fleet Details", expanded=False):
        b1, b2, b3 = st.columns(3)
        b1.metric("Bus count", bus_res["bus_count"])
        b2.metric("Daily distance/bus (km)", f"{bus_res['daily_distance_km']:.1f}")
        b3.metric("Daily fuel/bus (L)", f"{bus_res['daily_fuel_liter']:.1f}")
        st.write(f"Daily emissions/bus: **{bus_res['daily_emissions_kg']:.1f} kg CO₂e**")
        st.write(f"Annual bus fleet: **{bus_res['total_annual_emissions_kg']/1000:.1f} tCO₂e**")

    st.markdown("### Totals & Equivalents")
    tt1, tt2, tt3 = st.columns(3)
    tt1.metric("Institutional total (tCO₂e/year)", f"{total_inst_kg/1000:,.1f}")
    trees = (total_inst_kg/1000) * 6
    eq_cars = (total_inst_kg/1000) / 2.4
    tt2.metric("Trees needed (est.)", f"{trees:,.0f}")
    tt3.metric("Equivalent cars (est.)", f"{eq_cars:,.0f}")

    # Downloads
    assumptions = {
        "avg_commute_km": avg_commute_km,
        "working_days": working_days,
        "traffic_factor": traffic_factor,
        "operating_days_per_year": operating_days_per_year,
    }
    inst_text = build_institutional_report(emp, bus_res, assumptions)
    st.download_button("⬇️ Download executive summary (TXT)", data=inst_text, file_name=f"ned_institutional_{datetime.now().strftime('%Y%m%d_%H%M')}.txt")
    csv_breakdown = emp["df"].to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download breakdown (CSV)", data=csv_breakdown, file_name="employee_breakdown.csv")

# =============================== Individual =============================== #
with indiv_tab:
    st.subheader("Individual Vehicle Calculator (Multi-entry)")

    if "individuals" not in st.session_state:
        st.session_state.individuals = []  # list of dicts: {user, calc}

    # Role & academic weeks
    colr, coln = st.columns([1,1])
    role = colr.selectbox("Your role", ["Student", "Faculty", "Staff", "Contractor", "Visitor"], index=0)
    name = coln.text_input("Your Name (optional)", "")

    if role == "Student":
        st.markdown("**Academic semesters** (choose to auto-set weeks/year)")
        sem_col1, sem_col2, sem_col3 = st.columns(3)
        fall = sem_col1.checkbox("Fall (16 wks)", value=True)
        spring = sem_col2.checkbox("Spring (16 wks)", value=True)
        summer = sem_col3.checkbox("Summer (8 wks)", value=False)
        total_weeks = (16 if fall else 0) + (16 if spring else 0) + (8 if summer else 0)
        if total_weeks == 0:
            total_weeks = 40  # default academic year
    else:
        total_weeks = 48  # working year default

    # Vehicle picker
    st.divider()
    left, right = st.columns([2,1])
    nice_labels = [f"{v['name']} • {v['category'].title()} • {v['emission_factor']} kg/km" for k,v in VEHICLE_DATABASE.items()]
    keys = list(VEHICLE_DATABASE.keys())
    label = left.selectbox("Select your vehicle", options=nice_labels, index=0)
    vehicle_key = keys[nice_labels.index(label)]
    v = VEHICLE_DATABASE[vehicle_key]

    with right:
        st.metric("Emission factor", f"{v['emission_factor']} kg/km")
        st.metric("Fuel type", v['fuel_type'].title())
        st.metric("Engine", f"{v['engine_cc']} cc" if v['engine_cc'] else "—")

    with st.form("usage_form"):
        c1, c2, c3, c4 = st.columns(4)
        daily_km = c1.number_input("Daily commute (km, round trip)", min_value=1.0, value=22.0, step=1.0)
        days_week = c2.number_input("Days per week", min_value=1, max_value=7, value=5, step=1)
        weeks_year = c3.number_input("Weeks per year", min_value=1, max_value=52, value=int(total_weeks), step=1)
        years = c4.number_input("Years (planning period)", min_value=0.5, value=2.0, step=0.5)
        add_btn = st.form_submit_button("Add to list", use_container_width=True)

    if add_btn:
        calc = individual_calc(vehicle_key, daily_km, int(days_week), int(weeks_year), float(years))
        st.session_state.individuals.append({
            "user": {"name": name, "role": role, "years": float(years), "weeks_year": int(weeks_year)},
            "calc": calc
        })
        st.success("Vehicle added to list.")

    # Current list
    if st.session_state.individuals:
        st.markdown("### Your Vehicles")
        rows = []
        for idx, item in enumerate(st.session_state.individuals):
            v = item["calc"]["vehicle"]
            e = item["calc"]["emissions"]
            d = item["calc"]["distances"]
            rows.append({
                "#": idx+1,
                "User": item["user"]["name"] or "Anonymous",
                "Role": item["user"]["role"],
                "Vehicle": v["name"],
                "EF (kg/km)": v["emission_factor"],
                "Daily (kg)": round(e["daily_kg"], 3),
                "Yearly (kg)": round(e["yearly_kg"], 2),
                "Total (kg)": round(e["total_kg"], 2),
                "Total (tCO₂e)": round(e["total_kg"]/1000, 3),
                "Total km": round(d["total_km"], 1),
                "Years": item["user"]["years"],
            })
        df_ind = pd.DataFrame(rows)
        st.dataframe(df_ind, width='stretch')

        col_rm1, col_rm2 = st.columns([1,1])
        idx_to_remove = col_rm1.number_input("Remove by serial #", min_value=1, max_value=len(st.session_state.individuals), value=1)
        if col_rm2.button("Remove selected", use_container_width=True):
            st.session_state.individuals.pop(int(idx_to_remove)-1)
            st.rerun()  # updated API

        # Totals & downloads
        total_ind_kg = sum(item["calc"]["emissions"]["total_kg"] for item in st.session_state.individuals)
        tA, tB, tC = st.columns(3)
        tA.metric("Total individual (tCO₂e)", f"{total_ind_kg/1000:,.3f}")
        tB.metric("Vehicles in list", f"{len(st.session_state.individuals)}")
        tC.metric("Trees needed (est.)", f"{(total_ind_kg/1000)*6:,.1f}")

        ind_text = build_individual_report(st.session_state.individuals)
        st.download_button("⬇️ Download individual summary (TXT)", data=ind_text, file_name=f"ned_individual_{datetime.now().strftime('%Y%m%d_%H%M')}.txt")
        st.download_button("⬇️ Download table (CSV)", data=df_ind.to_csv(index=False).encode("utf-8"), file_name="individuals.csv")
    else:
        st.info("Add a vehicle above to build your individual report.")

# =============================== Combined ================================= #
with combined_tab:
    st.subheader("Combined Report (Institutional + Individual)")

    # Recompute institutional with current sidebar assumptions
    emp = calc_employee_emissions(avg_commute_km, working_days, traffic_factor)
    bus_res = calc_bus_emissions(daily_operation_hours, average_speed_kmh, fuel_consumption_liter_hour, operating_days_per_year)
    inst_total_kg = emp["total_emissions"] + bus_res["total_annual_emissions_kg"]

    # Individual totals from session list
    ind_total_kg = sum(item["calc"]["emissions"]["total_kg"] for item in st.session_state.get("individuals", []))

    c1, c2, c3 = st.columns(3)
    c1.metric("Institutional (tCO₂e/y)", f"{inst_total_kg/1000:,.1f}")
    c2.metric("Individual (tCO₂e)", f"{ind_total_kg/1000:,.3f}")
    c3.metric("Combined total (tCO₂e)", f"{(inst_total_kg+ind_total_kg)/1000:,.3f}")

    # Build long-form combined text
    assumptions = {
        "avg_commute_km": avg_commute_km,
        "working_days": working_days,
        "traffic_factor": traffic_factor,
        "operating_days_per_year": operating_days_per_year,
    }
    text_inst = build_institutional_report(emp, bus_res, assumptions)
    text_ind = build_individual_report(st.session_state.get("individuals", [])) if st.session_state.get("individuals") else "\n(No individual vehicles calculated yet.)"
    combined_text = text_inst + "\n\n" + text_ind

    st.download_button("⬇️ Download combined report (TXT)", data=combined_text, file_name=f"ned_combined_{datetime.now().strftime('%Y%m%d_%H%M')}.txt")

# =============================== Vehicle DB ================================ #
with db_tab:
    st.subheader("PakWheels-verified Vehicle Database")
    cats = ["All", "motorcycle", "car", "hybrid", "electric", "suv"]
    cat = st.selectbox("Filter by category", cats, index=0)

    rows = []
    for key, v in VEHICLE_DATABASE.items():
        if cat != "All" and v["category"] != cat:
            continue
        rows.append({
            "Key": key,
            "Name": v["name"],
            "Category": v["category"].title(),
            "Engine cc": v["engine_cc"],
            "Fuel": v["fuel_type"].title(),
            "Efficiency (km/l)": v["fuel_efficiency_kmpl"],
            "Emission factor (kg/km)": v["emission_factor"],
            "Verification": v["verification"],
        })

    df_db = pd.DataFrame(rows)
    st.dataframe(df_db, width='stretch')
    st.download_button("⬇️ Download database (CSV)", data=df_db.to_csv(index=False).encode("utf-8"), file_name="vehicle_database.csv")

    # Vehicle details viewer
    st.markdown("### Vehicle Details")
    sel = st.selectbox("Choose a model to view details", ["—"] + [v["name"] for v in VEHICLE_DATABASE.values()], index=0)
    if sel != "—":
        for key, v in VEHICLE_DATABASE.items():
            if v["name"] == sel:
                st.write(f"**Manufacturer:** {v['manufacturer']}")
                st.write(
                    f"**Engine:** {v['engine_cc']} cc • **Fuel:** {v['fuel_type'].title()}\n\n"
                    f"**Fuel efficiency:** {v['fuel_efficiency_kmpl']} km/l"
                )
                st.write(f"**Emission factor:** {v['emission_factor']} kg CO₂e/km")
                st.write(f"**Verification:** {v['verification']}")
                with st.expander("Technical specifications"):
                    for s, val in v["specifications"].items():
                        st.write(f"• {s.replace('_',' ').title()}: {val}")
                break

# =============================== Footer =================================== #
st.caption("Made for NED University • Streamlit full-port of Cleaned v2 • All calculations parity matched")