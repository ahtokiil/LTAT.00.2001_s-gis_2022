from PIL import Image
from colour import Color
from math import floor, sqrt
from andmed import andmed2
from värvid_tekst import värvid


def get_rgb(color: Color) -> tuple[int, int, int]:
    """
    Funktsioon võtab sisse python Color objekti ning tagastab värvi RGB väärtused tuple kujul
    """
    return (round(color.red * 255), round(color.green * 255), round(color.blue * 255))

def gradient(first: str, n: int, defaultStep: int) -> list:
    """
    Funktsioon võtab sisse esimese värvi nime stringi kujul ning
    tagastab n-elemendilise listi värvidest.
    """
    kõikvärvid = []
    for värv in värvid.values():                            # loob listi heksakoodidest
        kõikvärvid.append(värv)

    step = defaultStep                                      # step väärtus määrab värvi laiuse
    gradient = []
    värv_indeks = kõikvärvid.index(värvid[first])           # seab listi esimeseks elemendiks argumendiga antud värvi

    for i in range(n):                                      # loob n-elemendilise listi (list tuleb tegelikult alati pikem, kuid n on siin minimaalne listi pikkus mida on vaja)
        currentColor = kõikvärvid[värv_indeks]
        for j in range(step):                               # värv lisatakse listi nii mitu korda, kui suur on värvi laius
            gradient.append(currentColor)
        värv_indeks += 1                                    
        if värv_indeks > len(kõikvärvid) -1:                # kui indeks läheb listi piiridest välja, siis liigutatakse see tagasi algusesse
            värv_indeks -= len(kõikvärvid)
        step = max(step - andmed2[n], 1)                    # värvi laius muutub vastavalt tempo muutusele
    return gradient

def laine(width: int, height: int, startColor: str) -> Image:
    """
    Genereerib mõõtmetega (width, height) pildi, kus toimub värvide üleminek vasakult paremale
    alates värvist startColor.
    """
    print('Pildi loomine...')
    img = Image.new('RGB', (width, height))
    
    firstColor = startColor
    
    scale = width                                           # gradienti pikkus on pildi laius
    colors = gradient(firstColor, scale, 4)         

    for x in range(width):
        for y in range(height):
            rgb = get_rgb(Color(colors[x]))                 
            img.putpixel((x,y), rgb)                        # valib piksli värvi seades vastavusse piksli x-koordinaadi ja gradientis samal indeksil asuva värviga

    img.save('laine.png')                                   # salvestab pildi failina laine.png ning tagastab pildi
    return img                                                  

def ring(width: int, height: int, startColor: str) -> Image:
    """
    Genereerib mõõtmetega (width, height) pildi, kus toimub värvide üleminek ringikujuliselt seest välja
    alates värvist startColor.
    """
    print('Pildi loomine...')
    img = Image.new('RGB', (width, height))
    
    firstColor = startColor
    scale = floor(sqrt(width**2 + height**2))               # gradienti pikkus on vahemaa pildi nurgast keskpunkti
    colors = gradient(firstColor, scale, 2)

    for x in range(width):
        for y in range(height):
            r = floor(sqrt((abs(width//2 - x)//2)**2 + (abs(height//2 - y)//2)**2))     # arvutab piksli kauguse keskpunktist 
            rgb = get_rgb(Color(colors[r]))                                             # ja seab selle kauguse vastavusse gradienti vastaval indeksil asuva värviga
            img.putpixel((x,y), rgb)

    img.save('ring.png')                                    #salvestab pildi failina ring.png ja tagastab pildi 
    return img

