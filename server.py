# server.py
from mcp.server.fastmcp import FastMCP
import requests
from typing import List, Dict, Optional
from datetime import datetime

# Create an MCP server
mcp = FastMCP("server-mcp-ebird-api")

# Base URL for eBird API
EBIRD_API_BASE = "https://api.ebird.org/v2"

# Helper function to make API requests
def make_ebird_request(endpoint: str, params: Optional[Dict] = None) -> Dict:
    """Make a request to the eBird API"""
    headers = {
        "X-eBirdApiToken": "YOUR_API_TOKEN_HERE"
    }
    response = requests.get(f"{EBIRD_API_BASE}/{endpoint}", headers=headers, params=params)
    response.raise_for_status()
    return response.json()

# OBSERVATIONS DATA ENDPOINTS

@mcp.tool()
def get_recent_observations(region_code: str, back: int = 14, max_results: int = 100, include_provisional: bool = False, hotspot: bool = False) -> List[Dict]:
    """Get recent observations for a region"""
    params = {
        "back": back,
        "maxResults": max_results,
        "includeProvisional": include_provisional,
        "hotspot": hotspot
    }
    return make_ebird_request(f"data/obs/{region_code}/recent", params)

@mcp.tool()
def get_recent_notable_observations(region_code: str, back: int = 14, max_results: int = 100, include_provisional: bool = False, hotspot: bool = False, detail: str = "simple") -> List[Dict]:
    """Get recent notable observations for a regi   on"""
    params = {
        "back": back,
        "maxResults": max_results,
        "includeProvisional": include_provisional,
        "hotspot": hotspot,
        "detail": detail
    }
    return make_ebird_request(f"data/obs/{region_code}/recent/notable", params)

@mcp.tool()
def get_recent_species_observations(region_code: str, species_code: str, back: int = 14, max_results: int = 100, include_provisional: bool = False, hotspot: bool = False) -> List[Dict]:
    """Get recent observations for a specific species in a region"""
    params = {
        "back": back,
        "maxResults": max_results,
        "includeProvisional": include_provisional,
        "hotspot": hotspot
    }
    return make_ebird_request(f"data/obs/{region_code}/recent/{species_code}", params)

@mcp.tool()
def get_nearest_observations_of_species(species_code: str, lat: float, lng: float, back: int = 14, max_results: int = 100, dist: int = 25, include_provisional: bool = False, hotspot: bool = False) -> List[Dict]:
    """Get nearest observations of a species"""
    params = {
        "lat": lat,
        "lng": lng,
        "back": back,
        "maxResults": max_results,
        "dist": dist,
        "includeProvisional": include_provisional,
        "hotspot": hotspot
    }
    return make_ebird_request(f"data/nearest/geo/recent/{species_code}", params)

@mcp.tool()
def get_nearby_observations(lat: float, lng: float, back: int = 14, max_results: int = 100, dist: int = 25, include_provisional: bool = False, hotspot: bool = False, sort: str = "date") -> List[Dict]:
    """Get recent nearby observations"""
    params = {
        "lat": lat,
        "lng": lng,
        "back": back,
        "maxResults": max_results,
        "dist": dist,
        "includeProvisional": include_provisional,
        "hotspot": hotspot,
        "sort": sort
    }
    return make_ebird_request("data/obs/geo/recent", params)

@mcp.tool()
def get_nearby_notable_observations(lat: float, lng: float, back: int = 14, max_results: int = 100, dist: int = 25, include_provisional: bool = False, hotspot: bool = False, detail: str = "simple") -> List[Dict]:
    """Get recent nearby notable observations"""
    params = {
        "lat": lat,
        "lng": lng,
        "back": back,
        "maxResults": max_results,
        "dist": dist,
        "includeProvisional": include_provisional,
        "hotspot": hotspot,
        "detail": detail
    }
    return make_ebird_request("data/obs/geo/recent/notable", params)

@mcp.tool()
def get_nearby_species_observations(species_code: str, lat: float, lng: float, back: int = 14, max_results: int = 100, dist: int = 25, include_provisional: bool = False, hotspot: bool = False) -> List[Dict]:
    """Get recent nearby observations of a species"""
    params = {
        "lat": lat,
        "lng": lng,
        "back": back,
        "maxResults": max_results,
        "dist": dist,
        "includeProvisional": include_provisional,
        "hotspot": hotspot
    }
    return make_ebird_request(f"data/obs/geo/recent/{species_code}", params)

@mcp.tool()
def get_historic_observations(region_code: str, year: int, month: int, day: int, max_results: int = 100, include_provisional: bool = False, hotspot: bool = False, rank: str = "mrec") -> List[Dict]:
    """Get historic observations for a specific date"""
    params = {
        "maxResults": max_results,
        "includeProvisional": include_provisional,
        "hotspot": hotspot,
        "rank": rank
    }
    return make_ebird_request(f"data/obs/{region_code}/historic/{year}/{month}/{day}", params)

# PRODUCT ENDPOINTS

@mcp.tool()
def get_checklist(sub_id: str) -> Dict:
    """Get details for a specific checklist"""
    return make_ebird_request(f"product/checklist/view/{sub_id}")

