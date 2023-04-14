import copy
import numpy as xp
import astropy.units as u

psd_random = xp.random.RandomState()


def kneePSD(f,beta,fn,alpha):
    psd = beta/(1+f/fn)**alpha
    try:
        psd.decompose()
        return psd
    except:
        return psd
    
    
class wfe_time():
    #test 2D generation of a time series from PSD
    def __init__(self, screen_size,zerns_size,pixelscale,seed=None):
        print("still not tested")
        if seed is not None:
            psd_random.seed(seed)
        self.time_noise=psd_random.normal(loc=0,size=(screen_size,zerns_size))*u.nm
        self. freq_noise1 = xp.fft.fftn(time_noise,axes=[0])
        self.screen_size=screen_size
        self.zerns_size=zerns_size
        self.pixelscale=pixelscale
        
    def scaled_psd(self):
        psd_scaled1 = np.einsum("ij,i->ij", 
                        freq_noise1,
                        xp.sqrt(psd/(pixelscale.value**2))) 

        filtered=xp.fft.fftn(psd_scaled1,axes=[0])*np.sqrt(N)
        

        filtered = np.einsum('ab,b->ab', filtered,
                                xp.sqrt(spatial_psd/(pixelscale.value**2))) #https://obilaniu6266h16.wordpress.com/2016/02/04/einstein-summation-in-numpy/
        filtered *= Amp/filtered.std()
        filtered=filtered-filtered[0,:]
