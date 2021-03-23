# Getting Started with Python app for formatting the Restaurant “Opening Hours”

To get started, we'll build a Python-flask app which helps to format the input JSON-formatted opening hours of a restaurant
as an input payload and outputs hours in more human-readable format with response as Output JSON.

## Prerequisites

You'll need the following:
* [Flask]
* [Python]


## 1. Clone the sample app

You can clone the project from [Git repo].
   ```

  ```

## 2. Run the app locally

First, you have to install the dependencies listed in the [requirements.txt]to run it locally.

I prefer using a virtual environment [virtual environment] to avoid my dependencies clash with those of my other Python projects.
  ```
pip install -r requirements.txt
  ```

Run the app.
  ```
python app.py
  ```

View your app at:
  ``` 
http://127.0.0.1:5000/open-time-stamp-conversion/
  ```

## 3. List of routes mentioned in the app

Below i have mentioned the list of routes used in the app:
* [http://127.0.0.1:5000/open-time-stamp-conversion/](as the name suggests we can provide input payload as raw JSON and get formatted human-readable times)

INPUT JSON:
```
{
 "monday" : [],
 "tuesday" : [
 {
 "type" : "open",
 "value" : 36000
 },
 {
 "type" : "close",
 "value" : 64800
 }
 ],
 "wednesday" : [],
 "thursday" : [
 {
 "type" : "open",
 "value" : 36000
 },
 {
 "type" : "close",
 "value" : 64800
 }
 ],
 "friday" : [
 {
 "type" : "open",
 "value" : 36000
 },
 {
 "type" : "close",
 "value" : 3600
 }],
 "saturday" : [
 {
 "type" : "close",
 "value" : 3600
 },
 {
 "type" : "open",
 "value" : 36000
 }
 ],
 "sunday" : [

 {
 "type" : "open",
 "value" : 43200
 },
 {
 "type" : "close",
 "value" : 75600
 }
 ]
 }

  ``` 

RESPONSE JSON (human-readable time format):
  ```
{
    "friday": [
        "Open 10:00:00 AM",
        "Closed 01:00:00 AM"
    ],
    "monday": [
        "Closed"
    ],
    "saturday": [
        "Closed 01:00:00 AM",
        "Open 10:00:00 AM"
    ],
    "sunday": [
        "Open 12:00:00 PM",
        "Closed 09:00:00 PM"
    ],
    "thursday": [
        "Open 10:00:00 AM",
        "Closed 06:00:00 PM"
    ],
    "tuesday": [
        "Open 10:00:00 AM",
        "Closed 06:00:00 PM"
    ],
    "wednesday": [
        "Closed"
    ]
}
  ```