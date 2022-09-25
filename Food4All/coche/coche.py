class Coche:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        coche = self.session.get("coche")
        if not coche:
            coche = self.session["coche"]={}
        
        self.coche = coche
            
    def agregar (self,donan):
        if(str(donan.id) not in self.coche.keys()):
            self.coche[donan.id]={
                "donan_id": donan.id,
                "nombre": donan.nombre,
                "cantidad": 1,
                "imagen":donan.imagen.url
                
            }
        else:
            for key,value in self.coche.items():
                if key == str(donan.id):
                    value["cantidad"]= value["cantidad"]+1
                    break
        self.guardar_coche()
        
    def guardar_coche(self):
        self.session["coche"]= self.coche
        self.session.modified = True


    def eliminar(self,donan):
        donan.id=str(donan.id)
        if donan.id in self.coche:
            del self.coche[donan.id]
            self.guardar_coche()
    
    def restar_donan(self, donan):
        for key,value in self.coche.items():
            if key == str(donan.id):
                value["cantidad"]= value["cantidad"]-1
                if value["cantidad"]<1:
                    self.eliminar(donan)
                break
        self.guardar_coche()

    def limpiar_coche(self):
        self.session["coche"]={} 
        self.session.modified = True
        