@mcp.tool()
def get_species_list(region_code: str, fmt: str = "json") -> List[Dict]:
    """Get list of species for a region"""
    params = {"fmt": fmt}
    return make_ebird_request(f"product/spplist/{region_code}", params)

@mcp.tool()
def get_regional_statistics(region_code: str, year: int, month: int, day: int) -> Dict:
    """Get arrival and departure date statistics for a region"""
    return make_ebird_request(f"product/stats/{region_code}/{year}/{month}/{day}")

@mcp.tool()
def get_species_statistics(region_code: str, species_code: str, year: int, month: int, day: int) -> Dict:
    """Get arrival and departure statistics for a species in a region"""
    return make_ebird_request(f"product/stats/{region_code}/{species_code}/{year}/{month}/{day}")

@mcp.tool()
def get_top_100(region_code: str, year: int, month: int, day: int, rank_by: str = "spp", max_results: int = 100) -> List[Dict]:
    """Get top 100 contributors for a date"""
    params = {
        "rankBy": rank_by,
        "maxResults": max_results
    }
    return make_ebird_request(f"product/top100/{region_code}/{year}/{month}/{day}", params)

@mcp.tool()
def get_checklist_feed(region_code: str, year: int, month: int, day: int, sort_key: str = "obs_dt", max_results: int = 200) -> List[Dict]:
    """Get checklist feed for a region and date"""
    params = {
        "sortKey": sort_key,
        "maxResults": max_results
    }
    return make_ebird_request(f"product/lists/{region_code}/{year}/{month}/{day}", params)

@mcp.tool()
def get_regional_checklist_feed(region_code: str, year: int, month: int, day: int, sort_key: str = "creation_dt", max_results: int = 200) -> List[Dict]:
    """Get regional checklist feed"""
    params = {
        "sortKey": sort_key,
        "maxResults": max_results
    }
    return make_ebird_request(f"product/lists/{region_code}/{year}/{month}/{day}", params)

@mcp.tool()
def get_view_checklist(sub_id: str) -> Dict:
    """View a checklist submission"""
    return make_ebird_request(f"product/checklist/view/{sub_id}")

# REFERENCE DATA ENDPOINTS

@mcp.tool()
def get_taxonomy(fmt: str = "json", locale: str = "en", species_group: Optional[str] = None, version: Optional[str] = None) -> List[Dict]:
    """Get the eBird taxonomy"""
    params = {
        "fmt": fmt,
        "locale": locale
    }
    if species_group:
        params["cat"] = species_group
    if version:
        params["version"] = version
    return make_ebird_request("ref/taxonomy/ebird", params)

@mcp.tool()
def get_taxonomy_forms(species_code: str) -> List[Dict]:
    """Get taxonomic forms for a species"""
    return make_ebird_request(f"ref/taxonomy/forms/{species_code}")

@mcp.tool()
def get_taxa_locale_codes(fmt: str = "json") -> List[Dict]:
    """Get supported locale codes and names"""
    params = {"fmt": fmt}
    return make_ebird_request("ref/taxonomy/locales", params)

@mcp.tool()
def get_taxonomy_versions(fmt: str = "json") -> List[Dict]:
    """Get taxonomy version rollup"""
    params = {"fmt": fmt}
    return make_ebird_request("ref/taxonomy/versions", params)

@mcp.tool()
def get_taxonomy_groups(group_name_locale: str = "en", fmt: str = "json") -> List[Dict]:
    """Get taxonomy species groups"""
    params = {
        "groupNameLocale": group_name_locale,
        "fmt": fmt
    }
    return make_ebird_request("ref/sppgroup/merlin", params)

@mcp.tool()
def get_region_list(region_type: str, parent_region: Optional[str] = None, fmt: str = "json") -> List[Dict]:
    """Get list of regions"""
    endpoint = f"ref/region/list/{region_type}"
    if parent_region:
        endpoint += f"/{parent_region}"
    params = {"fmt": fmt}
    return make_ebird_request(endpoint, params)

@mcp.tool()
def get_region_info(region_code: str, region_name_format: str = "detailed", fmt: str = "json") -> Dict:
    """Get information about a region"""
    params = {
        "regionNameFormat": region_name_format,
        "fmt": fmt
    }
    return make_ebird_request(f"ref/region/info/{region_code}", params)

@mcp.tool()
def get_hotspots_in_region(region_code: str, back: Optional[int] = None, fmt: str = "json") -> List[Dict]:
    """Get hotspots in a region"""
    params = {"fmt": fmt}
    if back:
        params["back"] = back
    return make_ebird_request(f"ref/hotspot/{region_code}", params)

@mcp.tool()
def get_nearby_hotspots(lat: float, lng: float, back: Optional[int] = None, dist: int = 25, fmt: str = "json") -> List[Dict]:
    """Get nearby hotspots"""
    params = {
        "lat": lat,
        "lng": lng,
        "dist": dist,
        "fmt": fmt
    }
    if back:
        params["back"] = back
    return make_ebird_request("ref/hotspot/geo", params)

@mcp.tool()
def get_hotspot_info(loc_id: str, fmt: str = "json") -> Dict:
    """Get information about a hotspot"""
    params = {"fmt": fmt}
    return make_ebird_request(f"ref/hotspot/info/{loc_id}", params)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
