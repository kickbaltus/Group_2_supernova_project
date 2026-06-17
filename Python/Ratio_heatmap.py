import os
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from scipy import ndimage
from matplotlib.colors import LinearSegmentedColormap

# ==========================================================
# PADEN
# ==========================================================

input_dir = r"C:\Documents\GitHub\Offline_bestanden_project\Ruwe_data\Alligned_afbeeldingen"

output_dir = r"C:\Documents\GitHub\Offline_bestanden_project\Ruwe_data\Ratio_heatmaps"

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
# WAARDE CHECKS
# ==========================================================

for name, img in [("Ha", ha), ("OIII", oiii), ("SII", sii)]:

    print(f"\n{name}")

    print("P50 :", np.nanpercentile(img,50))
    print("P90 :", np.nanpercentile(img,90))
    print("P95 :", np.nanpercentile(img,95))
    print("P99 :", np.nanpercentile(img,99))
    print("P99.9 :", np.nanpercentile(img,99.9))

# ==========================================================
# CROP CRAB NEBULA
# ==========================================================

xmin = 1875
xmax = 2775

ymin = 2100
ymax = 3000

ha = ha[ymin:ymax, xmin:xmax]
oiii = oiii[ymin:ymax, xmin:xmax]
sii = sii[ymin:ymax, xmin:xmax]

print("Nieuwe shape:")
print("Ha  :", ha.shape)
print("OIII:", oiii.shape)
print("SII :", sii.shape)   

# ==========================================================
# SIGNAALMASKER
# ==========================================================

signal = np.maximum.reduce([
    ha,
    oiii,
    sii
])

signal_threshold = 1.2

signal_mask = (
    signal > signal_threshold
)

print(
    "Pixels boven threshold:",
    np.sum(signal_mask)
)

# ==========================================================
# MASKER TEGEN DELEN DOOR BIJNA NUL
# ==========================================================

threshold = 0.001

# ==========================================================
# RATIO'S
# ==========================================================

eps = 1e-6

ratio_oiii_ha = np.full_like(
    ha,
    np.nan,
    dtype=np.float32
)

ratio_sii_ha = np.full_like(
    ha,
    np.nan,
    dtype=np.float32
)

ratio_oiii_sii = np.full_like(
    ha,
    np.nan,
    dtype=np.float32
)

valid = (
    np.isfinite(ha)
    & np.isfinite(oiii)
    & np.isfinite(sii)
)

ratio_oiii_ha[valid] = (
    oiii[valid]
    / (ha[valid] + eps)
)

ratio_sii_ha[valid] = (
    sii[valid]
    / (ha[valid] + eps)
)

ratio_oiii_sii[valid] = (
    oiii[valid]
    / (sii[valid] + eps)
)

# ==========================================================
# LOG RATIO
# ==========================================================

log_oiii_ha = np.full_like(
    ratio_oiii_ha,
    np.nan
)

log_sii_ha = np.full_like(
    ratio_sii_ha,
    np.nan
)

log_oiii_sii = np.full_like(
    ratio_oiii_sii,
    np.nan
)

mask = ratio_oiii_ha > 0
log_oiii_ha[mask] = np.log10(
    ratio_oiii_ha[mask]
)

mask = ratio_sii_ha > 0
log_sii_ha[mask] = np.log10(
    ratio_sii_ha[mask]
)

mask = ratio_oiii_sii > 0
log_oiii_sii[mask] = np.log10(
    ratio_oiii_sii[mask]
)

# ==========================================================
# ACHTERGROND VERWIJDEREN
# ==========================================================

log_oiii_ha[~signal_mask] = np.nan
log_sii_ha[~signal_mask] = np.nan
log_oiii_sii[~signal_mask] = np.nan

# ==========================================================
# FITS EXPORT
# ==========================================================

fits.writeto(
    os.path.join(output_dir, "OIII_Ha_ratio.fits"),
    ratio_oiii_ha,
    overwrite=True
)

fits.writeto(
    os.path.join(output_dir, "SII_Ha_ratio.fits"),
    ratio_sii_ha,
    overwrite=True
)

fits.writeto(
    os.path.join(output_dir, "OIII_SII_ratio.fits"),
    ratio_oiii_sii,
    overwrite=True
)

# ==========================================================
# HEATMAP FUNCTIE
# ==========================================================

def show_and_save(
    data,
    title,
    filename,
    cmap,
    top_label,
    top_color,
    bottom_label,
    bottom_color,
    cbar_label
):

    cmap = cmap.copy()

    # achtergrond zwart
    cmap.set_bad("black")

    plt.figure(figsize=(10,10))

    plt.imshow(
        data,
        cmap=cmap,
        origin="lower",
        vmin=-1,
        vmax=1
    )

    cbar = plt.colorbar(
    label=cbar_label,
    shrink=0.72
)

    # tekst naast de colorbar
    cbar.ax.text(
        2.7,
        1.0,
        top_label,
        color=top_color,
        fontsize=11,
        ha="left",
        va="center",
        transform=cbar.ax.transAxes
    )

    

    cbar.ax.text(
        2.7,
        0.0,
        bottom_label,
        color=bottom_color,
        fontsize=11,
        ha="left",
        va="center",
        transform=cbar.ax.transAxes
    )

    plt.title(title)

    plt.xlabel("X-axis pixel number (-)")
    plt.ylabel("Y-axis pixel number (-)")

    plt.tight_layout()

    plt.savefig(
        os.path.join(output_dir, filename),
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    plt.close()

# ==========================================================
# SHO COLORMAPS
# ==========================================================

cmap_oiii_ha = LinearSegmentedColormap.from_list(
    "OIII_Ha",
    [
        "#00aa00",   # Ha dominant = groen
        "#ffffff",
        "#0066ff"    # OIII dominant = blauw
    ]
)

cmap_sii_ha = LinearSegmentedColormap.from_list(
    "SII_Ha",
    [
        "#00aa00",   # Ha dominant = groen
        "#ffffff",
        "#cc0000"    # SII dominant = rood
    ]
)

cmap_oiii_sii = LinearSegmentedColormap.from_list(
    "OIII_SII",
    [
        "#cc0000",   # SII dominant = rood
        "#ffffff",
        "#0066ff"    # OIII dominant = blauw
    ]
)

# ==========================================================
# HEATMAPS
# ==========================================================

print("\nHeatmaps maken...")

show_and_save(
    log_oiii_ha,
    "Distribution (OIII / Ha)",
    "OIII_Ha_heatmap.png",
    cmap_oiii_ha,
    top_label=" OIII\n dominant",
    top_color="blue",
    bottom_label=" Ha\n dominant",
    bottom_color="green",
    cbar_label="Ratio OIII / Ha (-)\nlog$_{10}$ scale"
)

show_and_save(
    log_sii_ha,
    "Distribution (SII / Ha)",
    "SII_Ha_heatmap.png",
    cmap_sii_ha,
    top_label=" SII\n dominant",
    top_color="red",
    bottom_label=" Ha\n dominant",
    bottom_color="green",
    cbar_label="Ratio SII / Ha (-)\nlog$_{10}$ scale"
)

show_and_save(
    log_oiii_sii,
    "Distribution (OIII / SII)",
    "OIII_SII_heatmap.png",
    cmap_oiii_sii,
    top_label=" OIII\n dominant",
    top_color="blue",
    bottom_label=" SII\n dominant",
    bottom_color="red",
    cbar_label="Ratio OIII / SII (-)\nlog$_{10}$ scale"
)

print("\nHeatmaps opgeslagen.")