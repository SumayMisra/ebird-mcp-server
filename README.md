# eBird MCP Server

A Model Context Protocol (MCP) server that provides access to the eBird API, allowing Claude Desktop to retrieve bird observation data, species information, and regional statistics.

## Features

This MCP server provides access to various eBird API endpoints including:

- **Recent Observations**: Get recent bird observations for any region
- **Notable Observations**: Find rare or notable bird sightings
- **Species-specific Data**: Search for observations of specific species
- **Geographic Searches**: Find observations near specific coordinates
- **Historical Data**: Access historical observation data
- **Taxonomy Information**: Get species taxonomy and classification data
- **Regional Statistics**: Access arrival/departure statistics
- **Hotspot Information**: Find and explore birding hotspots

## Prerequisites

Before setting up this MCP server, ensure you have:

1. **Python 3.12 or higher** installed on your system
2. **Claude Desktop** installed and configured
3. **Git** installed (for cloning the repository)

## Installation

### Step 1: Clone the Repository
1. Go to the local git repository directory
 Examples: C:\\Users\\<username>\\dev **Windows**
           /Users/<username>/dev      **Mac-OS** 
2. Run
```bash
git clone https://github.com/SumayMisra/ebird-mcp-server.git
cd ebird-mcp-server
```
This will create a directory **ebird-mcp-server** in the git respository directory and place all code there 

### Step 2: Install Dependencies

The project uses `uv` for dependency management. If you don't have `uv` installed, you can install it with:

```bash
pip install uv
```

Then install the project dependencies:

```bash
uv sync
```

Alternatively, if you prefer using pip:

```bash
pip install -r requirements.txt
```

### Step 3: Get an eBird API Token

1. Visit the [eBird API website](https://documenter.getpostman.com/view/664302/S1ENwy59)
2. Sign up for an eBird account if you don't have one
3. Request an API token by following their documentation
4. Note down your API token for the next step

### Step 4: Configure the API Token

Open `server.py` and replace the API token on line 15:

```python
headers = {
    "X-eBirdApiToken": "YOUR_API_TOKEN_HERE"
}
```

Replace `YOUR_API_TOKEN_HERE` with your actual eBird API token.

### Step 5: Test Your Setup

Run the test script to verify everything is working:

```bash
python test_server.py
```

This will test your API connection and basic functionality. If all tests pass, you're ready to configure Claude Desktop!

## Setting up with Claude Desktop

### Step 1: Configure Claude Desktop

1. Open Claude Desktop
2. Go to **Settings** (profile icon)
3. Click **Developer**
4. Click **Edit Config**
5. This opens the folder containing file **claude_desktop_config.json**

### Step 2: Add the MCP Server

In the **claude_desktop_config.json** file, copy the below for **Windows**
```
{
  "mcpServers": {
    "ebird": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\Users\\<username>\\dev\\ebird-mcp-server",
        "run",
        "server.py"
      ]
    }
  }
}
```
 For **Mac-OS** 
 replace ```C:\\Users\\<username>\\dev\\ebird-mcp-server```
 with    ```/Users/<username>/dev/ebird-mcp-server```


### Step 3: Test the Connection

1. Save the configuration
2. Restart Claude Desktop
3. Start a New Chat
4. Now you should see **eBird** in the drop down 
   <img width="1073" height="541" alt="image" src="https://github.com/user-attachments/assets/272b8310-3912-46ad-8c60-f7b379f1b9fc" />
5. Try asking Claude about bird observations, for example:
   - "What recent bird observations are there in California?"
   - "Show me notable bird sightings near San Francisco"
   - "What species have been observed in Central Park recently?"

## Usage Examples

Once configured, you can ask Claude to use the eBird data in various ways:

### Recent Observations
- "Get recent bird observations for New York state"
- "Show me the last 7 days of observations in Central Park"

### Notable Sightings
- "What rare birds have been spotted in California this week?"
- "Show me notable observations near my location"

### Species-specific Queries
- "Find recent observations of American Robins in my area"
- "Show me where Bald Eagles have been spotted recently"

### Geographic Searches
- "What birds have been observed near coordinates 40.7128, -74.0060?"
- "Find bird observations within 25 miles of San Francisco"

### Historical Data
- "What birds were observed in Central Park on March 15, 2024?"
- "Show me historical data for American Goldfinches in California"

## API Endpoints Available

The MCP server provides access to these eBird API endpoints:

### Observations
- `get_recent_observations` - Recent observations for a region
- `get_recent_notable_observations` - Notable/recent sightings
- `get_recent_species_observations` - Species-specific observations
- `get_nearest_observations_of_species` - Nearest sightings of a species
- `get_nearby_observations` - Nearby observations by location
- `get_nearby_notable_observations` - Nearby notable sightings
- `get_nearby_species_observations` - Nearby species-specific observations
- `get_historic_observations` - Historical observation data

### Products
- `get_checklist` - Detailed checklist information
- `get_species_list` - Species list for a region
- `get_regional_statistics` - Regional statistics
- `get_species_statistics` - Species-specific statistics
- `get_top_100` - Top contributors
- `get_checklist_feed` - Checklist feeds

### Reference Data
- `get_taxonomy` - Species taxonomy
- `get_region_list` - Available regions
- `get_region_info` - Region information
- `get_hotspots_in_region` - Birding hotspots
- `get_hotspot_info` - Hotspot details

## Troubleshooting

### Common Issues

1. **"Module not found" errors**
   - Ensure you've installed dependencies with `uv sync` or `pip install -r requirements.txt`
   - Verify you're using Python 3.12 or higher

2. **API authentication errors**
   - Check that your eBird API token is correctly set in `server.py`
   - Verify your API token is valid and active

3. **Claude Desktop can't connect to the server**
   - Ensure the working directory path is correct
   - Check that `server.py` is executable
   - Verify Python is in your system PATH

4. **No data returned**
   - Check that your region codes are valid (e.g., "US-CA" for California)
   - Verify the date parameters are in the correct format
   - Ensure your API token has the necessary permissions

### Getting Help

If you encounter issues:

1. **Run the test script first**: `python test_server.py` to verify your setup
2. Check the Claude Desktop logs for error messages
3. Verify your eBird API token is working by testing it directly
4. Ensure all dependencies are properly installed
5. Check that the server.py file is in the correct working directory

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [eBird API](https://documentation.ebird.org/en/home.html) for providing the bird observation data
- [Model Context Protocol](https://modelcontextprotocol.io/) for the MCP specification
- [Claude Desktop](https://claude.ai/) for the AI assistant platform
