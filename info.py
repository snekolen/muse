class Info():
      def __init__(self):
            self.allCountries = []
            self.topCountries = {}
            self.allDecades = []
            self.topDecades = {}
            self.allSongs = []
            self.topSongs = {}


      def get_allC(self):
            return self.allCountries
      
      def get_topC(self):
            return self.topCountries

      def set_allC(self, cArr):
            self.allCountries = cArr
      
      def set_topC(self, cDict):
            self.topCountries = cDict
      

      #Dicts for decades
      def get_allD(self):
            pass

      def get_topD(self):
            pass

      def set_allD(self, decade):
            pass

      def set_topD(self, dDict):
            pass

      #Dicts for songs
      def get_allS(self):
            pass
      
      def get_topS(self):
            pass
      
      def set_allS(self, song, author, country, year):
            pass

      def set_topS(self, sDict):
            pass

s = Info()

def updateAllC(country): #Returns dict
      cArr = s.get_allC()
      if len(cArr) == 0:
            c = {"Country": country, "Count": 1}
            cArr.append(c)
      else:
            found = False
            for d in cArr:
                  if d["Country"] == country:
                        d["Count"] += 1
                        found = True
                        break
            if found == False:
                  c = {"Country": country, "Count": 1}
                  cArr.append(c)
      s.set_allC(cArr)

def updateTopC(country):
      cArr = s.get_allC()
      cDict = s.get_topC()
      c = None
      
      for d in cArr:
            if d["Country"] == country:
                  c = d
                  break

      if len(cDict) == 0:
            cDict["1"] = d
      elif len(cDict) == 1:
            if c["Count"] >= cDict["1"]["Count"] and c["Country"] != cDict["1"]["Country"]:
                  cDict["2"] = cDict["1"]
                  cDict["1"] = c
            elif c["Country"] != cDict["1"]["Country"]:
                  cDict["2"] = c
      elif len(cDict) == 2:
            if c["Country"] != cDict["1"]["Country"] and c["Country"] != cDict["2"]["Country"]: #If country is not in top list
                  if c["Count"] >= cDict["1"]["Count"]:
                        cDict["3"] = cDict["2"]
                        cDict["2"] = cDict["1"]
                        cDict["1"] = c
                  elif c["Count"] >= cDict["2"]["Count"]:
                        cDict["3"] = cDict["2"]
                        cDict["2"] = c
                  else:
                        cDict["3"] = c
            elif c["Country"] == cDict["2"]["Country"] and c["Count"] >= cDict["1"]["Count"]: #If 2nd most searched country is more or 
                  sec = cDict["2"]
                  cDict["2"] = cDict["1"]
                  cDict["1"] = sec
      elif len(cDict) == 3: #When top 3 is full
            if c["Country"] == cDict["1"]["Country"]:
                  pass
            elif c["Country"] == cDict["2"]["Country"]: #If country is the 2nd one
                  if c["Count"] >= cDict["1"]["Count"]:
                        sec = cDict["2"]
                        cDict["2"] = cDict["1"]
                        cDict["1"] = sec
            elif c["Country"] == cDict["3"]["Country"]: #If country is the 3rd one
                  if c["Count"] >= cDict["1"]["Count"]:
                        cDict["3"] = cDict["2"]
                        cDict["2"] = cDict["1"]
                        cDict["1"] = c
                  elif c["Count"] >= cDict["2"]["Count"]: 
                        third = cDict["3"]
                        cDict["3"] = cDict["2"]
                        cDict["2"] = third
            elif c["Country"] != cDict["1"]["Country"] or c["Country"] != cDict["2"]["Country"] or c["Country"] != cDict["3"]["Country"]: #If country is not in cDict
                  if c["Count"] >= cDict["1"]["Count"]:
                        cDict["3"] = cDict["2"]
                        cDict["2"] = cDict["1"]
                        cDict["1"] = c
                  elif c["Count"] >= cDict["2"]["Count"]: 
                        cDict["3"] = cDict["2"]
                        cDict["2"] = c
                  elif c["Count"] >= cDict["3"]["Count"]: 
                        cDict["3"] = c
      s.set_topC(cDict)
      #Get dict with country in it by going through cArr

#Top decades
def updateAllD(decade):
      pass

def updateTopD(decade):
      pass

#Top songs
def updateAllS(title, author, country):
      pass

def updateTopS(title, author, country):
      pass

