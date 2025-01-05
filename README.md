# Urbanalize

Urbanalize is a Python library for geospatial analysis of cities using OpenStreetMap data. The library provides tools to compute statistics on road networks and natural areas within a city, enabling detailed analysis of urban infrastructure and natural resources.

---

## Features

### 1. **Road Statistics** (`road_stats`)
- Calculates road length and density statistics for a specific city.
- Groups roads by categories (e.g., "residential", "primary").
- Computes the total length of roads and the density (km of roads per km² of city area).

### 2. **Natural Features Statistics** (`natural_stats`)
- Analyzes natural features (e.g., parks, water bodies) within a city.
- Calculates the total area for each type of natural feature.
- Determines the relative density of each type of natural feature as a percentage of the city's total area.

---

## Installation

### Prerequisites
- **Python 3.10 or higher**
- Required Python libraries:
  - `osmnx`
  - `geopandas`
  - `requests`
  - `shapely`

### Install Dependencies
The easiest way to set up the environment is by using the provided `environment.yml` file. Run the following command:
```bash
conda env create -f environment.yml
```
---

## Usage
Urbanalize makes it simple to analyze urban areas. Just provide the name of a city, and the library does the rest. Below are examples of how to use the key functions.

### 1. Calculate Road Statistics
The road_stats function computes detailed statistics on road networks for a given city.

**Example:**
from urbanalize import road_stats
road_stats("Milan")

**Expected Output:**
The function will display statistics similar to:

Thank you for using this function!
Extracting road statistics for the city of Milan might take a few minutes.
Road statistics for the city of Milan are ready:
   category      length (km)  density (km/km²)
   primary          120.5             2.14
   residential       430.8             7.62
   ...

### 2. Calculate Natural Statistics
The natural_stats function computes statistics for natural features (e.g., parks, water) in a city.

**Example:**

```python
from urbanalize import natural_stats

natural_stats("Rome")
```
**Expected Output:**
The function will display statistics similar to:

```sql
Thank you for using this function!
Extracting natural statistics for the city of Rome might take a few minutes.
Natural statistics for the city of Rome are ready:
   type        area_km2  density (%)
   park           15.421        3.12
   water           5.672        1.15
   ...
```

The simplicity of providing only a city name and obtaining detailed statistics makes Urbanalize a powerful tool for urban analysis.

---

## Acknowledgements
Urbanalize heavily relies on the following libraries:

- `osmnx`: A Python package that simplifies the acquisition and analysis of street networks and other geospatial data from OpenStreetMap.
- `requests`: A simple and elegant HTTP library for Python, used for querying the Overpass API to retrieve geospatial data. I extend special thanks to the developers of these libraries for making tools like Urbanalize possible.