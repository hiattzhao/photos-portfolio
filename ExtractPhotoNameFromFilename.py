import re

regex = re.compile(r"(\d{4})([a-zA-Z]+)(\d+)", re.I | re.DOTALL)

result = regex.findall(
    """
2002Tree50copy.jpg
2003Flagstaff060.jpg
2003Flagstaff147.jpg
2003Rochester3172.JPG
2003Seattle142.jpg
2004Ottowa109.jpg
2005NewYorkCity36.jpg
2005Rochester100copy.jpg
2006Chicago147.jpg
2011Birds11copy.jpg
2011Flowers020copy.jpg
2011Flowers139copy.jpg
2011Flowers209copy.jpg
2011Flowers217copy.jpg
2011Flowers251copy.jpg
2011Flowers268copy.jpg
2011Flowers297copy.jpg
2011Flowers331copy.jpg
2011Flowers344copy.jpg
2011Flowers379copy.jpg
2011HopeLn003copy.jpg
2011TrexlerPark22copy.jpg
2012Wescosville169copy.jpg
2013Anchorage177copy.jpg
2013Beijing1136copy.jpg
2013Carmel386copy.jpg
2013Carmel390copy.jpg
2013Carmel394copy.jpg
2013Juneau564copy.jpg
2013LosAngeles289copy.jpg
2013Monterey233copy.jpg
2013PacificGrove089copy.jpg
2014LakeGeorge87copy3.jpg
2014LakePlacid099copy.jpg
2014LakePlacid155copy2.jpg
2014Orlando094copy2.jpg
2014Orlando116copy2.jpg
2014StPetersburg249copy.jpg
2015AntelopeCanyon137copy.jpg
2015GrandCanyon032copy.jpg
2015NewYorkCity0995copy.jpg
2015Rochester196copy.jpg
2015SaltLakeCity014copy.jpg
2016BlueBell14.JPG
2016TrexlerNaturePreserve26.JPG
2017Moon39.jpg
2017NewYearsDay22copy.jpg
2017Tree081.jpg
2017WestOakLane021copy.jpg
2017WestOakLane029copy.jpg
2017WestOakLane046copy.jpg
2017WestOakLane072copy.jpg
2018Baker1733-edit.jpg
2018Baker1785-edit.jpg
2018Boulder2500-edit.jpg
2018BryceCanyon1472-edit.jpg
2018Fallon1988-edit.jpg
2018Fallon1998-edit2.jpg
2018Gardnerville2082-edit3.jpg
2018Lancaster0083-edited.jpg
2018Telluride2253-edit.jpg
2020Wayne053-edit.jpg
2021KingOfPrussia131.jpg
2022Flowers13-edit.jpg
2022KeyWest36-edit.jpg
2022Reading25-edit.jpg
2024Bantayan29-edit.jpg
2024ElNido87-edit.jpg
2024Phuket76-edit.jpg
2024PortBarton29-edit.jpg
2024PortBarton122-edit.jpg
2024Taipei305-edit.jpg
"""
)

filenamesList = []

for filename in result:
    filenamesList.append(filename[0] + " " + filename[1] + " " + filename[2])

print(filenamesList)
print("Total files: " + str(len(filenamesList)))
