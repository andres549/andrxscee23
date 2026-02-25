print ("==================================================")
print ("=       BIENVENIDOS A  RIWITECHSTORE             =")
print ("=       UBICACION: BARRANQUILLA-COLOMBIA         =")
print ("=          CORREO : RIWISTORE@GMAIL.COM          =")
print ("==================================================")
cliente =input ("nombre del cliente :")
precio =input ("precio del producto :")
cantidad =input ("cantidad de productos :")
vip =input ("eres vip si/no? :")

cantidad =   float(cantidad)
precio = float (precio)
if vip == "si":
  vip = True
else:
 vip = False
descuento =0.10
subtotal = cantidad*precio
if (vip):
 total = subtotal - (subtotal*descuento)
else:
 total = subtotal
 print (" =======================")
 print (" = RECIBO DE SU COMPRA =")
 print (" =                     =")
 print (f"= Nombre: {cliente}   =" )
 print (f" subtotal {subtotal}")
if (vip):
 print("DESCUENTO APLICADO")
 print (f"total a pagar $:{total}")