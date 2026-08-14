# FishTech Final Report

## Milestone 8: Final Report Submission

## Project Title
FishTech

## Team Members
- Jackie Luu
- Mason Chansamone
- Geraldine Casaas

## Required Links

- Project tracker (instructor can access): 
- Version control repository (instructors have access): https://github.com/geca8469/FishTech/tree/main
- 5-minute customer demo video: https://cuboulder.zoom.us/rec/share/PB9NolGxH5JKEzNmLygQDeeeYTZJdplwvFpgnxuBF_TQ2ExWeLr4GjGLw6O8wyBV.DswBhEYwpfOr3mxf
- Zoom Passcode: 5qYL1yJ
- Public deployment site: https://fishtech.onrender.com/

## Repository Readiness

All team members have verified that their latest work is pushed to the remote repository.

The repository contains the following required files and assets:

- README.md
- WEEKLY_STATUS.md
- PAGE_TESTING.md
- SQL_TESTING.md
- FINAL_REPORT.md
- Project presentation files from the Presentation Milestone
- Video of demo
- Source code (frontend and backend)
- Test cases (unit and integration)
- Source documentation and auto-generated documentation files

## Final Status Report

### What We Completed
- Working MVP including:
  - User authentication/log in page
  - Interactive map with location and information feature, including deep links from a selected water body into its fish on the Fish Collection page
  - Fish information database
- Server-rendered Flask/Jinja2 frontend with a consistent navigation flow
- PostgreSQL database with a relational schema
- Public deployment of the application
- Project presentation slides and a customer-facing demo video

### What We Were in the Middle of Implementing
- Search/filtering on the "Explore Fish" page (by name, water type, habitat)
- UI polish and accessibility pass

### What We Planned for the Future
- Habitat builder for users to be matched with their ideal habitat
- User features such as favoriting or saving fish and habitats (the `UserFavorites` and `UserSetting` tables already exist in the schema but have no routes/UI yet)
- Expand database for fish and habitats
- Password hashing and a non-hardcoded Flask secret key before handling real user credentials

### Known Problems and Limitations
- **Passwords are stored and compared in plaintext** 
- `app.secret_key` in `app.py` is a hardcoded literal (`'a secret key'`) rather than an environment-provided secret.
- Several unauthenticated developer/testing routes are still registered in `app.py` and are reachable on the public deployment by anyone who finds the URL.
- The navbar's "Build" link points to a static `habitat-builder.html` page that doesn't exist yet, so it 404s.
- Fish search/filtering by name, water type, or habitat (specified in `PAGE_TESTING.md`) isn't implemented — `/fish-collection` always returns the full list.

## System Overview

FishTech is a single Flask service with a server-rendered frontend:

- **Backend (`app.py`)** — Flask routes for each page (`/`, `/fish-collection`, `/map`, `/login`, `/create_account`, `/logout`) plus a small JSON API, `/api/waterbody/<id>/fish`

- **Data access (`db.py`)** — A thin layer over `psycopg2`. Each function opens its own connection, runs a parameterized query, and closes the connection.

- **Database** — PostgreSQL, schema defined in `schema.sql` (`Users`, `Fish`, `WaterBody`, `FishCondition`, `WaterCondition`, `UserFavorites`, `UserSetting`, `WaterBodyFish`). Local setup is scripted by `setup_db.sh`; sample data comes from `seed.sql`.

- **Frontend** — Server-rendered Jinja2 templates a `navbar.html`, styled by one stylesheet (`static/css/style.css`). The Interactive Map is the one page with real client-side JS (`static/js/map.js`): 

- **Deployment** — Hosted on Render at the public URL above, configured via environment variables rather than a committed `.env` file.

## Pages That Access Database Information

- Login: users
- Fish collection: fish, preferred conditions 
- Interactive Map: fish, water bodies

## Page Data Access Tests (High-Level)

### Use case name
Fish Collection page loads fish from the database

### Description
Verify that `/fish-collection` queries the `Fish` table and renders one card per fish, each with a stable anchor the map page can deep-link to.

### Pre-conditions
Database is seeded (`seed.sql`); 5 fish exist in the `Fish` table.

### Test steps
1. Send `GET /fish-collection`.
2. Count the number of `fish-card` elements in the response.
3. Confirm each card has an `id="fish-<FishID>"` anchor.

### Expected result
HTTP 200; exactly 5 fish cards rendered, each with a `fish-<id>` anchor.

### Actual result
HTTP 200; 5 fish cards rendered, each with the expected `fish-<id>` anchor. Pass.

### Status
Pass (verified via Flask test client against the local seeded database)

### Notes
This test was run earlier in development, not re-run for this report — re-verify before final submission.

### Post-conditions
No state change; read-only test.

---

### Use case name
Interactive Map links a water body to its fish

### Description
Verify that selecting a water body on `/map` returns the correct fish for that location via `/api/waterbody/<id>/fish`, using the `WaterBodyFish` join table.

### Pre-conditions
Database is seeded; `WaterBodyFish` links Lake Michigan (id 1) to Largemouth Bass and Channel Catfish, and Boulder Creek (id 2) to Rainbow Trout and Bluegill.

### Test steps
1. Send `GET /map` and confirm it renders.
2. Send `GET /api/waterbody/1/fish`.
3. Send `GET /api/waterbody/2/fish`.
4. Compare the returned fish names against the `WaterBodyFish` seed data.

### Expected result
`/map` returns HTTP 200. Waterbody 1 returns Largemouth Bass and Channel Catfish; waterbody 2 returns Rainbow Trout and Bluegill.

### Actual result
`/map` returned HTTP 200. Waterbody 1 returned Largemouth Bass and Channel Catfish; waterbody 2 returned Rainbow Trout and Bluegill — matching the seed data exactly. Pass.

### Status
Pass (verified via Flask test client against the local seeded database)

### Post-conditions
No state change; read-only test.

## Reflection

Our team members were quite busy, so it was for everyone to commit time to the project, all non-technical work was smooth, but actually building it out was difficult due to the low amount of interaction between the team member throughout the project.

Our biggest win on this project was the pre-planning. We built out our schema and the vision for the project really early on, so when we finally started implemented features and building out the app, there wasn't any design issues we had to reconciliate when we got there. 

If we had more time to work on this project, building out the database more would allow us to showcase the features better as well as more time designing the UI/UX would benefit. Overall for the composition of our team, I think we did a pretty good job. 



