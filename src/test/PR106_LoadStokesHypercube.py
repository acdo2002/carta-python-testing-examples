from carta.session import Session
from carta.structs import StokesImage
from carta.constants import Polarization

## Change the Session.interact content based on the backend information
## preparation: need to finish the building of carta frontend
## open carta-backend with ./carta_backend --frontend_folder=/Users/ming-yi/carta-frontend/build --enable_scripting
session = Session.interact("http://localhost:3002/?token=82CCCF79-39CC-461D-B876-25DAD50565E1", 2920849320)

## Set the image directory
directory = "/Users/ming-yi/carta-test-img/set_StokesCube"

## Test open Stokes Hypercube image
HypercubeArray = [StokesImage(stokes=Polarization.I, path=''+directory+'/Orion_source_I_Stokes_I.fits', hdu="0"), 
StokesImage(stokes=Polarization.Q, path=''+directory+'/Orion_source_I_Stokes_Q.fits', hdu="0")]
session.load_stokes_hypercube(stokes_images = HypercubeArray, append=False)