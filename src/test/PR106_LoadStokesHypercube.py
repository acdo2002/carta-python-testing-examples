from carta.session import Session
from carta.structs import StokesImage
from carta.constants import Polarization

## Change the Session.interact content based on the backend information
## preparation: need to finish the building of carta frontend
## open carta-backend with ./carta_backend --frontend_folder=/Users/ming-yi/carta-frontend/build --enable_scripting
session = Session.interact("http://localhost:3002/?token=D1EB3979-97CB-4DB2-A26A-8A2F2D0A49D7", 1175470984)

## Set the image directory
directory = "/Users/ming-yi/carta-test-img/set_StokesCube"

## Test open Stokes Hypercube image
HypercubeArray = [StokesImage(stokes=Polarization.I, path=''+directory+'/Orion_source_I_Stokes_I.fits', hdu="0"), 
StokesImage(stokes=Polarization.Q, path=''+directory+'/Orion_source_I_Stokes_Q.fits', hdu="0"),
StokesImage(stokes=Polarization.U, path=''+directory+'/Orion_source_I_Stokes_U.fits', hdu="0")]
session.load_stokes_hypercube(stokes_images = HypercubeArray, append=False)