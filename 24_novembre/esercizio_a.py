# Apro e Leggo il file, Linea per Linea
my_file = open('shampoo_sales.csv','r')  

def sum_csv(file_nella_funzione):

#creo chart list da usare nel not in 
    chart_list=["Date","Sales"]
    somma=0 #sommare la lista con la funzione append 

    for line in file_nella_funzione:

        # Faccio lo split di ogni riga sulla virgola
        elements = line.split(',') #elements: una lista che contine 2 elementi (1 linea del file)
        
        # Se NON sto processando L'intestazione...
        if elements[0] != 'Date':                                          
            somma+= float(elements[1]) #float() funzione che trasforma in float 

    return somma

somma=sum_csv(my_file)
print("Risultato:{}" .format(somma))