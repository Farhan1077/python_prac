# You are given a list of user activity records.
# Each record is represented as a tuple:

# (user_id: int, username: str, activities: List[str])

# Your task

# Process the data and return a dictionary with the following details:

# Output Dictionary Requirements

# "unique_users" → a set of all unique usernames

# "activity_count" → a dictionary where keys are activities (string) and values are how many times they occurred across all users

# "user_activity_map" → a dictionary mapping each username to a sorted list of their unique activities

# # "most_active_user" → the username (string) who performed the highest number of total activities

from typing import List, Tuple, Dict, Any   
def process_user_activity(records: List[Tuple[int, str, List[str]]]) -> Dict[str, Any]:
    unique_users = set()
    activity_count = {}
    user_activity_map = {}
    user_total_activities = {}

    for user_id, username, activities in records:
        unique_users.add(username)
        
        if username not in user_activity_map:
            user_activity_map[username] = set()
            user_total_activities[username] = 0
        
        for activity in activities:
            # Count activity occurrences
            if activity in activity_count:
                activity_count[activity] += 1
            else:
                activity_count[activity] = 1
            
            # Map user to their unique activities
            user_activity_map[username].add(activity)
            user_total_activities[username] += 1

    # Convert sets to sorted lists in user_activity_map
    for username in user_activity_map:
        user_activity_map[username] = sorted(user_activity_map[username])
    
    # Determine the most active user
    most_active_user = max(user_total_activities, key=user_total_activities.get)

    return {
        "unique_users": unique_users,
        "activity_count": activity_count,
        "user_activity_map": user_activity_map,
        "most_active_user": most_active_user
    }