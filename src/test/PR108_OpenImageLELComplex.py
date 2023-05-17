from carta.session import Session
from carta.token import ControllerToken, BackendToken


## Change the Session.interact content based on the backend information
## preparation: need to finish the building of carta frontend
## open carta-backend with ./carta_backend --frontend_folder=/Users/ming-yi/carta-frontend/build --enable_scripting
session = Session.interact("http://localhost:3002/?token=79EF9541-0B6E-421F-8085-715913AC88F4", 2675186687)

## Set the image directory
directory = "/Users/ming-yi/carta-test-img/set_QA"

## Test open_LEL_image
expression = "M17_SWex.fits + M17_SWex.hdf5"
expression2 = "M17_SWex.fits * 2"
session.open_LEL_image(expression = expression, directory = directory)
session.open_LEL_image(expression = expression2, directory = directory, append = True)

## Test open_LEL_image with absolute path (NO directory), i.e. can open different images in different directories
expression3 = '"'+directory+'/M17_SWex.fits" + "'+directory+'/M17_SWex.hdf5"'
session.open_LEL_image(expression = expression3, append = True)

## Test appended open an image
expression4 = "HH211_IQU.fits"
session.open_image(path = directory+"/"+expression4, hdu="0", append=True)

## Test appended open an complex image (REAL & IMAG)
expression5 = "complex.image"
session.open_complex_image(path = directory+"/"+expression5, expression="REAL", append=True)
session.open_complex_image(path = directory+"/"+expression5, expression="IMAG", append=True)
