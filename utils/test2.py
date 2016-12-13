import unirest

response = unirest.post("https://bmi.p.mashape.com/",
  headers={
    "X-Mashape-Key": "fs2VyXxGiZmshQ26lUFKNpzZ7zpMp1bMFSNjsnyr6gRbjidRYi",
    "Content-Type": "application/json",
    "Accept": "application/json"
  },
  params=("{\"weight\":{\"value\":\"85.00\",\"unit\":\"kg\"},\"height\":{\"value\":\"170.00\",\"unit\":\"cm\"},\"sex\":\"m\",\"age\":\"24\",\"waist\":\"34.00\",\"hip\":\"40.00\"}")
)

print response.body
