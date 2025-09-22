"""
TPD - Théorie Polyvagale Digitale
=================================

Une architecture neuro-inspirée pour la modélisation et l'orchestration 
de la résilience des systèmes complexes, basée sur la Théorie Polyvagale.

La tripartition neuro-numérique :
- VENTRAL : État de sécurité et d'engagement social
- SYMPATHETIC : État de mobilisation et d'activation 
- DORSAL : État d'effondrement et de conservation

Architecture Guardian/Predator pour la souveraineté des systèmes.
"""

from .etats import EtatPolyvagal, EtatVentral, EtatSympathetic, EtatDorsal, NiveauResilience
from .architecture import Guardian, Predator, SystemeResilience, EvenementSysteme, StrategieAdaptive
from .conscience import ConscienceSituationnelle, NiveauConscience, PerceptionSensorielle, PatternRecognition
from .souverainete import SouveraineteNumerique, NiveauSouverainete, DomaineSouverainete, MetriqueSouverainete, DependanceExterne, CapaciteInterne

__version__ = "0.1.0"
__author__ = "Sentire Dynamics"
__doctrine__ = "TPD - Théorie Polyvagale Digitale"

__all__ = [
    # États polyvagaux
    "EtatPolyvagal",
    "EtatVentral", 
    "EtatSympathetic",
    "EtatDorsal",
    "NiveauResilience",
    
    # Architecture Guardian/Predator
    "Guardian",
    "Predator",
    "SystemeResilience",
    "EvenementSysteme",
    "StrategieAdaptive",
    
    # Conscience situationnelle
    "ConscienceSituationnelle",
    "NiveauConscience",
    "PerceptionSensorielle",
    "PatternRecognition",
    
    # Souveraineté numérique
    "SouveraineteNumerique",
    "NiveauSouverainete",
    "DomaineSouverainete",
    "MetriqueSouverainete",
    "DependanceExterne",
    "CapaciteInterne",
]