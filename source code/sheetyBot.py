import requests


class uploaderBot:
    def __init__(self, areaList, ownerList, amountList,sheetyEndpoint):
        self.areaList = areaList
        self.ownerList = ownerList
        self.amountList = amountList
        self.endpoint = sheetyEndpoint
        self.head = {
            "Authorization": "Basic bnVsbDpudWxs",
        }

    def initiateUploading(self):
        print(self.endpoint)

        for x in range(0, len(self.areaList) - 1):
            try:
                agentName = self.ownerList[x].text
            except:
                agentName = 'N A'

            data = {
                "sheet1": {
                    "area": self.areaList[x].text,
                    "owner/agent": agentName,
                    "rent": self.amountList[x].text,
                }
            }
            print(data)
            response = requests.post(url=self.endpoint, json=data)
            response.raise_for_status()
