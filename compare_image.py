import cv2
import numpy as np


def pre_fit(img,filtre):
    H,W = img.shape[:2]
    yh = round(H/filtre)*filtre
    yw = round(W/filtre)*filtre
    return cv2.resize(img,(yw,yh))

def do_filter(img,filtre):
    slider = np.lib.stride_tricks.sliding_window_view(img,(filtre,filtre),axis=None)[::filtre,::filtre]
    slider = np.mean(slider,axis=(-1,-2))
    return slider.astype(np.uint8)

def give_rate(img,miktar):
    H,W = img.shape[:2]
    adimH =H//miktar
    adimW = W//miktar
    if(adimH<=0 or adimW<=0):
        return [0 for i in range(miktar**2)]
    slider = np.lib.stride_tricks.sliding_window_view(img,(adimH,adimW))[::adimH,::adimW]
    slider = np.mean(slider,axis=(-1,-2))
    S = slider.shape
    return slider.reshape((S[0]*S[1]),)

def calc_puan(p1,p2):
    p1 = np.array(p1)
    p2 = np.array(p2)
    p1 = p1[:min(len(p1),len(p2))]
    p2 = p2[:min(len(p1),len(p2))]
    #print(p1.shape,p2.shape)
    sonuc = p2-p1
    sonuc = np.absolute(sonuc)
    return np.sum(sonuc)/len(sonuc)

def compare(buyuk,kucuk,filtre=5): 
    Bgri = buyuk.copy()
    Kgri = kucuk.copy()

    Bgri = pre_fit(Bgri,filtre)
    Kgri = pre_fit(Kgri,filtre)

    Bf = do_filter(Bgri,filtre)
    Kf = do_filter(Kgri,filtre)

    bOran = give_rate(Bf,8)
    kOran = give_rate(Kf,8)

    puan = calc_puan(bOran,kOran)
    return puan
 

im0 = cv2.imread("0_img.jpg",0)
im1 = cv2.imread("1_img.jpg",0)
print(compare(im1,im1))