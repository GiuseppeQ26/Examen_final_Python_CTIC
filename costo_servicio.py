import argparse
import sys

def main():
   parser = argparse.ArgumentParser()
   parser.add_argument('--animal', type = str, default = 'NULL', help = 'Tipo de animal para el tratamiento')
   parser.add_argument('--tratamiento', type = str, default = 'NULL', help = 'Tipo de tratamiento o servicio')
   args = parser.parse_args()
   sys.stdout.write(str(costo_tratamiento(args)))

def costo_tratamiento(args):
   if args.tratamiento == 'corte de pelo':
     if args.animal == 'gato':
       costo = 20
     elif args.animal == 'perro':
       costo = 30
     elif args.animal == 'conejo':
       costo = 15
     else:
       print(f'Tratamiento no disponible para {args.animal}')

   elif args.tratamiento == 'baño':
     if args.animal == 'gato':
       costo = 15
     elif args.animal == 'perro':
       costo = 20
     elif args.animal == 'conejo':
       costo = 10
     else:
       print(f'Tratamiento no disponible para {args.animal}')

   elif args.tratamiento == 'desparasitación':
     if args.animal == 'gato':
       costo = 35
     elif args.animal == 'perro':
       costo = 50
     elif args.animal == 'conejo':
       costo = 25
     else:
       print(f'Tratamiento no disponible para {args.animal}')
    
   else:
      print(f'El tratamiento {args.tratamiento} no esta disponible')
   
   return f'El costo de {args.tratamiento} para un {args.animal} es de {costo}'


if __name__ == '__main__':
   main()