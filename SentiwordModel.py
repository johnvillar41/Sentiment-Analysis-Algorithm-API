import json


class SentiwordModel:
    def __init__(self, polarityScore, sentimentScore):
        self.polarityScore = polarityScore             
        self.sentimentScore = sentimentScore

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
