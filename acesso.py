##tipos de resposta
loginADM_M = ("Ola administrador")
loginADM_F = ("Ola administradora")

loginUSR_M = ("Ola usuario")
loginUSR_F = ("Ola usuaria")

loginGUEST = ("Ola visitante")

loginUNKW = ("Ola desconhecido")

##inputs
caixaEntradaCargo = str(input("Por favor informe o seu cargo: "))

caixaEntradaGenero = str(input("Por favor informe o seu genero: "))

##padronizando
caixaEntradaCargo = caixaEntradaCargo.upper()
caixaEntradaGenero = caixaEntradaGenero.upper()

##loops dos cargos
if caixaEntradaCargo == "ADM" and caixaEntradaGenero == "M":
    print (loginADM_M)
    
elif caixaEntradaCargo == "ADM" and caixaEntradaGenero == "F":
        print (loginADM_F)


if caixaEntradaCargo == "USR" and caixaEntradaGenero == "M":
    print (loginUSR_M)
    
elif caixaEntradaCargo == "USR" and caixaEntradaGenero == "F":
        print (loginUSR_F)

if caixaEntradaCargo == "GUEST" and caixaEntradaGenero == "M":
    print (loginGUEST)

elif caixaEntradaCargo == "GUEST" and caixaEntradaGenero == "F":
    print (loginGUEST)
    
if caixaEntradaCargo != "ADM" and caixaEntradaCargo != "USR" and caixaEntradaCargo != "GUEST":
    print (loginUNKW)