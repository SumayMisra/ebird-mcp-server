#!/usr/bin/env python3
"""
Test script for the eBird MCP Server
Run this script to verify that your server is working correctly.
"""

import sys
import json
from server import make_ebird_request

def test_api_connection():
    """Test the eBird API connection"""
    try:
        print("Testing eBird API connection...")
        
        # Test a simple endpoint - get taxonomy
        result = make_ebird_request("ref/taxonomy/ebird", {"fmt": "json"})
        
        if result and len(result) > 0:
            print("✅ API connection successful!")
            print(f"Retrieved {len(result)} taxonomy records")
            return True
        else:
            print("❌ API returned empty response")
            return False
            
    except Exception as e:
        print(f"❌ API connection failed: {e}")
        print("Please check your API token in server.py")
        return False

def test_basic_endpoints():
    """Test basic endpoint functionality"""
    try:
        print("\nTesting basic endpoints...")
        
        # Test getting a region list
        regions = make_ebird_request("ref/region/list/country", {"fmt": "json"})
        if regions:
            print("✅ Region list endpoint working")
        else:
            print("❌ Region list endpoint failed")
            return False
            
        # Test getting taxonomy
        taxonomy = make_ebird_request("ref/taxonomy/ebird", {"fmt": "json", "maxResults": 5})
        if taxonomy:
            print("✅ Taxonomy endpoint working")
        else:
            print("❌ Taxonomy endpoint failed")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ Endpoint test failed: {e}")
        return False

def main():
    """Main test function"""
    print("eBird MCP Server Test")
    print("=" * 30)
    
    # Test API connection
    if not test_api_connection():
        print("\n❌ Setup incomplete. Please check your API token.")
        sys.exit(1)
    
    # Test basic endpoints
    if not test_basic_endpoints():
        print("\n❌ Some endpoints are not working properly.")
        sys.exit(1)
    
    print("\n✅ All tests passed! Your eBird MCP server is ready to use.")
    print("\nNext steps:")
    print("1. Configure Claude Desktop to use this server")
    print("2. Restart Claude Desktop")
    print("3. Start a new conversation and ask about bird observations!")

if __name__ == "__main__":
    main() 