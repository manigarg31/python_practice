import requests
import sys

class status(object):
    OK=0
    WARNING=1
    CRITICAL=2
    UNKNOWN=3

def query_url(URL):
    response = requests.get(URL)
    return response.json()

def check_status(get_response,warning,critical):
    exit_status= status.UNKNOWN
    for i in get_response:
        for datapoint in i['datapoints']:
            if datapoint[0] is None:
                exit_status= status.UNKNOWN
            elif datapoint[0] >= critical:
                exit_status= status.CRITICAL
            elif datapoint[0] >= warning:
                exit_status= status.WARNING
            else:
                exit_status= status.OK
    return exit_status


if __name__ == "__main__":
    #print(sys.argv[0])
    URL= "https://play.grafana.org/api/datasources/proxy/1/render?target=aliasByNode(movingAverage(scaleToSeconds(apps.fakesite.*.counters.requests.count,%201),%202),%202)&format=json&from=-5min"
    get_response = query_url(URL)
    status = check_status(get_response, float(sys.argv[1]), float(sys.argv[2]))
    print("Exited with status: {}".format(status))
    sys.exit(status)
