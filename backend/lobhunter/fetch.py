from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import time
import os
import base64
from pprint import pprint

# Define the scopes required for accessing Gmail
SCOPES = ["https://mail.google.com/"]


# def authenticate_gmail():
#     creds = None
#     # Load credentials from file if available
#     if os.path.exists("token.json"):
#         creds = Credentials.from_authorized_user_file("token.json", SCOPES)
#     # If credentials are invalid, re-authenticate
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for future use
#         with open("token.json", "w") as token:
#             token.write(creds.to_json())
#     return creds

def authenticate_gmail():
    creds = None
    # Load credentials from file if available
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If credentials are invalid, re-authenticate
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for future use
    creds.refresh(Request())
    with open("token.json", "w") as token:
        token.write(creds.to_json())
    return creds


def fetcher():
    creds = authenticate_gmail()
    service = build("gmail", "v1", credentials=creds)
    result = service.users().messages().list(userId="me", labelIds=["INBOX"]).execute()
    messages = result.get("messages")
    all_messages = []
    if not messages:
        return all_messages
    for idx, msg in enumerate(messages):
        txt = service.users().messages().get(userId="me", id=msg["id"]).execute()
        email_id = txt["id"]
        payload = txt["payload"]
        # print(payload["body"])
        if int(payload["body"]["size"]) == 0:
            continue
        data = payload["body"]["data"]
        data = data.replace("-", "+").replace("_", "/")
        decoded_data = base64.b64decode(data).decode("utf-8")
        all_messages.append({"email_id": email_id, "data": decoded_data})
        print(f"Added {idx} messages for commit")
        # Move the message to trash
        service.users().messages().trash(userId="me", id=email_id).execute()
    print("Finished Sync")
    return all_messages if all_messages else []
