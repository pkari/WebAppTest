# Twitch Selenium Test

This is an E2E test project with Selenium, created by Karoly Puskas

## Demo

![Demo GIF](twitch_demo.gif)

## Structure

WebAppTest/
├── helpers/
│   └── web_element_helper.py     # Helper functions for web elements
├── pages/
│   ├── streamer_page.py          # Page object for the streamer page
│   └── twitch_page.py            # Page object for the Twitch page
├── screenshots/                  # Screenshots captured during tests
├── tests/
│   └── test_twitch_mobile.py     # Test script for Twitch mobile functionality
├── conftest.py                   # Pytest configuration and fixtures
├── readme.md                     # Project documentation
└── twitch_demo.gif               # Demo GIF showing test execution or app behavior