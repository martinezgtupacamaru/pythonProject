provinces={"QC":"Quebec","ON":"Ontario"}

##This one fails if QC not found, sometimes its good to fail (!!)
#Anytime you use and index you need to use []
print(provinces["QC"])

##This one gives nothing if QC is not found
#Here we are using a get function, so use ()
print(provinces.get("QC"))

#if find nothing, give back N/A
print(provinces.get("BC", "N/A"))

