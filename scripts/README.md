# Lahman Data Ingestion for Python/ML Predictions

Run `python ingest_lahman.py` to download the full Lahman database from the repo zip and load **all core tables** into `lahman.db` (SQLite).

This makes historical player, team, batting, pitching, etc. data instantly queryable for your +EV betting models or any predictions.

After running:
- Use pandas + sqlite3 for analysis
- Integrate directly into mlb-ev-framework
- Add features like career stats, WAR proxies, etc. for ML models

Data updated via the zip in this repo (2025+ edition). Re-run periodically if needed.

Tables loaded: AllstarFull, Appearances, Batting, Pitching, People, Teams, Salaries, etc.
