def extractName(name ):
    info = name
    info = info.split('@')
    companyName =  info[1]
    companyName= companyName.split('.')
    return (companyName[0])

Email = input ("Enter EmailAddress      ")

print (extractName(Email))
