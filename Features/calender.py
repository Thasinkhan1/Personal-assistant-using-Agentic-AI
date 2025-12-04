from __future__ import print_function
import datetime
import os.path
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from langchain.tools import tool


SCOPES = ["https://www.googleapis.com/auth/calendar"]

def get_calendar_service():
    creds = None
    
    if os.path.exists("Features\tokens.json"):
        creds = Credentials.from_authorized_user_file("Features\tokens.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("Features\credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("Features\tokens.json", "w") as token:
            token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)
    return service


# print(get_calendar_service()) working fine

def get_today_events():
    service = get_calendar_service()
    now = datetime.datetime.utcnow().isoformat() + "Z"
    end = (datetime.datetime.utcnow() + datetime.timedelta(hours=24)).isoformat() + "Z"

    events_result = service.events().list(
        calendarId="primary", timeMin=now, timeMax=end,
        maxResults=20, singleEvents=True, orderBy="startTime"
    ).execute()

    events = events_result.get("items", [])
    if not events:
        return "You have no events today."

    response = "Here are your events for today:\n"
    for event in events:
        time = event["start"].get("dateTime", event["start"].get("date"))
        response += f"- {event['summary']} at {time}\n"
    return response

# print(get_today_events()) working fine

def create_event(summary, date, start_time, end_time):
    service = get_calendar_service()

    event = {
        "summary": summary,
        "start": {
            "dateTime": f"{date}T{start_time}:00",
            "timeZone": "Asia/Kolkata",
        },
        "end": {
            "dateTime": f"{date}T{end_time}:00",
            "timeZone": "Asia/Kolkata",
        },
    }

    event_result = service.events().insert(
        calendarId="primary", body=event
    ).execute()

    return f"Event created: {event_result.get('htmlLink')}"


# if __name__ == "__main__":
#     print(create_event(
#         summary="Meeting with Aman",
#         date="2025-02-01",
#         start_time="15:00",
#         end_time="16:00"
#     )) tested working fine till here




@tool
def check_calendar_today():
    "Returns today's calendar events"
    return get_today_events()

@tool
def add_calendar_event(data: str):
    """
    Add an event to calendar.
    Format: 'Meeting with Aman | 2025-12-10 | 15:00 | 16:00'
    """
    summary, date, start, end = [i.strip() for i in data.split("|")]
    return create_event(summary, date, start, end)
