# MyEvent Voice Reminder Project

This project demonstrates the use of Twilio Voice API to send automated voice reminders to users about their scheduled events.

## Features

- Users voluntarily provide their phone number.
- Users can enter important events or appointments.
- The system makes an automated voice call to remind the user about the event.
- No promotional or bulk messages/calls are sent. Only personal reminders for registered users.

## How it Works

1. A user enters their phone number and event details.
2. Before the event, the system initiates a voice call using Twilio Voice API.
3. The call delivers a spoken reminder message.

## Example Usage

See `voice_reminder.py` for a working example using Twilio Voice API.

## References

- Twilio Voice API documentation: https://www.twilio.com/docs/voice
