#Nama : Ghufron Malik
#NIM  : 312210559

#                               HAPUS TANDA "#" UNTUK MENJALANKAN PROGRAM                                   #

#def KelvinToFahrenheit(Temperature):
#    assert (Temperature >= 0),"Colder than absolute zerol!"
#    return ((Temperature-273)*1.8)+32
#print(KelvinToFahrenheit(273))
#print(int(KelvinToFahrenheit(505.78)))
#print(KelvinToFahrenheit(-5))


#try:
#    fh = open("testfile", "w")
#    fh.write("Ini adalah file test untuk menguji exception handling!!")
#except IOError:
#    print ("Error: tidak bisa menemukan file atau membaca data")
#else:
#    print ("Penulisan isi didalam file berhasil dilakukan")
#    fh.close()


#try:
#    fh = open("testfile", "r")
#    fh.write("Ini adalah file test untuk menguji exception handling!!")
#except IOError:
#    print ("Error: tidak bisa menemukan file atau membaca data")
#else:
#    print ("Penulisan isi didalam file berhasil dilakukan")


#try:
#    fh = open("testfile", "w")
#    fh.write("Ini adalah file test untuk menguji exception handling!!")
#finally:
#    print("Error: tidak dapat menemukan data atau membaca data")


#try:
#    fh = open("testfile","w")
#    try:
#        fh.write("Ini adalah file test untuk menguji exception handling!!")
#    finally:
#        print("Akan menutup file")
#        fh.close()
#except IOError:
#    print("Error: tidak dapat menemukan data atau membaca data")


# Definisikan sebuah fungsi disini.
#def temp_convert(var):
#    try:
#        return int(var)
#    except ValueError as Argument :
#        print("Argument tidak berisi nomer-nomer\n", Argument)
# Memanggil lagi fungsi disini.
#temp_convert("xyz");


#def functionNmae(level):
#    if level < 1:
#        raise ("Invalid level!, level")
#    print(raise)
    # kode dibawah ini tidak akan di eksekusi
    # jika kita munculkan sebuah pengecualian.


#class Networkerror(RuntimeError):
#   def __init__(self, arg):
#      self.args = arg


#try:
#   raise Networkerror("Bad hostname")
#except Networkerror,e:
#   print (e.args)