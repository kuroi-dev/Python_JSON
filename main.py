import json
import collections.abc

def leer_json(ruta):
    with open(ruta ,"r") as contenido:
        datas = json.load(contenido)

        for data3,data4 in datas.items():

            if isinstance(data4, collections.abc.Sequence) == True:
                print(data3 + " : " + data4)
            else:
                for data5 , data6  in data4.items():

                    if isinstance(data6, collections.abc.Sequence) == True:
                        print(data3 + "_"+data5+" : "+ data6)

                    else:
                        try:
                            if float(data6).is_integer():
                                print( data3 + "_"+data5+" : "+ str(data6))
                        except:
                            for data7, data8 in data6.items():
                                for data9, data10 in data8.items():
                                    print(data3 + "_"+data5+"_"+data7+"_"+data9+" : "+ data10)

if __name__ == "__main__":
    ruta = "datos.json"
    leer_json(ruta)
