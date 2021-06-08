#!/usr/bin/env python
# coding: utf-8

# Voorpagina
# =======================

# In[1]:


import os
import pandas as pd
import numpy as np
import plotly.express as px

os.getcwd()

# !wget  https://www.rijkswaterstaat.nl/apps/geoservices/geodata/dmc/bron/01-01-2010_31-12-2019.zip  


# ````{margin}
# ```{note}
# Here is a note!
# ```
# ````

# In[2]:


# puntlocatie = pd.read_csv('/Afstudeerproject/Data/01-01-2010_31-12-2019 (BRON)/PGS0112-o-CSV-bestand-J-1-N-J-N/Netwerkgegevens/puntlocaties.txt')


# In[3]:


# puntlocatie


# In[4]:


# # usecols=['WVK_BEGDAT', 'FK_VELD5', 'KLOK_BEG', 'KLOK_END']
# wegvakken = pd.read_csv('Verkeersongevallen/01-01-2010_31-12-2019/PGS0112-o-CSV-bestand-J-1-N-J-N/Netwerkgegevens/wegvakken.txt')

# wegvakken.columns


# In[5]:


# ongevallen = pd.read_csv('Verkeersongevallen/01-01-2010_31-12-2019/PGS0112-o-CSV-bestand-J-1-N-J-N/Ongevallengegevens/ongevallen.txt')
# display(ongevallen.shape)
# display(ongevallen.columns)
# ongevallen.head()


# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Voorblad
# 
# abstract
# inhoudsopgave
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Introductie
# 
# introductie
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Methodologie, onderzoeksmethode of onderzoeksopzet
# 
# methoden
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Referentie
# 
# referentie
# ```
# 
