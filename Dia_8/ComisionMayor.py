import json

archivito= open('Dates.json')
miJson= json.load(archivito)

def Comi_mayor(comercial):
    return comercial['comisión']
comisionsita= (miJson['ventas'] ['comerciales'])
comisiónM= sorted(comisionsita, key=Comi_mayor, reverse=True)
print(comisiónM[0],comisiónM[1]) 
