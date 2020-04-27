import requests
import json





class Covid():

    URL = "https://covidtracking.com/api/v1/"

    def __init__(self, state=None):
        self.state = state

    def stateResults(self, states):
        pyInput = input("Enter a date (ex: 04/19/2020): ")
        formattedDateArray = pyInput.split("/")
        finalFormatted = formattedDateArray[2] + formattedDateArray[0] + formattedDateArray[1]
        resp = requests.get(Covid.URL + "states/" + states +"/daily.json")
        data = resp.json()
        for i in range(len(data)):
            if(data[i]['date'] == int(finalFormatted)):
                print("For date: " + pyInput)
                print("State: " + str(data[i]['state']))
                print("Positive Tests: " + str(data[i]['positive']))
                print("Negative Tests: " + str(data[i]['negative']))
                print("Number hospitalized on this date: " + str(data[i]['hospitalizedCurrently']))
                print("Total test results: " + str(data[i]['totalTestResults']))

    def stateInfo(self, states):
        resp = requests.get(Covid.URL + "states/info.json")
        data = resp.json()
        for i in range(len(data)):
            if(data[i]['state'] == states):
                print("For state: " + data[i]['name'])
                print("COVID-19 Resources: " + data[i]['covid19Site'])

    def today(self, states):
        resp = requests.get(Covid.URL + "us/current.json")
        data = resp.json()
        print("Positive Tests: " + str(data[0]['positive']))
        print("Negative Tests: " + str(data[0]['negative']))
        print("Number hospitalized: " + str(data[0]['hospitalizedCurrently']))
        print("Recovered: " + str(data[0]['recovered']))
