import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage
import astroalign as aa
from skimage.registration import phase_cross_correlation
from scipy.ndimage import shift
from astropy.io import fits

# ==========================================================
# INPUT MAPPEN
# ==========================================================

input_dir = r"C:\Documents\GitHub\Offline_bestanden_project\Ruwe_data\Gestackte_afbeeldingen"

output_dir = r"C:\Documents\GitHub\Offline_bestanden_project\Ruwe_data\Alligned_afbeeldingen"

os.makedirs(output_dir, exist_ok=True)

# ==========================================================
# AUTOMATISCH ZOEKEN
# ==========================================================

fits_files = [
    f for f in os.listdir(input_dir)
    if f.lower().endswith(".fits")
]

ha_path = None
oiii_path = None
sii_path = None

for f in fits_files:

    name = f.lower()

    if "ha" in name:
        ha_path = os.path.join(input_dir, f)

    elif "oiii" in name or "o3" in name:
        oiii_path = os.path.join(input_dir, f)

    elif "sii" in name or "s2" in name:
        sii_path = os.path.join(input_dir, f)

print("Gevonden bestanden:")
print("Ha   :", ha_path)
print("OIII :", oiii_path)
print("SII  :", sii_path)

if ha_path is None:
    raise RuntimeError("Geen Ha FITS gevonden.")

if oiii_path is None:
    raise RuntimeError("Geen OIII FITS gevonden.")

if sii_path is None:
    raise RuntimeError("Geen SII FITS gevonden.")

# ==========================================================
# FUNCTIES
# ==========================================================

def orient_image(img):

    img = np.rot90(img, k=1)
    img = np.flipud(img)

    return img


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


def save_grayscale(img, title, filename):

    disp = stretch(img)

    plt.figure(figsize=(10, 10))

    plt.imshow(
        disp,
        cmap="gray",
        origin="lower"
    )

    plt.title(title)
    plt.axis("off")

    plt.tight_layout()

    plt.savefig(
        os.path.join(output_dir, filename),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


# ==========================================================
# LOAD
# ==========================================================

print("Inladen bestanden...")

ha = fits.getdata(ha_path).astype(np.float32)
oiii = fits.getdata(oiii_path).astype(np.float32)
sii = fits.getdata(sii_path).astype(np.float32)

# ==========================================================
# ORIENTATIE
# ==========================================================

print("Roteren en flippen...")

ha = orient_image(ha)
oiii = orient_image(oiii)
sii = orient_image(sii)

print("Afmetingen:")
print("Ha  :", ha.shape)
print("OIII:", oiii.shape)
print("SII :", sii.shape)

# ==========================================================
# ORIGINELE CONTROLEPLOTS
# ==========================================================

save_grayscale(
    ha,
    "Original Ha",
    "01_Ha_original.png"
)

save_grayscale(
    oiii,
    "Original OIII",
    "02_OIII_original.png"
)

save_grayscale(
    sii,
    "Original SII",
    "03_SII_original.png"
)

# ==========================================================
# ALIGNMENT PREP
# ==========================================================

print("\nMedian filtering voor sterdetectie...")

ha_clean = ndimage.median_filter(ha, size=3)
oiii_clean = ndimage.median_filter(oiii, size=3)
sii_clean = ndimage.median_filter(sii, size=3)

ha_clean = np.arcsinh(ha_clean)
oiii_clean = np.arcsinh(oiii_clean)
sii_clean = np.arcsinh(sii_clean)

# ==========================================================
# ALIGN OIII -> HA
# ==========================================================

print("\nBepalen verschuiving OIII -> Ha")

shift_oiii, error, diffphase = phase_cross_correlation(
    ha_clean,
    oiii_clean,
    upsample_factor=10
)

print("OIII shift:", shift_oiii)

oiii_aligned = shift(
    oiii,
    shift=shift_oiii,
    mode="constant",
    cval=np.nan
)

# ==========================================================
# ALIGN SII -> HA
# ==========================================================

print("\nBepalen verschuiving SII -> Ha")

shift_sii, error, diffphase = phase_cross_correlation(
    ha_clean,
    sii_clean,
    upsample_factor=10
)

print("SII shift:", shift_sii)

sii_aligned = shift(
    sii,
    shift=shift_sii,
    mode="constant",
    cval=np.nan
)

# ==========================================================
# REFERENTIE
# ==========================================================

ha_aligned = ha.copy()

# ==========================================================
# FITS EXPORT
# ==========================================================

print("\nOpslaan aligned FITS...")

fits.writeto(
    os.path.join(output_dir, "Ha_aligned.fits"),
    ha_aligned,
    overwrite=True
)

fits.writeto(
    os.path.join(output_dir, "OIII_aligned.fits"),
    oiii_aligned,
    overwrite=True
)

fits.writeto(
    os.path.join(output_dir, "SII_aligned.fits"),
    sii_aligned,
    overwrite=True
)

# ==========================================================
# ALIGNED CONTROLEPLOTS
# ==========================================================

save_grayscale(
    ha_aligned,
    "Aligned Ha",
    "04_Ha_aligned.png"
)

save_grayscale(
    oiii_aligned,
    "Aligned OIII",
    "05_OIII_aligned.png"
)

save_grayscale(
    sii_aligned,
    "Aligned SII",
    "06_SII_aligned.png"
)

# ==========================================================
# RGB ALIGNMENT CHECK
# ==========================================================

print("RGB controlebeeld maken...")

rgb = np.dstack([
    stretch(sii_aligned),   # rood
    stretch(ha_aligned),    # groen
    stretch(oiii_aligned)   # blauw
])

plt.figure(figsize=(12, 12))

plt.imshow(
    rgb,
    origin="lower"
)

plt.title("RGB Alignment Check")
plt.axis("off")

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "07_RGB_alignment_check.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# ==========================================================
# OVERLAP MASK
# ==========================================================

print("Overlap mask maken...")

overlap = (
    np.isfinite(ha_aligned)
    & np.isfinite(oiii_aligned)
    & np.isfinite(sii_aligned)
)

plt.figure(figsize=(10, 10))

plt.imshow(
    overlap,
    cmap="gray",
    origin="lower"
)

plt.title("Common Overlap Region")
plt.axis("off")

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "08_overlap_mask.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# ==========================================================
# KLAAR
# ==========================================================

print("\n===================================")
print("Alignment voltooid")
print("Controleer:")
print(" - 07_RGB_alignment_check.png")
print(" - 08_overlap_mask.png")
print("===================================")