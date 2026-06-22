Het bijhouden van het logboek en de meeting is gedaan in OneNote, hiervoor is Joshua uitgenodigd. 

In dit project zitten 2 verschillende mappen: Resultaten en Python.
In de map 'Resultaten' zitten de gebruikte .png afbeeldingen die gebruikt zijn voor het maken van het poster. 
Deze afbeeldingen bevatten de 3 heatmaps met ratio's, de 3 losse filterafbeeldingen in RGB-kleuren, en tot slot de gestackte afbeelding van de filters.

In de map 'Python' zitten de verschillende gebruikte pythonscripts die gebruikt zijn voor de datareducie en analyse. Er wordt nu per script een uitleg gegeven wat het doet. Hiermee kan je begrijpen hoe de afbeeldingen tot stand zijn gekomen. 

          Alignment.py:
          Dit script lijnt de drie gestackte masterafbeeldingen van Hα, OIII en SII op elkaar uit. Vervolgens worden de gealigneerde FITS-bestanden opgeslagen en worden controleafbeeldingen gemaakt om de kwaliteit van de uitlijning te controleren.
          
          Calibrated_light_frames.py:
          Dit script kalibreert de dark-gecorrigeerde light frames met behulp van een master flat frame. Hierdoor worden verschillen in gevoeligheid van de detector en optische effecten gecorrigeerd, waarna de gekalibreerde afbeeldingen als nieuwe FITS-bestanden worden opgeslagen.
          
          Corrected_flat_frames.py:
          Dit script corrigeert de ruwe flat frames door het master dark frame van de bijbehorende belichtingstijd af te trekken. Hierdoor wordt thermische ruis uit de flatbeelden verwijderd en ontstaan dark-gecorrigeerde flat frames die gebruikt kunnen worden voor het maken van een master flat frame.
          
          Corrected_light_frames.py:
          Dit script corrigeert de ruwe light frames door het master dark frame van iedere opname af te trekken. Hierdoor wordt thermische ruis verwijderd en ontstaan dark-gecorrigeerde beelden die gebruikt kunnen worden voor de verdere kalibratie met een master flat frame.
          
          Histogram.ipynb:
          script voor korte visualisatie, maar niet gebruikt
          
          image_stacking_Ha.py:
          Dit script lijnt alle gekalibreerde Hα-opnamen uit en combineert deze tot één master stack. Hierdoor wordt de signaal-ruisverhouding verbeterd en ontstaat een representatieve Hα-afbeelding.
          
          image_stacking_o3.py:
          Dit script stapelt alle OIII-opnamen tot één master OIII-afbeelding. De afzonderlijke beelden worden eerst uitgelijnd en vervolgens gemiddeld.
          
          image_stacking_S2.py:
          Dit script maakt een master stack van alle SII-opnamen. Door meerdere beelden te combineren wordt het signaal versterkt en de ruis verminderd.
          
          imagestack_all.py:
          script uiteindeljk niet gebruikt voor resultaten..
          
          Master_frame_dark.py:
          Dit script combineert alle dark frames tot één master dark frame. Dit master dark frame wordt gebruikt om thermische ruis uit de light frames te verwijderen.
          
          Master_frame_flat.py:
          Dit script combineert alle flat frames tot één master flat frame. Dit master flat frame corrigeert verschillen in gevoeligheid van de sensor en optische effecten zoals vignettering.
          
          Master_frame_inspector.py:
          Dit script wordt gebruikt om master frames visueel te controleren. Hiermee kunnen eventuele afwijkingen of artefacten in de masterbeelden worden opgespoord.
          
          Ratio_heatmap.py:
          Dit script berekent de verhouding tussen de verschillende emissielijnen (OIII, Hα en SII) per pixel. De resultaten worden weergegeven als heatmaps, waarmee de ruimtelijke verdeling van de verschillende stoffen in de Crabnevel zichtbaar wordt gemaakt.
          
          SHO_images.py:
          Dit script maakt distributieafbeeldingen van Hα, OIII en SII en combineert deze tot een SHO-kleurenafbeelding. Alle afbeeldingen hebben dezelfde uitsnede en schaal, zodat ze direct met de ratio-heatmaps kunnen worden vergeleken.

Dit was de uitleg van de verschillende afbeeldigen en pythoncodes
          
