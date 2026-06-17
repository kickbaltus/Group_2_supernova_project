import os
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

# ==========================================================
# PADEN
# ==========================================================

input_dir = r"C:\Documents\GitHub\Offline_bestanden_project\Ruwe_data\Alligned_afbeeldingen"

output_dir = r"C:\Documents\GitHub\Offline_bestanden_project\Ruwe_data\RGB_filter_visualisations"

os.makedirs(output_dir, exist_ok=True)

# ==========================================================
# INLADEN
# ==========================================================

ha = fits.getdata(
    os.path.join(input_dir, "Ha_aligned.fits")
).astype(np.float32)

oiii = fits.getdata(
    os.path.join(input_dir, "OIII_aligned.fits")
).astype(np.float32)

sii = fits.getdata(
    os.path.join(input_dir, "SII_aligned.fits")
).astype(np.float32)

print("Beelden geladen.")

# ==========================================================
# ZELFDE CROP ALS HEATMAPS
# ==========================================================

xmin = 1875
xmax = 2775

ymin = 2100
ymax = 3000

ha = ha[ymin:ymax, xmin:xmax]
oiii = oiii[ymin:ymax, xmin:xmax]
sii = sii[ymin:ymax, xmin:xmax]

# ==========================================================
# STRETCH FUNCTIE
# ==========================================================

def stretch(img):

    img = img.copy()

    img -= np.nanpercentile(img, 1)

    img[img < 0] = 0

    img = np.arcsinh(img)

    vmax = np.nanpercentile(img, 99.7)

    if vmax > 0:
        img /= vmax

    img = np.clip(img, 0, 1)

    return img

# ==========================================================
# GESTRETCHTE DATA
# ==========================================================

ha_disp = stretch(ha)
oiii_disp = stretch(oiii)
sii_disp = stretch(sii)

# ==========================================================
# RGB FILTERAFBEELDINGEN
# ==========================================================

ha_rgb = np.dstack([
    np.zeros_like(ha_disp),
    0.67 * ha_disp,
    np.zeros_like(ha_disp)
])

oiii_rgb = np.dstack([
    np.zeros_like(oiii_disp),
    0.40 * oiii_disp,
    1.00 * oiii_disp
])

sii_rgb = np.dstack([
    0.80 * sii_disp,
    np.zeros_like(sii_disp),
    np.zeros_like(sii_disp)
])

# ==========================================================
# SHO COMBINATIE
# ==========================================================

sho_rgb = np.dstack([
    0.80*sii_disp,
    0.67*ha_disp + 0.40*oiii_disp,
    1.00*oiii_disp
])

# ==========================================================
# PLOT FUNCTIE
# ==========================================================

def save_rgb(rgb, title, filename):

    plt.figure(figsize=(7,7))

    plt.imshow(
        rgb,
        origin="lower"
    )

    plt.xlabel("X-axis pixel number (-)")
    plt.ylabel("Y-axis pixel number (-)")

    plt.title(title)

    plt.tight_layout()

    plt.savefig(
        os.path.join(output_dir, filename),
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    plt.close()

# ==========================================================
# OPSLAAN
# ==========================================================

save_rgb(
    ha_rgb,
    "Distribution Hα",
    "01_Ha_distribution.png"
)

save_rgb(
    oiii_rgb,
    "Distribution OIII",
    "02_OIII_distribution.png"
)

save_rgb(
    sii_rgb,
    "Distribution SII",
    "03_SII_distribution.png"
)

save_rgb(
    sho_rgb,
    "Combined distribution (SHO)",
    "04_SHO_distribution.png"
)

print("\nAfbeeldingen opgeslagen.")