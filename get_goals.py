import soccerdata as sd
import pandas as pd
import time

print("FBref se saare 380 matches ka data nikaal rahe hain...")

fbref = sd.FBref(leagues=['ENG-Premier League'], seasons=['2025'])

# Schedule nikaalein (saare matches ki list)
schedule = fbref.read_schedule()
match_ids = schedule['game_id'].tolist()
print(f"Total matches: {len(match_ids)}")

all_events = []

# Ek-ek match ka data nikaalein
for i, match_id in enumerate(match_ids):
    print(f"Match {i+1}/{len(match_ids)}: {match_id}")
    try:
        events = fbref.read_events(match_id=match_id)
        all_events.append(events)
        time.sleep(1)  # 1 second ka break
    except Exception as e:
        print(f"Error on match {match_id}: {e}")
        continue

# Saara data combine karein
if all_events:
    combined = pd.concat(all_events)
    combined.to_csv('premier_league_2025_26_events.csv')
    print(f"Done! {len(combined)} events saved to premier_league_2025_26_events.csv")
else:
    print("Koi data nahi mila.")