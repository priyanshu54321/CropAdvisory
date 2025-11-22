# Farmer-Friendly Crop Advisory System

## Overview

This is a web-based agricultural advisory platform designed to empower Indian farmers with data-driven insights for better farming decisions. The system provides multilingual support (English, Hindi, Marathi, Bengali, Telugu, Punjabi) and covers crop recommendations, weather forecasts, market prices, fertilizer guidance, government schemes, and a community forum. The application targets small to medium-scale farmers across India, making agricultural knowledge accessible through a simple, localized interface.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Technology Stack:**
- Pure HTML/CSS/JavaScript (no framework dependencies)
- Font Awesome for icons
- Google Fonts for multilingual typography (Poppins, Noto Sans Devanagari, Noto Sans Bengali, etc.)
- Responsive design with CSS Grid and Flexbox

**Design Decisions:**

1. **Multilingual Support**: Client-side translation system using key-value mapping in JavaScript
   - **Problem Addressed**: Making agricultural information accessible to farmers across different Indian language regions
   - **Solution**: Language selector in header that dynamically updates UI text based on selected language
   - **Pros**: No server-side overhead, instant language switching, reduced API calls
   - **Cons**: Requires maintaining translation files, initial page load includes all translations

2. **Static Asset Delivery**: All frontend assets served from `/static` directory
   - **Problem Addressed**: Efficient resource delivery and caching
   - **Pros**: Simple deployment, CDN-ready, browser caching support
   - **Cons**: No build optimization or bundling

3. **Component-Based UI**: Logical sections (header, hero, dashboard cards, modals) without framework
   - **Pros**: Lightweight, fast loading, no build process
   - **Cons**: Manual DOM manipulation, no built-in state management

### Backend Architecture

**Technology Stack:**
- Flask (Python web framework)
- Flask-CORS for cross-origin resource sharing
- Flask-JWT-Extended for token-based authentication
- Werkzeug for password hashing
- GeoPy for geocoding and location services
- SQLAlchemy ORM for database operations

**Design Decisions:**

1. **Monolithic Flask Application**: Single `app.py` contains all routes and business logic
   - **Problem Addressed**: Rapid development and deployment for MVP
   - **Chosen Solution**: Keep all routes in one file for simplicity
   - **Pros**: Easy to understand, minimal setup, quick prototyping
   - **Cons**: May become difficult to maintain as features grow, tight coupling

2. **JWT-Based Authentication**: Stateless authentication using JSON Web Tokens
   - **Problem Addressed**: Secure user authentication without session storage
   - **Solution**: Flask-JWT-Extended with 7-day token expiration
   - **Pros**: Scalable, stateless, mobile-friendly
   - **Cons**: Token revocation requires additional implementation

3. **RESTful API Design**: `/api/*` endpoints for all data operations
   - **Problem Addressed**: Separation of concerns between frontend and backend
   - **Pros**: Clear API contract, frontend-agnostic, testable
   - **Cons**: Additional HTTP overhead compared to server-side rendering

### Data Storage

**Technology Stack:**
- SQLite for persistent storage
- SQLAlchemy ORM for database abstraction

**Database Schema:**

1. **Users Table**: Stores user authentication data
   - Fields: id, username, password (hashed), created_at
   - Relationships: One-to-many with forum posts and answers

2. **Forum Posts Table**: Community discussion threads
   - Fields: id, author (FK to users), title, content, created_at
   - Relationships: One-to-many with forum answers

3. **Forum Answers Table**: Responses to forum posts
   - Fields: id, post_id (FK), author (FK to users), content, created_at
   - Relationships: Many-to-one with forum posts and users

**Design Decisions:**

1. **SQLite Database**: File-based relational database
   - **Problem Addressed**: Need for persistent storage without complex database setup
   - **Chosen Solution**: SQLite with SQLAlchemy ORM
   - **Pros**: Zero configuration, file-based, good for development and small-scale deployment
   - **Cons**: Limited concurrent writes, not suitable for high-traffic production, no network access
   - **Note**: Should migrate to PostgreSQL for production deployment

2. **JSON Data Files**: Static agricultural data stored as JSON
   - **Files**: crops.json, fertilizer.json, market_prices.json, schemes.json
   - **Problem Addressed**: Quick access to reference data without database queries
   - **Pros**: Easy to update, version controllable, multilingual support
   - **Cons**: No relational integrity, manual updates required, loaded into memory

### Authentication & Security

**Design Decisions:**

1. **Password Hashing**: Werkzeug's password hashing utilities
   - **Problem Addressed**: Secure password storage
   - **Solution**: Generate and verify password hashes using industry-standard algorithms
   - **Pros**: Built-in, tested, secure
   - **Cons**: None significant

2. **JWT Secret Key**: Environment variable or fallback default
   - **Problem Addressed**: Secure token signing
   - **Configuration**: Uses `SESSION_SECRET` environment variable or default key
   - **Note**: Should always use environment variable in production

## External Dependencies

### Third-Party APIs

1. **OpenWeather API**
   - **Purpose**: Real-time weather forecasts and conditions
   - **Configuration**: Requires `OPENWEATHER_API_KEY` environment variable
   - **Usage**: Location-based weather data for farming decisions
   - **Endpoints Used**: Weather forecast API

2. **GeoPy/Nominatim**
   - **Purpose**: Geocoding and reverse geocoding services
   - **Usage**: Convert user locations to coordinates for weather and crop recommendations
   - **Note**: Free service with rate limits

### Python Dependencies

**Core Framework:**
- Flask: Web application framework
- Flask-CORS: Cross-origin resource sharing
- Flask-JWT-Extended: JWT authentication

**Database:**
- SQLAlchemy: ORM for database operations
- sqlite3: Database engine (Python standard library)

**Security:**
- Werkzeug: Password hashing utilities

**External Services:**
- GeoPy: Geocoding services
- Requests: HTTP client for API calls

### Frontend Dependencies (CDN)

1. **Font Awesome 6.4.0**: Icon library
2. **Google Fonts**: Multilingual typography support
   - Poppins (English)
   - Noto Sans Devanagari (Hindi)
   - Noto Sans Bengali (Bengali)
   - Additional Noto Sans variants for regional languages

### Environment Variables

Required for full functionality:
- `SESSION_SECRET`: JWT signing key (required for production)
- `OPENWEATHER_API_KEY`: Weather API access (optional, degrades gracefully)

### File System Dependencies

- `/data/` directory: Stores JSON reference data files
- `/static/` directory: Frontend assets (HTML, CSS, JS)
- `farmer_advisory.db`: SQLite database file (auto-created)